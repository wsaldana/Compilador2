# Generated from yapl.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,190,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,
        2,1,2,1,2,1,2,1,2,3,2,33,8,2,1,3,1,3,1,3,1,3,3,3,39,8,3,1,3,1,3,
        1,3,1,3,5,3,45,8,3,10,3,12,3,48,9,3,1,3,1,3,1,4,1,4,3,4,54,8,4,1,
        5,1,5,1,5,1,5,1,5,5,5,61,8,5,10,5,12,5,64,9,5,5,5,66,8,5,10,5,12,
        5,69,9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,83,
        8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,5,7,104,8,7,10,7,12,7,107,9,7,5,7,109,8,7,10,7,12,
        7,112,9,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,4,7,133,8,7,11,7,12,7,134,1,7,1,7,1,7,1,7,
        1,7,1,7,5,7,143,8,7,10,7,12,7,146,9,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,3,7,155,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,166,8,7,1,
        7,1,7,1,7,1,7,1,7,1,7,5,7,174,8,7,10,7,12,7,177,9,7,5,7,179,8,7,
        10,7,12,7,182,9,7,1,7,5,7,185,8,7,10,7,12,7,188,9,7,1,7,0,1,14,8,
        0,2,4,6,8,10,12,14,0,3,2,0,41,42,45,45,1,0,27,30,1,0,31,35,211,0,
        19,1,0,0,0,2,23,1,0,0,0,4,27,1,0,0,0,6,34,1,0,0,0,8,53,1,0,0,0,10,
        55,1,0,0,0,12,77,1,0,0,0,14,154,1,0,0,0,16,17,3,6,3,0,17,18,5,20,
        0,0,18,20,1,0,0,0,19,16,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,
        1,0,0,0,22,1,1,0,0,0,23,24,5,43,0,0,24,25,5,18,0,0,25,26,5,44,0,
        0,26,3,1,0,0,0,27,28,5,43,0,0,28,29,5,18,0,0,29,32,5,44,0,0,30,31,
        5,37,0,0,31,33,3,14,7,0,32,30,1,0,0,0,32,33,1,0,0,0,33,5,1,0,0,0,
        34,35,5,1,0,0,35,38,5,44,0,0,36,37,5,11,0,0,37,39,5,44,0,0,38,36,
        1,0,0,0,38,39,1,0,0,0,39,40,1,0,0,0,40,46,5,23,0,0,41,42,3,8,4,0,
        42,43,5,20,0,0,43,45,1,0,0,0,44,41,1,0,0,0,45,48,1,0,0,0,46,44,1,
        0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,50,5,24,0,0,50,
        7,1,0,0,0,51,54,3,10,5,0,52,54,3,12,6,0,53,51,1,0,0,0,53,52,1,0,
        0,0,54,9,1,0,0,0,55,56,5,43,0,0,56,67,5,21,0,0,57,62,3,2,1,0,58,
        59,5,17,0,0,59,61,3,2,1,0,60,58,1,0,0,0,61,64,1,0,0,0,62,60,1,0,
        0,0,62,63,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,65,57,1,0,0,0,66,69,
        1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,
        70,71,5,22,0,0,71,72,5,18,0,0,72,73,5,44,0,0,73,74,5,23,0,0,74,75,
        3,14,7,0,75,76,5,24,0,0,76,11,1,0,0,0,77,78,5,43,0,0,78,79,5,18,
        0,0,79,82,5,44,0,0,80,81,5,37,0,0,81,83,3,14,7,0,82,80,1,0,0,0,82,
        83,1,0,0,0,83,13,1,0,0,0,84,85,6,7,-1,0,85,86,5,13,0,0,86,155,5,
        44,0,0,87,88,5,25,0,0,88,155,3,14,7,13,89,90,5,12,0,0,90,155,3,14,
        7,12,91,92,5,14,0,0,92,155,3,14,7,11,93,155,5,43,0,0,94,155,7,0,
        0,0,95,96,5,43,0,0,96,97,5,37,0,0,97,155,3,14,7,8,98,99,5,43,0,0,
        99,110,5,21,0,0,100,105,3,14,7,0,101,102,5,17,0,0,102,104,3,14,7,
        0,103,101,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,
        0,106,109,1,0,0,0,107,105,1,0,0,0,108,100,1,0,0,0,109,112,1,0,0,
        0,110,108,1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,110,1,0,0,
        0,113,155,5,22,0,0,114,115,5,7,0,0,115,116,3,14,7,0,116,117,5,4,
        0,0,117,118,3,14,7,0,118,119,5,9,0,0,119,120,3,14,7,0,120,121,5,
        8,0,0,121,155,1,0,0,0,122,123,5,3,0,0,123,124,3,14,7,0,124,125,5,
        5,0,0,125,126,3,14,7,0,126,127,5,6,0,0,127,155,1,0,0,0,128,132,5,
        23,0,0,129,130,3,14,7,0,130,131,5,20,0,0,131,133,1,0,0,0,132,129,
        1,0,0,0,133,134,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,136,
        1,0,0,0,136,137,5,24,0,0,137,155,1,0,0,0,138,139,5,2,0,0,139,144,
        3,4,2,0,140,141,5,17,0,0,141,143,3,4,2,0,142,140,1,0,0,0,143,146,
        1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,147,1,0,0,0,146,144,
        1,0,0,0,147,148,5,10,0,0,148,149,3,14,7,3,149,155,1,0,0,0,150,151,
        5,21,0,0,151,152,3,14,7,0,152,153,5,22,0,0,153,155,1,0,0,0,154,84,
        1,0,0,0,154,87,1,0,0,0,154,89,1,0,0,0,154,91,1,0,0,0,154,93,1,0,
        0,0,154,94,1,0,0,0,154,95,1,0,0,0,154,98,1,0,0,0,154,114,1,0,0,0,
        154,122,1,0,0,0,154,128,1,0,0,0,154,138,1,0,0,0,154,150,1,0,0,0,
        155,186,1,0,0,0,156,157,10,16,0,0,157,158,7,1,0,0,158,185,3,14,7,
        17,159,160,10,15,0,0,160,161,7,2,0,0,161,185,3,14,7,16,162,165,10,
        1,0,0,163,164,5,26,0,0,164,166,5,44,0,0,165,163,1,0,0,0,165,166,
        1,0,0,0,166,167,1,0,0,0,167,168,5,19,0,0,168,169,5,43,0,0,169,180,
        5,21,0,0,170,175,3,14,7,0,171,172,5,17,0,0,172,174,3,14,7,0,173,
        171,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,
        179,1,0,0,0,177,175,1,0,0,0,178,170,1,0,0,0,179,182,1,0,0,0,180,
        178,1,0,0,0,180,181,1,0,0,0,181,183,1,0,0,0,182,180,1,0,0,0,183,
        185,5,22,0,0,184,156,1,0,0,0,184,159,1,0,0,0,184,162,1,0,0,0,185,
        188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,15,1,0,0,0,188,186,
        1,0,0,0,18,21,32,38,46,53,62,67,82,105,110,134,144,154,165,175,180,
        184,186
    ]

