# Generated from compiler/grammar/yapl.g4 by ANTLR 4.13.0
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


    # Visit a parse tree produced by yaplParser#expr.
    def visitExpr(self, ctx:yaplParser.ExprContext):
        return self.visitChildren(ctx)



del yaplParser