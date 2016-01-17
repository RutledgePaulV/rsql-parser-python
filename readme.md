### rsql-python

A python parser and tree visiting library for RSQL (resource query language). Lexer and parser
are generated using an antlr4 grammar.

RSQL is a concise query language that makes an ideal candidate for flexible query support on
list endpoints of a rest api.


```python
from rsql_python import *


class Reflect(QueryGeneratingVisitor):

	def and_node(self, children):
		return ';'.join(list(map(str, children)))

	def or_node(self, children):
		return ','.join(list(map(str, children)))

	def wrap(self, child):
		return "(" + child + ")"

	def comparison(self, key, operator, values):
		if not isinstance(values, list):
			return key + operator + str(values)
		else:
			return key + operator + "(" + ','.join(list(map(str,values))) + ")"


result = parse("(abasdfasd=ex=true;thing=='stuff'),something!=3.0", Reflect())

print(result)

# (abasdfasd=ex=True;thing=='stuff'),something!=3.0
```

### License

This project is licensed under [MIT license](http://opensource.org/licenses/MIT).