from gen.RsqlParser import *
from gen.RsqlLexer import *
from gen.RsqlVisitor import *

lexer = RsqlLexer(InputStream("(abasdfasd=ex=true;thing=='stuff'),something!=3.0"))
parser = RsqlParser(CommonTokenStream(lexer))

tree = parser.statement()

print(tree.getChildCount())