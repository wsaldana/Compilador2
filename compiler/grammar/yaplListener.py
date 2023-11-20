# Generated from yapl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete listener for a parse tree produced by yaplParser.
class yaplListener(ParseTreeListener):

    # Enter a parse tree produced by yaplParser#program.
    def enterProgram(self, ctx:yaplParser.ProgramContext):
        pass

    # Exit a parse tree produced by yaplParser#program.
    def exitProgram(self, ctx:yaplParser.ProgramContext):
        pass


    # Enter a parse tree produced by yaplParser#formal.
    def enterFormal(self, ctx:yaplParser.FormalContext):
        pass

    # Exit a parse tree produced by yaplParser#formal.
    def exitFormal(self, ctx:yaplParser.FormalContext):
        pass


    # Enter a parse tree produced by yaplParser#attributeDeclaration.
    def enterAttributeDeclaration(self, ctx:yaplParser.AttributeDeclarationContext):
        pass

    # Exit a parse tree produced by yaplParser#attributeDeclaration.
    def exitAttributeDeclaration(self, ctx:yaplParser.AttributeDeclarationContext):
        pass


    # Enter a parse tree produced by yaplParser#classDefinition.
    def enterClassDefinition(self, ctx:yaplParser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by yaplParser#classDefinition.
    def exitClassDefinition(self, ctx:yaplParser.ClassDefinitionContext):
        pass


    # Enter a parse tree produced by yaplParser#featureDefinition.
    def enterFeatureDefinition(self, ctx:yaplParser.FeatureDefinitionContext):
        pass

    # Exit a parse tree produced by yaplParser#featureDefinition.
    def exitFeatureDefinition(self, ctx:yaplParser.FeatureDefinitionContext):
        pass


    # Enter a parse tree produced by yaplParser#methodDef.
    def enterMethodDef(self, ctx:yaplParser.MethodDefContext):
        pass

    # Exit a parse tree produced by yaplParser#methodDef.
    def exitMethodDef(self, ctx:yaplParser.MethodDefContext):
        pass


    # Enter a parse tree produced by yaplParser#attr.
    def enterAttr(self, ctx:yaplParser.AttrContext):
        pass

    # Exit a parse tree produced by yaplParser#attr.
    def exitAttr(self, ctx:yaplParser.AttrContext):
        pass


    # Enter a parse tree produced by yaplParser#arith.
    def enterArith(self, ctx:yaplParser.ArithContext):
        pass

    # Exit a parse tree produced by yaplParser#arith.
    def exitArith(self, ctx:yaplParser.ArithContext):
        pass


    # Enter a parse tree produced by yaplParser#new_type.
    def enterNew_type(self, ctx:yaplParser.New_typeContext):
        pass

    # Exit a parse tree produced by yaplParser#new_type.
    def exitNew_type(self, ctx:yaplParser.New_typeContext):
        pass


    # Enter a parse tree produced by yaplParser#statement_while.
    def enterStatement_while(self, ctx:yaplParser.Statement_whileContext):
        pass

    # Exit a parse tree produced by yaplParser#statement_while.
    def exitStatement_while(self, ctx:yaplParser.Statement_whileContext):
        pass


    # Enter a parse tree produced by yaplParser#statement_at.
    def enterStatement_at(self, ctx:yaplParser.Statement_atContext):
        pass

    # Exit a parse tree produced by yaplParser#statement_at.
    def exitStatement_at(self, ctx:yaplParser.Statement_atContext):
        pass


    # Enter a parse tree produced by yaplParser#negative_expr.
    def enterNegative_expr(self, ctx:yaplParser.Negative_exprContext):
        pass

    # Exit a parse tree produced by yaplParser#negative_expr.
    def exitNegative_expr(self, ctx:yaplParser.Negative_exprContext):
        pass


    # Enter a parse tree produced by yaplParser#int_var.
    def enterInt_var(self, ctx:yaplParser.Int_varContext):
        pass

    # Exit a parse tree produced by yaplParser#int_var.
    def exitInt_var(self, ctx:yaplParser.Int_varContext):
        pass


    # Enter a parse tree produced by yaplParser#statement_paren.
    def enterStatement_paren(self, ctx:yaplParser.Statement_parenContext):
        pass

    # Exit a parse tree produced by yaplParser#statement_paren.
    def exitStatement_paren(self, ctx:yaplParser.Statement_parenContext):
        pass


    # Enter a parse tree produced by yaplParser#bool_lt.
    def enterBool_lt(self, ctx:yaplParser.Bool_ltContext):
        pass

    # Exit a parse tree produced by yaplParser#bool_lt.
    def exitBool_lt(self, ctx:yaplParser.Bool_ltContext):
        pass


    # Enter a parse tree produced by yaplParser#statement_let.
    def enterStatement_let(self, ctx:yaplParser.Statement_letContext):
        pass

    # Exit a parse tree produced by yaplParser#statement_let.
    def exitStatement_let(self, ctx:yaplParser.Statement_letContext):
        pass


    # Enter a parse tree produced by yaplParser#void_expr.
    def enterVoid_expr(self, ctx:yaplParser.Void_exprContext):
        pass

    # Exit a parse tree produced by yaplParser#void_expr.
    def exitVoid_expr(self, ctx:yaplParser.Void_exprContext):
        pass


    # Enter a parse tree produced by yaplParser#str_var.
    def enterStr_var(self, ctx:yaplParser.Str_varContext):
        pass

    # Exit a parse tree produced by yaplParser#str_var.
    def exitStr_var(self, ctx:yaplParser.Str_varContext):
        pass


    # Enter a parse tree produced by yaplParser#params.
    def enterParams(self, ctx:yaplParser.ParamsContext):
        pass

    # Exit a parse tree produced by yaplParser#params.
    def exitParams(self, ctx:yaplParser.ParamsContext):
        pass


    # Enter a parse tree produced by yaplParser#statement_if.
    def enterStatement_if(self, ctx:yaplParser.Statement_ifContext):
        pass

    # Exit a parse tree produced by yaplParser#statement_if.
    def exitStatement_if(self, ctx:yaplParser.Statement_ifContext):
        pass


    # Enter a parse tree produced by yaplParser#not_expr.
    def enterNot_expr(self, ctx:yaplParser.Not_exprContext):
        pass

    # Exit a parse tree produced by yaplParser#not_expr.
    def exitNot_expr(self, ctx:yaplParser.Not_exprContext):
        pass


    # Enter a parse tree produced by yaplParser#equal.
    def enterEqual(self, ctx:yaplParser.EqualContext):
        pass

    # Exit a parse tree produced by yaplParser#equal.
    def exitEqual(self, ctx:yaplParser.EqualContext):
        pass


    # Enter a parse tree produced by yaplParser#bool_le.
    def enterBool_le(self, ctx:yaplParser.Bool_leContext):
        pass

    # Exit a parse tree produced by yaplParser#bool_le.
    def exitBool_le(self, ctx:yaplParser.Bool_leContext):
        pass


    # Enter a parse tree produced by yaplParser#asign_expr.
    def enterAsign_expr(self, ctx:yaplParser.Asign_exprContext):
        pass

    # Exit a parse tree produced by yaplParser#asign_expr.
    def exitAsign_expr(self, ctx:yaplParser.Asign_exprContext):
        pass


    # Enter a parse tree produced by yaplParser#id_var.
    def enterId_var(self, ctx:yaplParser.Id_varContext):
        pass

    # Exit a parse tree produced by yaplParser#id_var.
    def exitId_var(self, ctx:yaplParser.Id_varContext):
        pass


    # Enter a parse tree produced by yaplParser#bool_var.
    def enterBool_var(self, ctx:yaplParser.Bool_varContext):
        pass

    # Exit a parse tree produced by yaplParser#bool_var.
    def exitBool_var(self, ctx:yaplParser.Bool_varContext):
        pass


    # Enter a parse tree produced by yaplParser#statement_brace.
    def enterStatement_brace(self, ctx:yaplParser.Statement_braceContext):
        pass

    # Exit a parse tree produced by yaplParser#statement_brace.
    def exitStatement_brace(self, ctx:yaplParser.Statement_braceContext):
        pass



del yaplParser