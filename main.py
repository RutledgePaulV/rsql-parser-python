from rsql_python import *
from tinydb import *
import operator, functools


class Tiny(QueryGeneratingVisitor):

	def and_node(self, children):
		return functools.reduce(operator.and_, children)

	def or_node(self, children):
		return functools.reduce(operator.or_, children)

	def wrap(self, child):
		return (child)

	def comparison(self, key, operator, values):
		if operator == '==':
			return where(key) == values
		elif operator == '!=':
			return where(key) != values
		elif operator == '=gt=':
			return where(key) > values
		elif operator == '=ge=':
			return where(key) >= values
		elif operator == '=lt=':
			return where(key) < values
		elif operator == '=le=':
			return where(key) <= values
		elif operator == '=ex=':
			if values == True:
				return where(key).exists()
			else:
				return ~where(key).exists()
		elif operator == '=in=':
			return where(key).any(values)
		elif operator == '=out=':
			return ~where(key).any(values)
		else:
			raise NotImplementedError



tiny_db_query = parse("(abasdfasd=ex=true;thing=='stuff'),something!=3.0", Tiny())

print(tiny_db_query)
# QueryImpl('or', frozenset({('!=', ('something',), 3.0), ('and', frozenset({('exists', ('abasdfasd',)), ('==', ('thing',), 'stuff')}))}))