### rsql-python

A python parser and tree visiting library for RSQL (resource query language). Lexer and parser
are generated using an antlr4 grammar. RSQL is a concise query language that makes an ideal
candidate for flexible query support on list endpoints of a rest api.


```python
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
			return where(key).exists() if values == True else ~where(key).exists()
		elif operator == '=in=':
			return where(key).any(values)
		elif operator == '=out=':
			return ~where(key).any(values)
		else:
			raise NotImplementedError



tiny_db_query = parse("(abasdfasd=ex=true;thing=='stuff'),something!=3.0", Tiny())

print(tiny_db_query)
# QueryImpl('or', frozenset({('!=', ('something',), 3.0), ('and', frozenset({('exists', ('abasdfasd',)), ('==', ('thing',), 'stuff')}))}))
```

### License

This project is licensed under [MIT license](http://opensource.org/licenses/MIT).