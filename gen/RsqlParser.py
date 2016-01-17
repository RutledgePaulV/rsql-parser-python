# Generated from /Users/paul.rutledge/PyCharmProjects/rsql-python/Rsql.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\25")
        buf.write(":\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\7\2\30\n\2\f\2\16")
        buf.write("\2\33\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3&\n")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\7\6\60\n\6\f\6\16\6")
        buf.write("\63\13\6\3\6\3\6\3\6\5\68\n\6\3\6\2\3\2\7\2\4\6\b\n\2")
        buf.write("\7\3\2\5\6\4\2\t\n\r\20\3\2\13\f\3\2\3\4\4\2\3\4\23\24")
        buf.write(":\2\22\3\2\2\2\4%\3\2\2\2\6\'\3\2\2\2\b)\3\2\2\2\n\67")
        buf.write("\3\2\2\2\f\r\b\2\1\2\r\16\7\7\2\2\16\17\5\2\2\2\17\20")
        buf.write("\7\b\2\2\20\23\3\2\2\2\21\23\5\4\3\2\22\f\3\2\2\2\22\21")
        buf.write("\3\2\2\2\23\31\3\2\2\2\24\25\f\5\2\2\25\26\t\2\2\2\26")
        buf.write("\30\5\2\2\6\27\24\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2")
        buf.write("\31\32\3\2\2\2\32\3\3\2\2\2\33\31\3\2\2\2\34\35\7\22\2")
        buf.write("\2\35\36\t\3\2\2\36&\5\b\5\2\37 \7\22\2\2 !\t\4\2\2!&")
        buf.write("\5\n\6\2\"#\7\22\2\2#$\7\21\2\2$&\5\6\4\2%\34\3\2\2\2")
        buf.write("%\37\3\2\2\2%\"\3\2\2\2&\5\3\2\2\2\'(\t\5\2\2(\7\3\2\2")
        buf.write("\2)*\t\6\2\2*\t\3\2\2\2+,\7\7\2\2,\61\5\b\5\2-.\7\6\2")
        buf.write("\2.\60\5\b\5\2/-\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61")
        buf.write("\62\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64\65\7\b\2\2")
        buf.write("\658\3\2\2\2\668\5\b\5\2\67+\3\2\2\2\67\66\3\2\2\28\13")
        buf.write("\3\2\2\2\7\22\31%\61\67")
        return buf.getvalue()


