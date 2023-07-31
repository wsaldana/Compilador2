from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from compiler.grammar.yaplLexer import yaplLexer
from compiler.grammar.yaplParser import yaplParser
from compiler.grammar.yaplListener import yaplListener
from compiler.grammar.yaplVisitor import yaplVisitor


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, value):
        self.symbols[name] = value

    def get_symbols(self):
        return self.symbols

class MyCustomVisitor(yaplVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()

    def visitStatement(self, ctx: yaplParser):
        print('nel')
        id_symbol = ctx.ID().getText()
        number_value = int(ctx.NUMBER().getText())
        self.symbol_table.add_symbol(id_symbol, number_value)

    # Correct way to access statement rules in program
    def visitProgram(self, ctx: yaplParser.ProgramContext):
        for child in ctx.getChildren():
            print(child)
            if isinstance(child, yaplParser.AttributeDeclarationContext):
                print(">> ", child)
                self.visitStatement(child)
    
    def get_symbol_table(self):
        return self.symbol_table.get_symbols()

def main():
    input_stream = FileStream('../examples/recur.cl')  # Replace 'input.txt' with your input file
    lexer = yaplLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = yaplParser(stream)

    tree = parser.program()
    visitor = MyCustomVisitor()
    visitor.visit(tree)

    symbol_table = visitor.get_symbol_table()
    print(symbol_table)

if __name__ == '__main__':
    main()