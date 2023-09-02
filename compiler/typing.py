import sys
from antlr4 import InputStream, CommonTokenStream
from compiler.grammar.yaplLexer import yaplLexer
from compiler.grammar.yaplParser import yaplParser
from compiler.grammar.yaplVisitor import yaplVisitor
from utils.errors.Errors import ErrorListener


class TypingVisitor(yaplVisitor):

    def __init__(self) -> None:
        super().__init__()

    def visitAttr(self, ctx: yaplParser.AttrContext):
        pos = ctx.getSourceInterval()
        for child in ctx.children:
            if isinstance(child, yaplParser.ExprContext):
                if len(child.getTokens(45)) > 0:
                    err = ErrorListener()
                    err.syntaxError(
                        None,
                        None,
                        pos[0] - 1,
                        pos[1],
                        "Unable to assign String to Int variable",
                        None
                    )
                if len(child.getTokens(42)) > 0:
                    err = ErrorListener()
                    err.syntaxError(
                        None,
                        None,
                        pos[0],
                        pos[1],
                        "Unable to assign Bool to Int variable",
                        None
                    )

    def visitExpr(self, ctx: yaplParser.ExprContext):
        if ctx.getToken(2, 0):
            var = ctx.varTypescript()[0]
            self.visitAttr(var)
        return self.visitChildren(ctx)


def main():
    file = sys.argv[1]
    input_stream = InputStream(file)
    lexer = yaplLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = yaplParser(stream)

    tree = parser.program()
    visitor = TypingVisitor()
    visitor.visit(tree)


if __name__ == '__main__':
    main()
