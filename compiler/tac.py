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
            string += tabs + str(v) + "\n"
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
    size: int = 0
    refs: SymbolTable = None
    parent_name: str = ""
    ctx: object = None

    def __repr__(self) -> str:
        if self.type == "class":
            return f'{self.name}:'
        elif isinstance(self.type, MethodTyping):
            return f'FUNC {self.parent_name}.{self.name}:'
        elif self.type in ("Int", "Bool", "String"):
            return f'{self.name}'
        else:
            return f'Symbol({self.name}, {self.type}, {self.parent_name})'


class SymbolsVisitor(yaplVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.current_scope = self.symbol_table
        self.parent_scopes = {}
        self.sizes = {
            "Int": 4, # bytes
            "String": 20, # 2 bytes per char for a max of 10 chars
            "Bool": 1,
        }
        self.t_count = 0

    def get_t(self):
        self.t_count += 1
        return f't{self.t_count}'

    def calc_size(self, ttype: str, name: str = '') -> int:
        size = 0
        try:
            size = self.sizes[ttype]
        except KeyError:
            print(ttype)
            if ttype == 'func':
                ...
            elif ttype == 'cls':
                ...
        return size

    def visitAttr(self, ctx: yaplParser.AttrContext):
        value = ctx.expr()
        if not value:
            value = "NONE"
        else:
            if value.ID_VAR() or value.INT_VAR() or value.STR_VAR() or value.BOOL_VAR():
                value = value.getText()
            else:
                value = value.getText()
        name = f'{ctx.ID_VAR().getText()} = {value}'
        ttype = ctx.getToken(44, 0).getText()
        size = self.calc_size(ttype)
        sym = Symbol(name, ttype, size)
        parent = ctx.parentCtx
        while isinstance(parent, yaplParser.FeatureDefinitionContext):
            parent = parent.parentCtx
        while isinstance(parent, yaplParser.ExprContext):
            parent = parent.parentCtx
        self.parent_scopes[id(parent)].refs.add_symbol(name, sym)
        while parent:
            if id(parent) in self.parent_scopes.keys():
                self.parent_scopes[id(parent)].size += size
            parent = parent.parentCtx

    def visitExpr(self, ctx: yaplParser.ExprContext):
        if ctx.getToken(2, 0):
            var = ctx.varTypescript()[0]
            self.visitAttr(var)

        else:
            name = ctx.getText()
            try:
                left_operand = ctx.getChild(0)
                right_operand = ctx.getChild(2)
                operator = ctx.getChild(1).getText()
                result_variable = self.get_t() 
                name = f"{result_variable} = {left_operand} {operator} {right_operand}"
            except:
                pass
            sym = Symbol(name, "exp")

            parent = ctx.parentCtx
            while isinstance(parent, yaplParser.MethodDefContext):
                parent = parent.parentCtx
            while isinstance(parent, yaplParser.FeatureDefinitionContext):
                parent = parent.parentCtx
            while isinstance(parent, yaplParser.ExprContext):
                parent = parent.parentCtx
            self.parent_scopes[id(parent)].refs.add_symbol("EXP", sym)

        return self.visitChildren(ctx)

    def visitProgram(self, ctx: yaplParser.ProgramContext):
        for child in ctx.getChildren():
            if isinstance(child, yaplParser.ClassDefinitionContext):
                self.visitClassDefinition(child)

    def visitClassDefinition(self, ctx: yaplParser.ClassDefinitionContext):
        temp_scope = SymbolTable()
        # self.parent_scopes[id(ctx)] = temp_scope
        name = ctx.getToken(44, 0).getText()
        ttype = ctx.getToken(1, 0).getText()
        self.sizes[name] = 0
        sym = Symbol(name, ttype, 4, temp_scope)
        self.parent_scopes[id(ctx)] = sym
        self.symbol_table.add_symbol(name, sym)
        return self.visitChildren(ctx)

    def visitMethodDef(self, ctx: yaplParser.MethodDefContext):
        # Create a scope for this method
        temp_scope = SymbolTable()
        #self.parent_scopes[id(ctx)] = temp_scope

        size = 4 # func definition size

        # Add attributes to the method scope
        for attr in ctx.formal():
            name = f'{attr.ID_VAR().getText()} = {self.get_t()}'
            ttype = attr.getToken(44, 0).getText()
            size_attr = self.calc_size(ttype)
            size += size_attr
            sym = Symbol(name, ttype, size_attr)
            temp_scope.add_symbol(name, sym)

        # Create a symbol from this method
        name = ctx.ID_VAR().getText()
        formals = tuple([f.TYPE_IDENTIFIER().getText() for f in ctx.formal()])
        ttype = ctx.TYPE_IDENTIFIER().getText()
        tab_type = MethodTyping(formals, ttype)
        sym = Symbol(name, tab_type, size, temp_scope)
        self.parent_scopes[id(ctx)] = sym

        # Add this symbol to its parent scope
        parent = ctx.parentCtx
        # Parent may not be in scope, as if it is a feature
        while isinstance(parent, yaplParser.FeatureDefinitionContext):
            parent = parent.parentCtx
        self.parent_scopes[id(parent)].refs.add_symbol(name, sym)
        self.parent_scopes[id(parent)].size += self.parent_scopes[id(ctx)].size
        sym.parent_name = parent.getToken(44, 0).getText()
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