# Generated from /Users/paul.rutledge/PyCharmProjects/rsql-python/Rsql.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RsqlParser import RsqlParser
else:
    from RsqlParser import RsqlParser

# This class defines a complete generic visitor for a parse tree produced by RsqlParser.

class RsqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RsqlParser#statement.
    def visitStatement(self, ctx:RsqlParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RsqlParser#boolean_value.
    def visitBoolean_value(self, ctx:RsqlParser.Boolean_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RsqlParser#single_value.
    def visitSingle_value(self, ctx:RsqlParser.Single_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RsqlParser#multi_value.
    def visitMulti_value(self, ctx:RsqlParser.Multi_valueContext):
        return self.visitChildren(ctx)



del RsqlParser