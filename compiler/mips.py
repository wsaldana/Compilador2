import sys


def custom_split(input_string):
    result = []
    current_word = ""
    inside_quotes = False

    for char in input_string:
        if char == ' ' and not inside_quotes:
            if current_word:
                result.append(current_word)
                current_word = ""
        elif char == '"':
            inside_quotes = not inside_quotes
            current_word += char
        else:
            current_word += char

    if current_word:
        result.append(current_word)

    return result


def main():
    print(".text")
    print(".globl main")

    addrs = {}
    tabs = ''
    cls_attrs = []
    open_data = True
    inClass = False
    n_label_t = 0
    n_label_e = 0
    pops = 0
    pushes = 0
    gets = 0
    returns = 0

    with open('tac', 'r') as tac:
        for line in tac:
            line = line[:-1]
            tokens = custom_split(line)

            if not tokens:
                continue

            if inClass:
                if open_data:
                    print(f"{tabs}.data")
                    open_data = False

                if tokens[0] == 'FUNC':
                    inClass = False
                    open_data = True
                else:
                    if '.' in tokens[0]:
                        name = tokens[0].split('.')[1]
                    else:
                        name = tokens[0]
                    value = 0 if tokens[2] == 'NONE' else tokens[2]
                    if 'NEW' in tokens:
                        value = tokens[3]
                    if '"' in tokens[2]:
                        print(f"{tabs}{name}: .asciiz {value}")
                    else:
                        print(f"{tabs}{name}: .word {value}")
                    continue

            if '+' in tokens:
                name = tokens[0].replace("_", '')
                a = tokens[2]
                b = tokens[4]
                a = addrs[a] if a in addrs.keys() else a
                b = addrs[b] if b in addrs.keys() else b
                print(f"{tabs}add ${name}, {a}, {b}")
            elif '-' in tokens:
                name = tokens[0].replace("_", '')
                a = tokens[2]
                b = tokens[4]
                a = addrs[a] if a in addrs.keys() else a
                b = addrs[b] if b in addrs.keys() else b
                print(f"{tabs}sub ${name}, {a}, {b}")
            elif '*' in tokens:
                name = tokens[0].replace("_", '')
                a = tokens[2]
                b = tokens[4]
                a = addrs[a] if a in addrs.keys() else a
                b = addrs[b] if b in addrs.keys() else b
                print(f"{tabs}mul ${name}, {a}, {b}")
            elif '==' in tokens:
                a = tokens[0].replace("_", '$')
                b = tokens[2].replace("_", '')
                c = tokens[4] if tokens[4] != '0' else '$zero'
                print(f"{tabs}lw {a}, {b}")
                print(f"{tabs}beq {a}, {c}, Label_True_{n_label_t}")
                print(f"{tabs}li {a}, 0")
                print(f"{tabs}j Label_End_{n_label_e}")
                print(f"{tabs}Label_True_{n_label_t}:")
                print(f"{tabs}li {a}, 0")
                print(f"{tabs}Label_End_{n_label_e}:")
                n_label_t += 1
                n_label_e += 1
            elif 'out_int' in tokens:
                print(f'{tabs}syscall')
            elif tokens[0] == 'CALL':
                print(f'{tabs}j {tokens[1]}')
            elif 'NEW' in tokens:
                pass
            elif 'CALL' in tokens:
                print(f'{tabs}j {tokens[3].split(".")[1]}')
            elif tokens[0] == 'PARAMS':
                call_params = tokens[1]
            elif 'PUSH' in tokens:
                arg = f'$a{pushes}'
                pushes += 1
                val = tokens[1].replace("_", '$')
                print(f'{tabs}lw {arg}, {val}')
            elif 'POP' in tokens:
                arg = f'$a{pops}'
                pops += 1
                name = tokens[0]
                print(f'{tabs}lw {arg}, {name}')
            elif 'RETURN' in tokens:
                arg = f'$r{returns}'
                returns += 1
                val = tokens[1].replace("_", '$')
                print(f'{tabs}lw {arg}, {val}')
            elif 'GET' in tokens:
                arg = f'$r{gets}'
                gets += 1
                name = tokens[0]
                print(f'{tabs}lw {arg}, {name}')
            elif '=' in tokens:
                name = tokens[0].replace("_", '')
                addrs[tokens[0]] = name
                value = tokens[2]
                if value in addrs.keys():
                    print(f"{tabs}lw ${name}, {addrs[value]}")
                else:
                    print(f"{tabs}lw ${name}, {value}")
            elif tokens[0] == 'goto':
                print(f"{tabs}j {tokens[1].replace('_', '')}")
            elif tokens[0] == 'CLASS':
                print(f'{tokens[1]}:')
                tabs = '\t'
                inClass = True
            elif tokens[0] == 'FUNC':
                inClass = False
                curr_func = tokens[1].split(".")[1]
                print(f'{tabs}{curr_func}:')
                tabs = '\t\t'
            elif tokens[0].startswith("_L"):
                print(f"{tabs}{tokens[0][1:]}")
            elif tokens[0] == 'if':
                crit = tokens[1].replace("_", '')
                label = tokens[-1].replace("_", '')
                print(f"{tabs}beq ${crit}, $zero, {label}")
            elif 'END_FUNC' in tokens:
                print(f"{tabs}j $ra")
            else:
                print(tabs, tokens)


class Tee(object):
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)

    def flush(self):
        pass


if __name__ == '__main__':
    f = open('mips.s', 'w')
    backup = sys.stdout
    sys.stdout = Tee(sys.stdout, f)

    main()

    sys.stdout = backup
