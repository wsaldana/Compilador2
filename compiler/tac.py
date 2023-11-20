import sys
from typing_extensions import SupportsIndex
from antlr4 import InputStream, CommonTokenStream
from compiler.grammar.yaplLexer import yaplLexer
from compiler.grammar.yaplParser import yaplParser
from compiler.grammar.yaplVisitor import yaplVisitor


class Stack(list):
    def pop(self, __index: SupportsIndex = 0):
        return super().pop(__index)


class SymbolsVisitor(yaplVisitor):
    def __init__(self):
        self.t_count = 0
        self.l_count = 0
        self.var_stack = Stack()
        self.args = []

    def get_t(self, current=False):
        if not current:
            self.t_count += 1
        return f't{self.t_count}'

    def get_l(self):
        self.l_count += 1
        return f'L{self.l_count}'

    def visitSimple_var(self, ctx: yaplParser.Simple_varContext):
        val = ctx.getText()
        self.var_stack.append(val)

    def visitId_var(self, ctx: yaplParser.Id_varContext):
        parent = ctx.parentCtx
        if isinstance(
            parent,
            (
                yaplParser.ArithContext,
                yaplParser.BoolContext,
                yaplParser.Statement_atContext,
                yaplParser.ParamsContext
            )
        ):
            name = ctx.getText()
            self.var_stack.append(name)

    def visitStatement_at(self, ctx: yaplParser.Statement_atContext):
        args = ctx.expr()
        if not isinstance(args, list):
            args = [args]
        args = args[1:]

        if not isinstance(ctx.parentCtx, (yaplParser.ParamsContext, yaplParser.Statement_atContext)):
            priv_stack = Stack()
            original_stack = self.var_stack.copy()
            self.var_stack = priv_stack
        else:
            priv_stack = self.var_stack

        for arg in args:
            self.visit(arg)
            print(f"PUSH {priv_stack.pop()}")

        if not isinstance(ctx.parentCtx, (yaplParser.ParamsContext, yaplParser.Statement_atContext)):
            self.var_stack = Stack()
            self.var_stack.extend(original_stack)

        res = self.get_t()
        self.var_stack.append(res)
        name = ctx.ID_VAR()
        print(f"{res} = CALL {ctx.expr(0).getText()}.{name}")

    def visitParams(self, ctx: yaplParser.ParamsContext):
        args = ctx.expr()
        if not isinstance(args, list):
            args = [args]

        if not isinstance(ctx.parentCtx, (yaplParser.ParamsContext, yaplParser.Statement_atContext)):
            priv_stack = Stack()
            original_stack = self.var_stack.copy()
            self.var_stack = priv_stack
        else:
            priv_stack = self.var_stack

        for arg in args:
            self.visit(arg)
            print(f"PUSH {priv_stack.pop()}")

        if not isinstance(ctx.parentCtx, (yaplParser.ParamsContext, yaplParser.Statement_atContext)):
            self.var_stack = Stack()
            self.var_stack.extend(original_stack)


        res = self.get_t()
        self.var_stack.append(res)
        name = ctx.ID_VAR()
        print(f"{res} = CALL {name}")

    def visitArith(self, ctx: yaplParser.ArithContext):
        self.visitChildren(ctx)
        res = self.get_t()
        self.var_stack.append(res)
        #print("---- ", ctx.getText(), self.var_stack)
        left = self.var_stack.pop()
        right = self.var_stack.pop()
        op = ctx.children[1].getText()
        print(f"{res} = {left} {op} {right}")

    def visitBool(self, ctx: yaplParser.BoolContext):
        self.visitChildren(ctx)
        res = self.get_t()
        self.var_stack.append(res)
        #print("---- ", ctx.getText(), self.var_stack)
        left = self.var_stack.pop()
        right = self.var_stack.pop()
        op = ctx.children[1].getText()
        op = '==' if op == '=' else op
        print(f"{res} = {left} {op} {right}")

    def visitAttr(self, ctx: yaplParser.AttrContext):
        classname = ctx.parentCtx.parentCtx.TYPE_IDENTIFIER(0).getText()
        name = ctx.ID_VAR()
        if ctx.expr():
            if isinstance(ctx.expr(), yaplParser.Simple_varContext):
                print(f"{classname}.{name} = {ctx.expr().getText()}")
            else:
                self.visitChildren(ctx)
                print(f"{classname}.{name} = {self.var_stack.pop()}")
        else:
            print(f"{classname}.{name} = NONE")

    def visitStatement_let(self, ctx: yaplParser.Statement_letContext):
        self.visitChildren(ctx)
        vars = ctx.varTypescript()
        listed = [c.ID_VAR().getText() for c in vars]
        joined = ', '.join(listed)
        print(f"RETURN {joined}")

    def visitAsign_expr(self, ctx: yaplParser.Asign_exprContext):
        self.visitChildren(ctx)
        name = ctx.ID_VAR()
        value = self.var_stack.pop()
        print(f"{name} = {value}")

    def visitNew_type(self, ctx: yaplParser.New_typeContext):
        obj = self.get_t()
        self.var_stack.append(obj)
        print(f"{obj} = NEW {ctx.TYPE_IDENTIFIER()}")

    def visitStatement_if(self, ctx: yaplParser.Statement_ifContext):
        label1 = self.get_l()
        label2 = self.get_l()
        label3 = self.get_l()
        self.visitBool(ctx.children[1])
        condition = self.var_stack.pop()
        print(f"if {condition} goto {label1}")
        print(f"goto {label2}")
        print(f"{label1}:")
        #self.visitExpr(ctx.children[3])
        self.visit(ctx.children[3])
        print(f"goto {label3}")
        print(f"{label2}:")
        #self.visitExpr(ctx.children[5])
        self.visit(ctx.children[5])
        print(f"{label3}:")

    def visitExpr(self, ctx: yaplParser.ExprContext):
        return self.visitChildren(ctx)

    def visitProgram(self, ctx: yaplParser.ProgramContext):
        for child in ctx.getChildren():
            if isinstance(child, yaplParser.ClassDefinitionContext):
                self.visitClassDefinition(child)

    def visitClassDefinition(self, ctx: yaplParser.ClassDefinitionContext):
        print('CLASS ', ctx.TYPE_IDENTIFIER(0).getText())
        self.visitChildren(ctx)

    def visitMethodDef(self, ctx: yaplParser.MethodDefContext):
        self.l_count = 0
        self.t_count = 0
        classname = ctx.parentCtx.parentCtx.TYPE_IDENTIFIER(0).getText()
        name = ctx.ID_VAR()
        print(f'FUNC {classname}.{name}')
        self.visitChildren(ctx)
        print("END_FUNC\n")

    def get_symbol_table(self):
        return self.symbol_table


class Tee(object):
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)

    def flush(self):
        pass


def main():
    file = sys.argv[1]
    input_stream = InputStream(file)
    lexer = yaplLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = yaplParser(stream)

    f = open('logfile', 'w')
    backup = sys.stdout
    sys.stdout = Tee(sys.stdout, f)

    tree = parser.program()
    visitor = SymbolsVisitor()
    visitor.visit(tree)

    sys.stdout = backup


if __name__ == '__main__':
    main()
