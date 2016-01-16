grammar Rsql;

options {
    language = Python3;
}

statement
    : statement ( AND_OPERATOR | OR_OPERATOR ) statement
    | L_PAREN statement R_PAREN
    | IDENTIFIER ( EQ | NE | GT | GTE | LT | LTE ) single_value
    | IDENTIFIER ( IN | NIN ) multi_value
    | IDENTIFIER ( EX ) boolean_value
    ;


TRUE: 'true';
FALSE: 'false';
AND_OPERATOR: ';';
OR_OPERATOR: ',';
L_PAREN: '(';
R_PAREN: ')';
EQ: '==';
NE: '!=';
IN: '=in=';
NIN: '=out=';
GT: '=gt=';
LT: '=lt=';
GTE: '=ge=';
LTE: '=le=';
EX: '=ex=';


IDENTIFIER
 : [a-zA-Z_] [a-zA-Z_0-9]*
 ;

boolean_value
    : TRUE
    | FALSE
    ;

single_value
    : TRUE
    | FALSE
    | STRING_LITERAL
    | NUMERIC_LITERAL
    ;

multi_value
    : '(' single_value ( ',' single_value )* ')'
    | single_value
    ;

NUMERIC_LITERAL
    : DIGIT+ ( '.' DIGIT* )? ( [-+]? DIGIT+ )?
    | '.' DIGIT+ ( [-+]? DIGIT+ )?
    ;

STRING_LITERAL
    : '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n'] )* '\''
    | '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n"] )* '"'
    ;

STRING_ESCAPE_SEQ
    : '\\' .
    ;

fragment DIGIT : [0-9];