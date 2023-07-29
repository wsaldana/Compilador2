import sys
import os

from antlr4 import FileStream, CommonTokenStream

from compiler.grammar.yaplLexer import yaplLexer
from compiler.grammar.yaplParser import yaplParser
from compiler.utils.errors.Errors import ErrorListener


def main():
    try:
        file = sys.argv[1]
        input_stream = FileStream(file)
    except Exception as e:
        raise Exception("Error with the file", e)

    lexer = yaplLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    error_listener_lexer = ErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener_lexer)

    parser = yaplParser(token_stream)
    error_listener_parser = ErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener_parser)

    parser.program()

    for i in token_stream.tokens:
        if i.type == yaplLexer.ERROR:
            print(f"ERROR: Bad token: {i}")
            continue
        print(i)

    if error_listener_lexer.true or error_listener_parser.true:
        print("\nFile has errors")
        exit(1)

    process = os.popen(
        'antlr4-parse compiler/grammar/yapl.g4 program -gui',
        'w'
    )
    process.write(input_stream.strdata)
    process.close()


if __name__ == '__main__':
    main()
