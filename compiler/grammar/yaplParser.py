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
        4,1,46,208,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,
        2,1,2,1,2,1,2,1,2,3,2,33,8,2,1,3,1,3,1,3,1,3,3,3,39,8,3,1,3,1,3,
        1,3,1,3,5,3,45,8,3,10,3,12,3,48,9,3,1,3,1,3,1,4,1,4,3,4,54,8,4,1,
        5,1,5,1,5,1,5,1,5,5,5,61,8,5,10,5,12,5,64,9,5,5,5,66,8,5,10,5,12,
        5,69,9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,83,
        8,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,91,8,7,10,7,12,7,94,9,7,5,7,96,8,
        7,10,7,12,7,99,9,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,4,7,120,8,7,11,7,12,7,121,1,7,1,7,
        1,7,1,7,1,7,1,7,5,7,130,8,7,10,7,12,7,133,9,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,3,7,158,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,184,8,
        7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,192,8,7,10,7,12,7,195,9,7,5,7,197,
        8,7,10,7,12,7,200,9,7,1,7,5,7,203,8,7,10,7,12,7,206,9,7,1,7,0,1,
        14,8,0,2,4,6,8,10,12,14,0,0,237,0,19,1,0,0,0,2,23,1,0,0,0,4,27,1,
        0,0,0,6,34,1,0,0,0,8,53,1,0,0,0,10,55,1,0,0,0,12,77,1,0,0,0,14,157,
        1,0,0,0,16,17,3,6,3,0,17,18,5,20,0,0,18,20,1,0,0,0,19,16,1,0,0,0,
        20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,24,5,44,
        0,0,24,25,5,18,0,0,25,26,5,45,0,0,26,3,1,0,0,0,27,28,5,44,0,0,28,
        29,5,18,0,0,29,32,5,45,0,0,30,31,5,39,0,0,31,33,3,14,7,0,32,30,1,
        0,0,0,32,33,1,0,0,0,33,5,1,0,0,0,34,35,5,1,0,0,35,38,5,45,0,0,36,
        37,5,11,0,0,37,39,5,45,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,40,1,0,
        0,0,40,46,5,23,0,0,41,42,3,8,4,0,42,43,5,20,0,0,43,45,1,0,0,0,44,
        41,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,
        0,48,46,1,0,0,0,49,50,5,24,0,0,50,7,1,0,0,0,51,54,3,10,5,0,52,54,
        3,12,6,0,53,51,1,0,0,0,53,52,1,0,0,0,54,9,1,0,0,0,55,56,5,44,0,0,
        56,67,5,21,0,0,57,62,3,2,1,0,58,59,5,17,0,0,59,61,3,2,1,0,60,58,
        1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,66,1,0,0,0,
        64,62,1,0,0,0,65,57,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,
        0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,71,5,22,0,0,71,72,5,18,0,0,
        72,73,5,45,0,0,73,74,5,23,0,0,74,75,3,14,7,0,75,76,5,24,0,0,76,11,
        1,0,0,0,77,78,5,44,0,0,78,79,5,18,0,0,79,82,5,45,0,0,80,81,5,39,
        0,0,81,83,3,14,7,0,82,80,1,0,0,0,82,83,1,0,0,0,83,13,1,0,0,0,84,
        85,6,7,-1,0,85,86,5,44,0,0,86,97,5,21,0,0,87,92,3,14,7,0,88,89,5,
        17,0,0,89,91,3,14,7,0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,
        92,93,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,95,87,1,0,0,0,96,99,1,
        0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,
        158,5,22,0,0,101,102,5,7,0,0,102,103,3,14,7,0,103,104,5,4,0,0,104,
        105,3,14,7,0,105,106,5,9,0,0,106,107,3,14,7,0,107,108,5,8,0,0,108,
        158,1,0,0,0,109,110,5,3,0,0,110,111,3,14,7,0,111,112,5,5,0,0,112,
        113,3,14,7,0,113,114,5,6,0,0,114,158,1,0,0,0,115,119,5,23,0,0,116,
        117,3,14,7,0,117,118,5,20,0,0,118,120,1,0,0,0,119,116,1,0,0,0,120,
        121,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,123,1,0,0,0,123,
        124,5,24,0,0,124,158,1,0,0,0,125,126,5,2,0,0,126,131,3,4,2,0,127,
        128,5,17,0,0,128,130,3,4,2,0,129,127,1,0,0,0,130,133,1,0,0,0,131,
        129,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,
        135,5,10,0,0,135,136,3,14,7,19,136,158,1,0,0,0,137,138,5,13,0,0,
        138,158,5,45,0,0,139,140,5,25,0,0,140,158,3,14,7,17,141,142,5,12,
        0,0,142,158,3,14,7,16,143,144,5,14,0,0,144,158,3,14,7,8,145,146,
        5,21,0,0,146,147,3,14,7,0,147,148,5,22,0,0,148,158,1,0,0,0,149,158,
        5,44,0,0,150,158,5,43,0,0,151,158,5,46,0,0,152,158,5,27,0,0,153,
        158,5,28,0,0,154,155,5,44,0,0,155,156,5,39,0,0,156,158,3,14,7,1,
        157,84,1,0,0,0,157,101,1,0,0,0,157,109,1,0,0,0,157,115,1,0,0,0,157,
        125,1,0,0,0,157,137,1,0,0,0,157,139,1,0,0,0,157,141,1,0,0,0,157,
        143,1,0,0,0,157,145,1,0,0,0,157,149,1,0,0,0,157,150,1,0,0,0,157,
        151,1,0,0,0,157,152,1,0,0,0,157,153,1,0,0,0,157,154,1,0,0,0,158,
        204,1,0,0,0,159,160,10,15,0,0,160,161,5,31,0,0,161,203,3,14,7,16,
        162,163,10,14,0,0,163,164,5,32,0,0,164,203,3,14,7,15,165,166,10,
        13,0,0,166,167,5,29,0,0,167,203,3,14,7,14,168,169,10,12,0,0,169,
        170,5,30,0,0,170,203,3,14,7,13,171,172,10,11,0,0,172,173,5,34,0,
        0,173,203,3,14,7,12,174,175,10,10,0,0,175,176,5,33,0,0,176,203,3,
        14,7,11,177,178,10,9,0,0,178,179,5,37,0,0,179,203,3,14,7,10,180,
        183,10,23,0,0,181,182,5,26,0,0,182,184,5,45,0,0,183,181,1,0,0,0,
        183,184,1,0,0,0,184,185,1,0,0,0,185,186,5,19,0,0,186,187,5,44,0,
        0,187,198,5,21,0,0,188,193,3,14,7,0,189,190,5,17,0,0,190,192,3,14,
        7,0,191,189,1,0,0,0,192,195,1,0,0,0,193,191,1,0,0,0,193,194,1,0,
        0,0,194,197,1,0,0,0,195,193,1,0,0,0,196,188,1,0,0,0,197,200,1,0,
        0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,201,1,0,0,0,200,198,1,0,
        0,0,201,203,5,22,0,0,202,159,1,0,0,0,202,162,1,0,0,0,202,165,1,0,
        0,0,202,168,1,0,0,0,202,171,1,0,0,0,202,174,1,0,0,0,202,177,1,0,
        0,0,202,180,1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,204,205,1,0,
        0,0,205,15,1,0,0,0,206,204,1,0,0,0,18,21,32,38,46,53,62,67,82,92,
        97,121,131,157,183,193,198,202,204
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
                     "'{'", "'}'", "'~'", "'@'", "'true'", "'false'", "'+'", 
                     "'-'", "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", 
                     "'='", "'=>'", "'<-'", "'ERROR'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "LET", "WHILE", "THEN", "LOOP", 
                      "POOL", "IF", "FI", "ELSE", "IN", "INHERITS", "ISVOID", 
                      "NEW", "NOT", "WS", "NEWLINE", "COMMA", "COLON", "PERIOD", 
                      "SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "NEGATIVE", "AT", "TRUE", "FALSE", "PLUS", "MINUS", 
                      "MULT", "DIV", "LESS_THAN", "LESS_EQUAL", "GREATER_THAN", 
                      "GREATER_EQUAL", "EQUAL", "FAT_ARROW", "ASSIGN", "ERROR", 
                      "COMMENT_BLOCK", "COMMENT_LINE", "INT_VAR", "ID_VAR", 
                      "TYPE_IDENTIFIER", "STR_VAR" ]

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
    TRUE=27
    FALSE=28
    PLUS=29
    MINUS=30
    MULT=31
    DIV=32
    LESS_THAN=33
    LESS_EQUAL=34
    GREATER_THAN=35
    GREATER_EQUAL=36
    EQUAL=37
    FAT_ARROW=38
    ASSIGN=39
    ERROR=40
    COMMENT_BLOCK=41
    COMMENT_LINE=42
    INT_VAR=43
    ID_VAR=44
    TYPE_IDENTIFIER=45
    STR_VAR=46

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

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)

        def COLON(self):
            return self.getToken(yaplParser.COLON, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return yaplParser.RULE_formal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal" ):
                listener.enterFormal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal" ):
                listener.exitFormal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal" ):
                return visitor.visitFormal(self)
            else:
                return visitor.visitChildren(self)




    def formal(self):

        localctx = yaplParser.FormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_formal)
        try:
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
            if _la==39:
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
            while _la==44:
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
            while _la==44:
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
            if _la==39:
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

        def IF(self):
            return self.getToken(yaplParser.IF, 0)

        def THEN(self):
            return self.getToken(yaplParser.THEN, 0)

        def ELSE(self):
            return self.getToken(yaplParser.ELSE, 0)

        def FI(self):
            return self.getToken(yaplParser.FI, 0)

        def WHILE(self):
            return self.getToken(yaplParser.WHILE, 0)

        def LOOP(self):
            return self.getToken(yaplParser.LOOP, 0)

        def POOL(self):
            return self.getToken(yaplParser.POOL, 0)

        def LBRACE(self):
            return self.getToken(yaplParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(yaplParser.RBRACE, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.SEMICOLON)
            else:
                return self.getToken(yaplParser.SEMICOLON, i)

        def LET(self):
            return self.getToken(yaplParser.LET, 0)

        def varTypescript(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.VarTypescriptContext)
            else:
                return self.getTypedRuleContext(yaplParser.VarTypescriptContext,i)


        def IN(self):
            return self.getToken(yaplParser.IN, 0)

        def NEW(self):
            return self.getToken(yaplParser.NEW, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)

        def NEGATIVE(self):
            return self.getToken(yaplParser.NEGATIVE, 0)

        def ISVOID(self):
            return self.getToken(yaplParser.ISVOID, 0)

        def NOT(self):
            return self.getToken(yaplParser.NOT, 0)

        def INT_VAR(self):
            return self.getToken(yaplParser.INT_VAR, 0)

        def STR_VAR(self):
            return self.getToken(yaplParser.STR_VAR, 0)

        def TRUE(self):
            return self.getToken(yaplParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(yaplParser.FALSE, 0)

        def ASSIGN(self):
            return self.getToken(yaplParser.ASSIGN, 0)

        def MULT(self):
            return self.getToken(yaplParser.MULT, 0)

        def DIV(self):
            return self.getToken(yaplParser.DIV, 0)

        def PLUS(self):
            return self.getToken(yaplParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(yaplParser.MINUS, 0)

        def LESS_EQUAL(self):
            return self.getToken(yaplParser.LESS_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(yaplParser.LESS_THAN, 0)

        def EQUAL(self):
            return self.getToken(yaplParser.EQUAL, 0)

        def PERIOD(self):
            return self.getToken(yaplParser.PERIOD, 0)

        def AT(self):
            return self.getToken(yaplParser.AT, 0)

        def getRuleIndex(self):
            return yaplParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 85
                self.match(yaplParser.ID_VAR)
                self.state = 86
                self.match(yaplParser.LPAREN)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 96757469966476) != 0):
                    self.state = 87
                    self.expr(0)
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==17:
                        self.state = 88
                        self.match(yaplParser.COMMA)
                        self.state = 89
                        self.expr(0)
                        self.state = 94
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 99
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 100
                self.match(yaplParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 101
                self.match(yaplParser.IF)
                self.state = 102
                self.expr(0)
                self.state = 103
                self.match(yaplParser.THEN)
                self.state = 104
                self.expr(0)
                self.state = 105
                self.match(yaplParser.ELSE)
                self.state = 106
                self.expr(0)
                self.state = 107
                self.match(yaplParser.FI)
                pass

            elif la_ == 3:
                self.state = 109
                self.match(yaplParser.WHILE)
                self.state = 110
                self.expr(0)
                self.state = 111
                self.match(yaplParser.LOOP)
                self.state = 112
                self.expr(0)
                self.state = 113
                self.match(yaplParser.POOL)
                pass

            elif la_ == 4:
                self.state = 115
                self.match(yaplParser.LBRACE)
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 116
                    self.expr(0)
                    self.state = 117
                    self.match(yaplParser.SEMICOLON)
                    self.state = 121 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 96757469966476) != 0)):
                        break

                self.state = 123
                self.match(yaplParser.RBRACE)
                pass

            elif la_ == 5:
                self.state = 125
                self.match(yaplParser.LET)
                self.state = 126
                self.varTypescript()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 127
                    self.match(yaplParser.COMMA)
                    self.state = 128
                    self.varTypescript()
                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 134
                self.match(yaplParser.IN)
                self.state = 135
                self.expr(19)
                pass

            elif la_ == 6:
                self.state = 137
                self.match(yaplParser.NEW)
                self.state = 138
                self.match(yaplParser.TYPE_IDENTIFIER)
                pass

            elif la_ == 7:
                self.state = 139
                self.match(yaplParser.NEGATIVE)
                self.state = 140
                self.expr(17)
                pass

            elif la_ == 8:
                self.state = 141
                self.match(yaplParser.ISVOID)
                self.state = 142
                self.expr(16)
                pass

            elif la_ == 9:
                self.state = 143
                self.match(yaplParser.NOT)
                self.state = 144
                self.expr(8)
                pass

            elif la_ == 10:
                self.state = 145
                self.match(yaplParser.LPAREN)
                self.state = 146
                self.expr(0)
                self.state = 147
                self.match(yaplParser.RPAREN)
                pass

            elif la_ == 11:
                self.state = 149
                self.match(yaplParser.ID_VAR)
                pass

            elif la_ == 12:
                self.state = 150
                self.match(yaplParser.INT_VAR)
                pass

            elif la_ == 13:
                self.state = 151
                self.match(yaplParser.STR_VAR)
                pass

            elif la_ == 14:
                self.state = 152
                self.match(yaplParser.TRUE)
                pass

            elif la_ == 15:
                self.state = 153
                self.match(yaplParser.FALSE)
                pass

            elif la_ == 16:
                self.state = 154
                self.match(yaplParser.ID_VAR)
                self.state = 155
                self.match(yaplParser.ASSIGN)
                self.state = 156
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 202
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = yaplParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 159
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 160
                        self.match(yaplParser.MULT)
                        self.state = 161
                        self.expr(16)
                        pass

                    elif la_ == 2:
                        localctx = yaplParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 163
                        self.match(yaplParser.DIV)
                        self.state = 164
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = yaplParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 166
                        self.match(yaplParser.PLUS)
                        self.state = 167
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = yaplParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 169
                        self.match(yaplParser.MINUS)
                        self.state = 170
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = yaplParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 171
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 172
                        self.match(yaplParser.LESS_EQUAL)
                        self.state = 173
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = yaplParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 174
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 175
                        self.match(yaplParser.LESS_THAN)
                        self.state = 176
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = yaplParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 177
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 178
                        self.match(yaplParser.EQUAL)
                        self.state = 179
                        self.expr(10)
                        pass

                    elif la_ == 8:
                        localctx = yaplParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 180
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 183
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==26:
                            self.state = 181
                            self.match(yaplParser.AT)
                            self.state = 182
                            self.match(yaplParser.TYPE_IDENTIFIER)


                        self.state = 185
                        self.match(yaplParser.PERIOD)
                        self.state = 186
                        self.match(yaplParser.ID_VAR)
                        self.state = 187
                        self.match(yaplParser.LPAREN)
                        self.state = 198
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & 96757469966476) != 0):
                            self.state = 188
                            self.expr(0)
                            self.state = 193
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==17:
                                self.state = 189
                                self.match(yaplParser.COMMA)
                                self.state = 190
                                self.expr(0)
                                self.state = 195
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)

                            self.state = 200
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 201
                        self.match(yaplParser.RPAREN)
                        pass

             
                self.state = 206
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
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 23)
         




