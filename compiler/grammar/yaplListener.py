# Generated from compiler/grammar/yapl.g4 by ANTLR 4.13.0
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


    # Enter a parse tree produced by yaplParser#expr.
    def enterExpr(self, ctx:yaplParser.ExprContext):
        pass

    # Exit a parse tree produced by yaplParser#expr.
    def exitExpr(self, ctx:yaplParser.ExprContext):
        pass



del yaplParser