# Generated from /Users/paul.rutledge/PyCharmProjects/rsql-python/Rsql.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RsqlParser import RsqlParser
else:
    from RsqlParser import RsqlParser

# This class defines a complete listener for a parse tree produced by RsqlParser.
class RsqlListener(ParseTreeListener):

    # Enter a parse tree produced by RsqlParser#statement.
    def enterStatement(self, ctx:RsqlParser.StatementContext):
        pass

    # Exit a parse tree produced by RsqlParser#statement.
    def exitStatement(self, ctx:RsqlParser.StatementContext):
        pass


    # Enter a parse tree produced by RsqlParser#comparison.
    def enterComparison(self, ctx:RsqlParser.ComparisonContext):
        pass

    # Exit a parse tree produced by RsqlParser#comparison.
    def exitComparison(self, ctx:RsqlParser.ComparisonContext):
        pass


    # Enter a parse tree produced by RsqlParser#boolean_value.
    def enterBoolean_value(self, ctx:RsqlParser.Boolean_valueContext):
        pass

    # Exit a parse tree produced by RsqlParser#boolean_value.
    def exitBoolean_value(self, ctx:RsqlParser.Boolean_valueContext):
        pass


    # Enter a parse tree produced by RsqlParser#single_value.
    def enterSingle_value(self, ctx:RsqlParser.Single_valueContext):
        pass

    # Exit a parse tree produced by RsqlParser#single_value.
    def exitSingle_value(self, ctx:RsqlParser.Single_valueContext):
        pass


    # Enter a parse tree produced by RsqlParser#multi_value.
    def enterMulti_value(self, ctx:RsqlParser.Multi_valueContext):
        pass

    # Exit a parse tree produced by RsqlParser#multi_value.
    def exitMulti_value(self, ctx:RsqlParser.Multi_valueContext):
        pass


