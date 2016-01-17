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