class yaplParser ( Parser ):

    grammarFileName = "yapl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','", "':'", "'.'", "';'", "'('", "')'", 
                     "'{'", "'}'", "'~'", "'@'", "'+'", "'-'", "'*'", "'/'", 
                     "'<'", "'<='", "'>'", "'>='", "'='", "'=>'", "'<-'", 
                     "'ERROR'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "LET", "WHILE", "THEN", "LOOP", 
                      "POOL", "IF", "FI", "ELSE", "IN", "INHERITS", "ISVOID", 
                      "NEW", "NOT", "WS", "NEWLINE", "COMMA", "COLON", "PERIOD", 
                      "SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "NEGATIVE", "AT", "PLUS", "MINUS", "MULT", "DIV", 
                      "LESS_THAN", "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", 
                      "EQUAL", "FAT_ARROW", "ASSIGN", "ERROR", "COMMENT_BLOCK", 
                      "COMMENT_LINE", "INT_VAR", "BOOL_VAR", "ID_VAR", "TYPE_IDENTIFIER", 
                      "STR_VAR" ]

    RULE_program = 0
    RULE_formal = 1
    RULE_varTypescript = 2
    RULE_classDefinition = 3
    RULE_featureDefinition = 4
    RULE_methodDefinition = 5
    RULE_attributeDefinition = 6
    RULE_expr = 7

    ruleNames =  [ "program", "formal", "varTypescript", "classDefinition", 
                   "featureDefinition", "methodDefinition", "attributeDefinition", 
                   "expr" ]

    EOF = Token.EOF
    CLASS=1
    LET=2
    WHILE=3
    THEN=4
    LOOP=5
    POOL=6
    IF=7
    FI=8
    ELSE=9
    IN=10
    INHERITS=11
    ISVOID=12
    NEW=13
    NOT=14
    WS=15
    NEWLINE=16
    COMMA=17
    COLON=18
    PERIOD=19
    SEMICOLON=20
    LPAREN=21
    RPAREN=22
    LBRACE=23
    RBRACE=24
    NEGATIVE=25
    AT=26
    PLUS=27
    MINUS=28
    MULT=29
    DIV=30
    LESS_THAN=31
    LESS_EQUAL=32
    GREATER_THAN=33
    GREATER_EQUAL=34
    EQUAL=35
    FAT_ARROW=36
    ASSIGN=37
    ERROR=38
    COMMENT_BLOCK=39
    COMMENT_LINE=40
    INT_VAR=41
    BOOL_VAR=42
    ID_VAR=43
    TYPE_IDENTIFIER=44
    STR_VAR=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ClassDefinitionContext)
            else:
                return self.getTypedRuleContext(yaplParser.ClassDefinitionContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.SEMICOLON)
            else:
                return self.getToken(yaplParser.SEMICOLON, i)

        def getRuleIndex(self):
            return yaplParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = yaplParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.classDefinition()
                self.state = 17
                self.match(yaplParser.SEMICOLON)
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return yaplParser.RULE_formal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArgsContext(FormalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.FormalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def COLON(self):
            return self.getToken(yaplParser.COLON, 0)
        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)



    def formal(self):

        localctx = yaplParser.FormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_formal)
        try:
            localctx = yaplParser.ArgsContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(yaplParser.ID_VAR)
            self.state = 24
            self.match(yaplParser.COLON)
            self.state = 25
            self.match(yaplParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarTypescriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return yaplParser.RULE_varTypescript

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AttributeDeclarationContext(VarTypescriptContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.VarTypescriptContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def COLON(self):
            return self.getToken(yaplParser.COLON, 0)
        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)
        def ASSIGN(self):
            return self.getToken(yaplParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeDeclaration" ):
                listener.enterAttributeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeDeclaration" ):
                listener.exitAttributeDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeDeclaration" ):
                return visitor.visitAttributeDeclaration(self)
            else:
                return visitor.visitChildren(self)



    def varTypescript(self):

        localctx = yaplParser.VarTypescriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varTypescript)
        self._la = 0 # Token type
        try:
            localctx = yaplParser.AttributeDeclarationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(yaplParser.ID_VAR)
            self.state = 28
            self.match(yaplParser.COLON)
            self.state = 29
            self.match(yaplParser.TYPE_IDENTIFIER)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 30
                self.match(yaplParser.ASSIGN)
                self.state = 31
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(yaplParser.CLASS, 0)

        def TYPE_IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.TYPE_IDENTIFIER)
            else:
                return self.getToken(yaplParser.TYPE_IDENTIFIER, i)

        def LBRACE(self):
            return self.getToken(yaplParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(yaplParser.RBRACE, 0)

        def INHERITS(self):
            return self.getToken(yaplParser.INHERITS, 0)

        def featureDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.FeatureDefinitionContext)
            else:
                return self.getTypedRuleContext(yaplParser.FeatureDefinitionContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.SEMICOLON)
            else:
                return self.getToken(yaplParser.SEMICOLON, i)

        def getRuleIndex(self):
            return yaplParser.RULE_classDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDefinition" ):
                listener.enterClassDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDefinition" ):
                listener.exitClassDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDefinition" ):
                return visitor.visitClassDefinition(self)
            else:
                return visitor.visitChildren(self)




    def classDefinition(self):

        localctx = yaplParser.ClassDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(yaplParser.CLASS)
            self.state = 35
            self.match(yaplParser.TYPE_IDENTIFIER)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 36
                self.match(yaplParser.INHERITS)
                self.state = 37
                self.match(yaplParser.TYPE_IDENTIFIER)


            self.state = 40
            self.match(yaplParser.LBRACE)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 41
                self.featureDefinition()
                self.state = 42
                self.match(yaplParser.SEMICOLON)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(yaplParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDefinition(self):
            return self.getTypedRuleContext(yaplParser.MethodDefinitionContext,0)


        def attributeDefinition(self):
            return self.getTypedRuleContext(yaplParser.AttributeDefinitionContext,0)


        def getRuleIndex(self):
            return yaplParser.RULE_featureDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeatureDefinition" ):
                listener.enterFeatureDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeatureDefinition" ):
                listener.exitFeatureDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeatureDefinition" ):
                return visitor.visitFeatureDefinition(self)
            else:
                return visitor.visitChildren(self)




    def featureDefinition(self):

        localctx = yaplParser.FeatureDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_featureDefinition)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.methodDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.attributeDefinition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return yaplParser.RULE_methodDefinition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MethodDefContext(MethodDefinitionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.MethodDefinitionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def LPAREN(self):
            return self.getToken(yaplParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(yaplParser.RPAREN, 0)
        def COLON(self):
            return self.getToken(yaplParser.COLON, 0)
        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)
        def LBRACE(self):
            return self.getToken(yaplParser.LBRACE, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)

        def RBRACE(self):
            return self.getToken(yaplParser.RBRACE, 0)
        def formal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.FormalContext)
            else:
                return self.getTypedRuleContext(yaplParser.FormalContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.COMMA)
            else:
                return self.getToken(yaplParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDef" ):
                listener.enterMethodDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDef" ):
                listener.exitMethodDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDef" ):
                return visitor.visitMethodDef(self)
            else:
                return visitor.visitChildren(self)



    def methodDefinition(self):

        localctx = yaplParser.MethodDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_methodDefinition)
        self._la = 0 # Token type
        try:
            localctx = yaplParser.MethodDefContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(yaplParser.ID_VAR)
            self.state = 56
            self.match(yaplParser.LPAREN)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 57
                self.formal()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 58
                    self.match(yaplParser.COMMA)
                    self.state = 59
                    self.formal()
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(yaplParser.RPAREN)
            self.state = 71
            self.match(yaplParser.COLON)
            self.state = 72
            self.match(yaplParser.TYPE_IDENTIFIER)
            self.state = 73
            self.match(yaplParser.LBRACE)
            self.state = 74
            self.expr(0)
            self.state = 75
            self.match(yaplParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return yaplParser.RULE_attributeDefinition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AttrContext(AttributeDefinitionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.AttributeDefinitionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def COLON(self):
            return self.getToken(yaplParser.COLON, 0)
        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)
        def ASSIGN(self):
            return self.getToken(yaplParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr" ):
                listener.enterAttr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr" ):
                listener.exitAttr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr" ):
                return visitor.visitAttr(self)
            else:
                return visitor.visitChildren(self)



    def attributeDefinition(self):

        localctx = yaplParser.AttributeDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributeDefinition)
        self._la = 0 # Token type
        try:
            localctx = yaplParser.AttrContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(yaplParser.ID_VAR)
            self.state = 78
            self.match(yaplParser.COLON)
            self.state = 79
            self.match(yaplParser.TYPE_IDENTIFIER)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 80
                self.match(yaplParser.ASSIGN)
                self.state = 81
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return yaplParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ArithContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def MULT(self):
            return self.getToken(yaplParser.MULT, 0)
        def DIV(self):
            return self.getToken(yaplParser.DIV, 0)
        def PLUS(self):
            return self.getToken(yaplParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(yaplParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith" ):
                listener.enterArith(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith" ):
                listener.exitArith(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith" ):
                return visitor.visitArith(self)
            else:
                return visitor.visitChildren(self)


    class New_typeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(yaplParser.NEW, 0)
        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNew_type" ):
                listener.enterNew_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNew_type" ):
                listener.exitNew_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew_type" ):
                return visitor.visitNew_type(self)
            else:
                return visitor.visitChildren(self)


    class Statement_whileContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(yaplParser.WHILE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def LOOP(self):
            return self.getToken(yaplParser.LOOP, 0)
        def POOL(self):
            return self.getToken(yaplParser.POOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_while" ):
                listener.enterStatement_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_while" ):
                listener.exitStatement_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_while" ):
                return visitor.visitStatement_while(self)
            else:
                return visitor.visitChildren(self)


    class Statement_atContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def PERIOD(self):
            return self.getToken(yaplParser.PERIOD, 0)
        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def LPAREN(self):
            return self.getToken(yaplParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(yaplParser.RPAREN, 0)
        def AT(self):
            return self.getToken(yaplParser.AT, 0)
        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.COMMA)
            else:
                return self.getToken(yaplParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_at" ):
                listener.enterStatement_at(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_at" ):
                listener.exitStatement_at(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_at" ):
                return visitor.visitStatement_at(self)
            else:
                return visitor.visitChildren(self)


    class Negative_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEGATIVE(self):
            return self.getToken(yaplParser.NEGATIVE, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegative_expr" ):
                listener.enterNegative_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegative_expr" ):
                listener.exitNegative_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegative_expr" ):
                return visitor.visitNegative_expr(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def LESS_THAN(self):
            return self.getToken(yaplParser.LESS_THAN, 0)
        def LESS_EQUAL(self):
            return self.getToken(yaplParser.LESS_EQUAL, 0)
        def GREATER_THAN(self):
            return self.getToken(yaplParser.GREATER_THAN, 0)
        def GREATER_EQUAL(self):
            return self.getToken(yaplParser.GREATER_EQUAL, 0)
        def EQUAL(self):
            return self.getToken(yaplParser.EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class Statement_parenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(yaplParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(yaplParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_paren" ):
                listener.enterStatement_paren(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_paren" ):
                listener.exitStatement_paren(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_paren" ):
                return visitor.visitStatement_paren(self)
            else:
                return visitor.visitChildren(self)


    class Statement_letContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(yaplParser.LET, 0)
        def varTypescript(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.VarTypescriptContext)
            else:
                return self.getTypedRuleContext(yaplParser.VarTypescriptContext,i)

        def IN(self):
            return self.getToken(yaplParser.IN, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.COMMA)
            else:
                return self.getToken(yaplParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_let" ):
                listener.enterStatement_let(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_let" ):
                listener.exitStatement_let(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_let" ):
                return visitor.visitStatement_let(self)
            else:
                return visitor.visitChildren(self)


    class Void_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ISVOID(self):
            return self.getToken(yaplParser.ISVOID, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoid_expr" ):
                listener.enterVoid_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoid_expr" ):
                listener.exitVoid_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoid_expr" ):
                return visitor.visitVoid_expr(self)
            else:
                return visitor.visitChildren(self)


    class Simple_varContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_VAR(self):
            return self.getToken(yaplParser.INT_VAR, 0)
        def STR_VAR(self):
            return self.getToken(yaplParser.STR_VAR, 0)
        def BOOL_VAR(self):
            return self.getToken(yaplParser.BOOL_VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_var" ):
                listener.enterSimple_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_var" ):
                listener.exitSimple_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_var" ):
                return visitor.visitSimple_var(self)
            else:
                return visitor.visitChildren(self)


    class ParamsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def LPAREN(self):
            return self.getToken(yaplParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(yaplParser.RPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.COMMA)
            else:
                return self.getToken(yaplParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)


    class Statement_ifContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(yaplParser.IF, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def THEN(self):
            return self.getToken(yaplParser.THEN, 0)
        def ELSE(self):
            return self.getToken(yaplParser.ELSE, 0)
        def FI(self):
            return self.getToken(yaplParser.FI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_if" ):
                listener.enterStatement_if(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_if" ):
                listener.exitStatement_if(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_if" ):
                return visitor.visitStatement_if(self)
            else:
                return visitor.visitChildren(self)


    class Not_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(yaplParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_expr" ):
                listener.enterNot_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_expr" ):
                listener.exitNot_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_expr" ):
                return visitor.visitNot_expr(self)
            else:
                return visitor.visitChildren(self)


    class Asign_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def ASSIGN(self):
            return self.getToken(yaplParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsign_expr" ):
                listener.enterAsign_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsign_expr" ):
                listener.exitAsign_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsign_expr" ):
                return visitor.visitAsign_expr(self)
            else:
                return visitor.visitChildren(self)


    class Id_varContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_var" ):
                listener.enterId_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_var" ):
                listener.exitId_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_var" ):
                return visitor.visitId_var(self)
            else:
                return visitor.visitChildren(self)


    class Statement_braceContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(yaplParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(yaplParser.RBRACE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.SEMICOLON)
            else:
                return self.getToken(yaplParser.SEMICOLON, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_brace" ):
                listener.enterStatement_brace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_brace" ):
                listener.exitStatement_brace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_brace" ):
                return visitor.visitStatement_brace(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = yaplParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = yaplParser.New_typeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 85
                self.match(yaplParser.NEW)
                self.state = 86
                self.match(yaplParser.TYPE_IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = yaplParser.Negative_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 87
                self.match(yaplParser.NEGATIVE)
                self.state = 88
                self.expr(13)
                pass

            elif la_ == 3:
                localctx = yaplParser.Void_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                self.match(yaplParser.ISVOID)
                self.state = 90
                self.expr(12)
                pass

            elif la_ == 4:
                localctx = yaplParser.Not_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 91
                self.match(yaplParser.NOT)
                self.state = 92
                self.expr(11)
                pass

            elif la_ == 5:
                localctx = yaplParser.Id_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                self.match(yaplParser.ID_VAR)
                pass

            elif la_ == 6:
                localctx = yaplParser.Simple_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 94
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 41781441855488) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 7:
                localctx = yaplParser.Asign_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 95
                self.match(yaplParser.ID_VAR)
                self.state = 96
                self.match(yaplParser.ASSIGN)
                self.state = 97
                self.expr(8)
                pass

            elif la_ == 8:
                localctx = yaplParser.ParamsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                self.match(yaplParser.ID_VAR)
                self.state = 99
                self.match(yaplParser.LPAREN)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 50577578946700) != 0):
                    self.state = 100
                    self.expr(0)
                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==17:
                        self.state = 101
                        self.match(yaplParser.COMMA)
                        self.state = 102
                        self.expr(0)
                        self.state = 107
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 112
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 113
                self.match(yaplParser.RPAREN)
                pass

            elif la_ == 9:
                localctx = yaplParser.Statement_ifContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114
                self.match(yaplParser.IF)
                self.state = 115
                self.expr(0)
                self.state = 116
                self.match(yaplParser.THEN)
                self.state = 117
                self.expr(0)
                self.state = 118
                self.match(yaplParser.ELSE)
                self.state = 119
                self.expr(0)
                self.state = 120
                self.match(yaplParser.FI)
                pass

            elif la_ == 10:
                localctx = yaplParser.Statement_whileContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.match(yaplParser.WHILE)
                self.state = 123
                self.expr(0)
                self.state = 124
                self.match(yaplParser.LOOP)
                self.state = 125
                self.expr(0)
                self.state = 126
                self.match(yaplParser.POOL)
                pass

            elif la_ == 11:
                localctx = yaplParser.Statement_braceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 128
                self.match(yaplParser.LBRACE)
                self.state = 132 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 129
                    self.expr(0)
                    self.state = 130
                    self.match(yaplParser.SEMICOLON)
                    self.state = 134 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 50577578946700) != 0)):
                        break

                self.state = 136
                self.match(yaplParser.RBRACE)
                pass

            elif la_ == 12:
                localctx = yaplParser.Statement_letContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.match(yaplParser.LET)
                self.state = 139
                self.varTypescript()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 140
                    self.match(yaplParser.COMMA)
                    self.state = 141
                    self.varTypescript()
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 147
                self.match(yaplParser.IN)
                self.state = 148
                self.expr(3)
                pass

            elif la_ == 13:
                localctx = yaplParser.Statement_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.match(yaplParser.LPAREN)
                self.state = 151
                self.expr(0)
                self.state = 152
                self.match(yaplParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 184
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = yaplParser.ArithContext(self, yaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 156
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 157
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2013265920) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 158
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = yaplParser.BoolContext(self, yaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 159
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 160
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66571993088) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 161
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = yaplParser.Statement_atContext(self, yaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 165
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==26:
                            self.state = 163
                            self.match(yaplParser.AT)
                            self.state = 164
                            self.match(yaplParser.TYPE_IDENTIFIER)


                        self.state = 167
                        self.match(yaplParser.PERIOD)
                        self.state = 168
                        self.match(yaplParser.ID_VAR)
                        self.state = 169
                        self.match(yaplParser.LPAREN)
                        self.state = 180
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & 50577578946700) != 0):
                            self.state = 170
                            self.expr(0)
                            self.state = 175
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==17:
                                self.state = 171
                                self.match(yaplParser.COMMA)
                                self.state = 172
                                self.expr(0)
                                self.state = 177
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)

                            self.state = 182
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 183
                        self.match(yaplParser.RPAREN)
                        pass

             
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