class RsqlParser ( Parser ):

    grammarFileName = "Rsql.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "';'", "','", "'('", 
                     "')'", "'=='", "'!='", "'=in='", "'=out='", "'=gt='", 
                     "'=lt='", "'=ge='", "'=le='", "'=ex='" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "AND_OPERATOR", "OR_OPERATOR", 
                      "L_PAREN", "R_PAREN", "EQ", "NE", "IN", "NIN", "GT", 
                      "LT", "GTE", "LTE", "EX", "IDENTIFIER", "NUMERIC_LITERAL", 
                      "STRING_LITERAL", "STRING_ESCAPE_SEQ" ]

    RULE_statement = 0
    RULE_comparison = 1
    RULE_boolean_value = 2
    RULE_single_value = 3
    RULE_multi_value = 4

    ruleNames =  [ "statement", "comparison", "boolean_value", "single_value", 
                   "multi_value" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    AND_OPERATOR=3
    OR_OPERATOR=4
    L_PAREN=5
    R_PAREN=6
    EQ=7
    NE=8
    IN=9
    NIN=10
    GT=11
    LT=12
    GTE=13
    LTE=14
    EX=15
    IDENTIFIER=16
    NUMERIC_LITERAL=17
    STRING_LITERAL=18
    STRING_ESCAPE_SEQ=19

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # StatementContext
            self.wrapped = None # StatementContext
            self.node = None # ComparisonContext
            self.op = None # Token
            self.right = None # StatementContext

        def L_PAREN(self):
            return self.getToken(RsqlParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(RsqlParser.R_PAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RsqlParser.StatementContext)
            else:
                return self.getTypedRuleContext(RsqlParser.StatementContext,i)


        def comparison(self):
            return self.getTypedRuleContext(RsqlParser.ComparisonContext,0)


        def AND_OPERATOR(self):
            return self.getToken(RsqlParser.AND_OPERATOR, 0)

        def OR_OPERATOR(self):
            return self.getToken(RsqlParser.OR_OPERATOR, 0)

        def getRuleIndex(self):
            return RsqlParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)



    def statement(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RsqlParser.StatementContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_statement, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            token = self._input.LA(1)
            if token in [RsqlParser.L_PAREN]:
                self.state = 11
                self.match(RsqlParser.L_PAREN)
                self.state = 12
                localctx.wrapped = self.statement(0)
                self.state = 13
                self.match(RsqlParser.R_PAREN)

            elif token in [RsqlParser.IDENTIFIER]:
                self.state = 15
                localctx.node = self.comparison()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RsqlParser.StatementContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement)
                    self.state = 18
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 19
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==RsqlParser.AND_OPERATOR or _la==RsqlParser.OR_OPERATOR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self.consume()
                    self.state = 20
                    localctx.right = self.statement(4) 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ComparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.key = None # Token
            self.op = None # Token
            self.value = None # Single_valueContext

        def IDENTIFIER(self):
            return self.getToken(RsqlParser.IDENTIFIER, 0)

        def single_value(self):
            return self.getTypedRuleContext(RsqlParser.Single_valueContext,0)


        def EQ(self):
            return self.getToken(RsqlParser.EQ, 0)

        def NE(self):
            return self.getToken(RsqlParser.NE, 0)

        def GT(self):
            return self.getToken(RsqlParser.GT, 0)

        def GTE(self):
            return self.getToken(RsqlParser.GTE, 0)

        def LT(self):
            return self.getToken(RsqlParser.LT, 0)

        def LTE(self):
            return self.getToken(RsqlParser.LTE, 0)

        def multi_value(self):
            return self.getTypedRuleContext(RsqlParser.Multi_valueContext,0)


        def IN(self):
            return self.getToken(RsqlParser.IN, 0)

        def NIN(self):
            return self.getToken(RsqlParser.NIN, 0)

        def EX(self):
            return self.getToken(RsqlParser.EX, 0)

        def boolean_value(self):
            return self.getTypedRuleContext(RsqlParser.Boolean_valueContext,0)


        def getRuleIndex(self):
            return RsqlParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = RsqlParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.state = 35
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                localctx.key = self.match(RsqlParser.IDENTIFIER)
                self.state = 27
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RsqlParser.EQ) | (1 << RsqlParser.NE) | (1 << RsqlParser.GT) | (1 << RsqlParser.LT) | (1 << RsqlParser.GTE) | (1 << RsqlParser.LTE))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 28
                localctx.value = self.single_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                localctx.key = self.match(RsqlParser.IDENTIFIER)
                self.state = 30
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==RsqlParser.IN or _la==RsqlParser.NIN):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 31
                localctx.value = self.multi_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                localctx.key = self.match(RsqlParser.IDENTIFIER)
                self.state = 33
                localctx.op = self.match(RsqlParser.EX)
                self.state = 34
                localctx.value = self.boolean_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(RsqlParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(RsqlParser.FALSE, 0)

        def getRuleIndex(self):
            return RsqlParser.RULE_boolean_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_value" ):
                listener.enterBoolean_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_value" ):
                listener.exitBoolean_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_value" ):
                return visitor.visitBoolean_value(self)
            else:
                return visitor.visitChildren(self)




    def boolean_value(self):

        localctx = RsqlParser.Boolean_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_boolean_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not(_la==RsqlParser.TRUE or _la==RsqlParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Single_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(RsqlParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(RsqlParser.FALSE, 0)

        def STRING_LITERAL(self):
            return self.getToken(RsqlParser.STRING_LITERAL, 0)

        def NUMERIC_LITERAL(self):
            return self.getToken(RsqlParser.NUMERIC_LITERAL, 0)

        def getRuleIndex(self):
            return RsqlParser.RULE_single_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_value" ):
                listener.enterSingle_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_value" ):
                listener.exitSingle_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_value" ):
                return visitor.visitSingle_value(self)
            else:
                return visitor.visitChildren(self)




    def single_value(self):

        localctx = RsqlParser.Single_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_single_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RsqlParser.TRUE) | (1 << RsqlParser.FALSE) | (1 << RsqlParser.NUMERIC_LITERAL) | (1 << RsqlParser.STRING_LITERAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Multi_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RsqlParser.Single_valueContext)
            else:
                return self.getTypedRuleContext(RsqlParser.Single_valueContext,i)


        def getRuleIndex(self):
            return RsqlParser.RULE_multi_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulti_value" ):
                listener.enterMulti_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulti_value" ):
                listener.exitMulti_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_value" ):
                return visitor.visitMulti_value(self)
            else:
                return visitor.visitChildren(self)




    def multi_value(self):

        localctx = RsqlParser.Multi_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_multi_value)
        self._la = 0 # Token type
        try:
            self.state = 53
            token = self._input.LA(1)
            if token in [RsqlParser.L_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(RsqlParser.L_PAREN)
                self.state = 42
                self.single_value()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RsqlParser.OR_OPERATOR:
                    self.state = 43
                    self.match(RsqlParser.OR_OPERATOR)
                    self.state = 44
                    self.single_value()
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 50
                self.match(RsqlParser.R_PAREN)

            elif token in [RsqlParser.TRUE, RsqlParser.FALSE, RsqlParser.NUMERIC_LITERAL, RsqlParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.single_value()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.statement_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def statement_sempred(self, localctx:StatementContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




