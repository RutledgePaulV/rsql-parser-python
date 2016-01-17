from gen.RsqlParser import *
from gen.RsqlLexer import *
from gen.RsqlVisitor import *


class QueryGeneratingVisitor(object):

	def and_node(self, children):
		raise NotImplementedError

	def or_node(self, children):
		raise NotImplementedError

	def wrap(self, child):
		raise NotImplementedError

	def comparison(self, key, operator, values):
		raise NotImplementedError


class Visitor(RsqlVisitor):
	def __init__(self, delegate: QueryGeneratingVisitor):
		self.delegate = delegate

	def visitStatement(self, ctx: RsqlParser.StatementContext):
		if ctx.left and ctx.op and ctx.right:
			if ctx.op.type == RsqlParser.AND_OPERATOR:
				return self.delegate.and_node((self.visit(ctx.left), self.visit(ctx.right)))
			elif ctx.op.type == RsqlParser.OR_OPERATOR:
				return self.delegate.or_node((self.visit(ctx.left), self.visit(ctx.right)))
		elif ctx.wrapped:
			return self.delegate.wrap(self.visit(ctx.wrapped))
		elif ctx.node:
			return self.visit(ctx.node)

	def visitComparison(self, ctx: RsqlParser.ComparisonContext):
		return self.delegate.comparison(ctx.key.text, ctx.op.text, self.visit(ctx.value))

	def visitBoolean_value(self, ctx: RsqlParser.Boolean_valueContext):
		return bool(ctx.getText())

	def visitSingle_value(self, ctx: RsqlParser.Single_valueContext):
		if ctx.TRUE() or ctx.FALSE():
			return bool(ctx.getText())
		elif ctx.NUMERIC_LITERAL():
			textual = ctx.getText()
			if '.' in textual:
				return float(ctx.getText())
			else:
				return int(ctx.getText())
		elif ctx.STRING_LITERAL():
			return str(ctx.getText())
		else:
			raise NotImplementedError


def parse(rsql: str, visitor: QueryGeneratingVisitor):
	lexer = RsqlLexer(InputStream(rsql))
	parser = RsqlParser(CommonTokenStream(lexer))
	tree = parser.statement()
	return tree.accept(Visitor(visitor))
