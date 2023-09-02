import sys
from antlr4 import InputStream, CommonTokenStream
from compiler.grammar.yaplLexer import yaplLexer
from compiler.grammar.yaplParser import yaplParser
from compiler.grammar.yaplVisitor import yaplVisitor
from dataclasses import dataclass
from antlr4.tree.Tree import TerminalNodeImpl


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, value):
        self.symbols[name] = value

    def get_symbols(self):
        return self.symbols

    def items(self):
        return self.symbols.items()

    def to_string(self, table=None, tabs=""):
        table = self if table is None else table
        string = ''
        for k, v in table.items():
            string += tabs + k + ": " + str(v) + "\n"
            if v.refs:
                string += self.to_string(v.refs, tabs + "\t")
        return string

    def __repr__(self) -> str:
        return f"SymbolTable{tuple(self.symbols.keys())}"

    def __str__(self) -> str:
        return self.__repr__()


@dataclass
class MethodTyping:
    attrs: tuple
    rtrn: str

    def __repr__(self) -> str:
        return f"{self.attrs} -> {self.rtrn}"


@dataclass
class Symbol:
    name: str
    type: str or MethodTyping
    refs: SymbolTable = None


class SymbolsVisitor(yaplVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.current_scope = self.symbol_table
        self.parent_scopes = {}

    def visitAttr(self, ctx: yaplParser.AttrContext):
        # name = ctx.getToken(44, 0).getText()
        name = ctx.ID_VAR().getText()
        ttype = ctx.getToken(44, 0).getText()
        sym = Symbol(name, ttype)
        parent = ctx.parentCtx
        while isinstance(parent, yaplParser.FeatureDefinitionContext):
            parent = parent.parentCtx
        while isinstance(parent, yaplParser.ExprContext):
            parent = parent.parentCtx
        self.parent_scopes[id(parent)].add_symbol(name, sym)

    def visitExpr(self, ctx: yaplParser.ExprContext):
        if ctx.getToken(2, 0):
            var = ctx.varTypescript()[0]
            self.visitAttr(var)
        return self.visitChildren(ctx)

    def visitProgram(self, ctx: yaplParser.ProgramContext):
        for child in ctx.getChildren():
            if isinstance(child, yaplParser.ClassDefinitionContext):
                self.visitClassDefinition(child)

    def visitClassDefinition(self, ctx: yaplParser.ClassDefinitionContext):
        temp_scope = SymbolTable()
        self.parent_scopes[id(ctx)] = temp_scope
        name = ctx.getToken(44, 0).getText()
        ttype = ctx.getToken(1, 0).getText()
        sym = Symbol(name, ttype, temp_scope)
        self.symbol_table.add_symbol(name, sym)
        return self.visitChildren(ctx)

    def visitMethodDef(self, ctx: yaplParser.MethodDefContext):
        # Create a scope for this method
        temp_scope = SymbolTable()
        self.parent_scopes[id(ctx)] = temp_scope

        # Add attributes to the method scope
        for attr in ctx.formal():
            name = attr.ID_VAR().getText()
            ttype = attr.getToken(44, 0).getText()
            sym = Symbol(name, ttype)
            temp_scope.add_symbol(name, sym)

        # Create a symbol from this method
        name = ctx.ID_VAR().getText()
        formals = tuple([f.TYPE_IDENTIFIER().getText() for f in ctx.formal()])
        ttype = ctx.TYPE_IDENTIFIER().getText()
        tab_type = MethodTyping(formals, ttype)
        sym = Symbol(name, tab_type, temp_scope)

        # Add this symbol to its parent scope
        parent = ctx.parentCtx
        # Parent may not be in scope, as if it is a feature
        while isinstance(parent, yaplParser.FeatureDefinitionContext):
            parent = parent.parentCtx
        self.parent_scopes[id(parent)].add_symbol(name, sym)

        # Visit its children
        return self.visitChildren(ctx)

    def get_symbol_table(self):
        return self.symbol_table


def main():
    file = sys.argv[1]
    input_stream = InputStream(file)
    lexer = yaplLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = yaplParser(stream)

    tree = parser.program()
    visitor = SymbolsVisitor()
    visitor.visit(tree)

    symbol_table = visitor.get_symbol_table()
    print(symbol_table.to_string())


if __name__ == '__main__':
    main()
