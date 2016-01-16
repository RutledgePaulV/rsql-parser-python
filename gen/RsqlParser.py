# Generated from /Users/paul.rutledge/PyCharmProjects/rsql-python/Rsql.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\25")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\31\n\2\3\2")
        buf.write("\3\2\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\7\5+\n\5\f\5\16\5.\13\5\3\5\3\5\3\5\5\5\63")
        buf.write("\n\5\3\5\2\3\2\6\2\4\6\b\2\7\4\2\t\n\r\20\3\2\13\f\3\2")
        buf.write("\5\6\3\2\3\4\4\2\3\4\23\24\66\2\30\3\2\2\2\4\"\3\2\2\2")
        buf.write("\6$\3\2\2\2\b\62\3\2\2\2\n\13\b\2\1\2\13\f\7\7\2\2\f\r")
        buf.write("\5\2\2\2\r\16\7\b\2\2\16\31\3\2\2\2\17\20\7\22\2\2\20")
        buf.write("\21\t\2\2\2\21\31\5\6\4\2\22\23\7\22\2\2\23\24\t\3\2\2")
        buf.write("\24\31\5\b\5\2\25\26\7\22\2\2\26\27\7\21\2\2\27\31\5\4")
        buf.write("\3\2\30\n\3\2\2\2\30\17\3\2\2\2\30\22\3\2\2\2\30\25\3")
        buf.write("\2\2\2\31\37\3\2\2\2\32\33\f\7\2\2\33\34\t\4\2\2\34\36")
        buf.write("\5\2\2\b\35\32\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3")
        buf.write("\2\2\2 \3\3\2\2\2!\37\3\2\2\2\"#\t\5\2\2#\5\3\2\2\2$%")
        buf.write("\t\6\2\2%\7\3\2\2\2&\'\7\7\2\2\',\5\6\4\2()\7\6\2\2)+")
        buf.write("\5\6\4\2*(\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-/\3\2")
        buf.write("\2\2.,\3\2\2\2/\60\7\b\2\2\60\63\3\2\2\2\61\63\5\6\4\2")
        buf.write("\62&\3\2\2\2\62\61\3\2\2\2\63\t\3\2\2\2\6\30\37,\62")
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
    RULE_boolean_value = 1
    RULE_single_value = 2
    RULE_multi_value = 3

    ruleNames =  [ "statement", "boolean_value", "single_value", "multi_value" ]

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

        def L_PAREN(self):
            return self.getToken(RsqlParser.L_PAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RsqlParser.StatementContext)
            else:
                return self.getTypedRuleContext(RsqlParser.StatementContext,i)


        def R_PAREN(self):
            return self.getToken(RsqlParser.R_PAREN, 0)

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

        def boolean_value(self):
            return self.getTypedRuleContext(RsqlParser.Boolean_valueContext,0)


        def EX(self):
            return self.getToken(RsqlParser.EX, 0)

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
            self.state = 22
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 9
                self.match(RsqlParser.L_PAREN)
                self.state = 10
                self.statement(0)
                self.state = 11
                self.match(RsqlParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 13
                self.match(RsqlParser.IDENTIFIER)
                self.state = 14
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RsqlParser.EQ) | (1 << RsqlParser.NE) | (1 << RsqlParser.GT) | (1 << RsqlParser.LT) | (1 << RsqlParser.GTE) | (1 << RsqlParser.LTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 15
                self.single_value()
                pass

            elif la_ == 3:
                self.state = 16
                self.match(RsqlParser.IDENTIFIER)
                self.state = 17
                _la = self._input.LA(1)
                if not(_la==RsqlParser.IN or _la==RsqlParser.NIN):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 18
                self.multi_value()
                pass

            elif la_ == 4:
                self.state = 19
                self.match(RsqlParser.IDENTIFIER)

                self.state = 20
                self.match(RsqlParser.EX)
                self.state = 21
                self.boolean_value()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RsqlParser.StatementContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement)
                    self.state = 24
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 25
                    _la = self._input.LA(1)
                    if not(_la==RsqlParser.AND_OPERATOR or _la==RsqlParser.OR_OPERATOR):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()
                    self.state = 26
                    self.statement(6) 
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 2, self.RULE_boolean_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
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
        self.enterRule(localctx, 4, self.RULE_single_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
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
        self.enterRule(localctx, 6, self.RULE_multi_value)
        self._la = 0 # Token type
        try:
            self.state = 48
            token = self._input.LA(1)
            if token in [RsqlParser.L_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(RsqlParser.L_PAREN)
                self.state = 37
                self.single_value()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RsqlParser.OR_OPERATOR:
                    self.state = 38
                    self.match(RsqlParser.OR_OPERATOR)
                    self.state = 39
                    self.single_value()
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 45
                self.match(RsqlParser.R_PAREN)

            elif token in [RsqlParser.TRUE, RsqlParser.FALSE, RsqlParser.NUMERIC_LITERAL, RsqlParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
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
                return self.precpred(self._ctx, 5)
         




