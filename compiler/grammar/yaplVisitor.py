# Generated from yapl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete generic visitor for a parse tree produced by yaplParser.

class yaplVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by yaplParser#program.
    def visitProgram(self, ctx:yaplParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#formal.
    def visitFormal(self, ctx:yaplParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#attributeDeclaration.
    def visitAttributeDeclaration(self, ctx:yaplParser.AttributeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#classDefinition.
    def visitClassDefinition(self, ctx:yaplParser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#featureDefinition.
    def visitFeatureDefinition(self, ctx:yaplParser.FeatureDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#methodDef.
    def visitMethodDef(self, ctx:yaplParser.MethodDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#attr.
    def visitAttr(self, ctx:yaplParser.AttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#arith.
    def visitArith(self, ctx:yaplParser.ArithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#new_type.
    def visitNew_type(self, ctx:yaplParser.New_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#statement_while.
    def visitStatement_while(self, ctx:yaplParser.Statement_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#statement_at.
    def visitStatement_at(self, ctx:yaplParser.Statement_atContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#negative_expr.
    def visitNegative_expr(self, ctx:yaplParser.Negative_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#int_var.
    def visitInt_var(self, ctx:yaplParser.Int_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#statement_paren.
    def visitStatement_paren(self, ctx:yaplParser.Statement_parenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#bool_lt.
    def visitBool_lt(self, ctx:yaplParser.Bool_ltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#statement_let.
    def visitStatement_let(self, ctx:yaplParser.Statement_letContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#void_expr.
    def visitVoid_expr(self, ctx:yaplParser.Void_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#str_var.
    def visitStr_var(self, ctx:yaplParser.Str_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#params.
    def visitParams(self, ctx:yaplParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#statement_if.
    def visitStatement_if(self, ctx:yaplParser.Statement_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#not_expr.
    def visitNot_expr(self, ctx:yaplParser.Not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#equal.
    def visitEqual(self, ctx:yaplParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#bool_le.
    def visitBool_le(self, ctx:yaplParser.Bool_leContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#asign_expr.
    def visitAsign_expr(self, ctx:yaplParser.Asign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#id_var.
    def visitId_var(self, ctx:yaplParser.Id_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#bool_var.
    def visitBool_var(self, ctx:yaplParser.Bool_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#statement_brace.
    def visitStatement_brace(self, ctx:yaplParser.Statement_braceContext):
        return self.visitChildren(ctx)



del yaplParser