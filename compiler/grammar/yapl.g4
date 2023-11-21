grammar yapl;

import lexers;

program: (classDefinition SEMICOLON)+;

formal: ID_VAR COLON TYPE_IDENTIFIER #args;

varTypescript:
    <assoc = right> ID_VAR COLON TYPE_IDENTIFIER (ASSIGN expr)? # attributeDeclaration;

classDefinition:
    CLASS TYPE_IDENTIFIER (INHERITS TYPE_IDENTIFIER)? LBRACE (featureDefinition SEMICOLON)* RBRACE;

featureDefinition:
    methodDefinition
    | attributeDefinition;

methodDefinition:
    ID_VAR LPAREN (formal (COMMA formal)*)* RPAREN COLON TYPE_IDENTIFIER LBRACE expr RBRACE # methodDef;

attributeDefinition:
    <assoc = right> ID_VAR COLON TYPE_IDENTIFIER (ASSIGN expr)? # attr;

expr:
    expr (MULT | DIV | PLUS | MINUS) expr                 #arith
    | expr (LESS_THAN | LESS_EQUAL | GREATER_THAN | GREATER_EQUAL | EQUAL) expr               #bool
    | NEW TYPE_IDENTIFIER                                 #new_type
    | NEGATIVE expr                                       #negative_expr
    | ISVOID expr                                         #void_expr
    | NOT expr                                            #not_expr
    | ID_VAR                                              #id_var
    | (INT_VAR | STR_VAR | BOOL_VAR)                      #simple_var
    | <assoc = right> ID_VAR ASSIGN expr                  #asign_expr
    | ID_VAR LPAREN (expr (COMMA expr)*)* RPAREN          #params
    | IF expr THEN expr ELSE expr FI                      #statement_if
    | WHILE expr LOOP expr POOL                           #statement_while
    | LBRACE (expr SEMICOLON)+ RBRACE                     #statement_brace
    | LET varTypescript (COMMA varTypescript)* IN expr    #statement_let
    | LPAREN expr RPAREN                                  #statement_paren
	| expr (AT TYPE_IDENTIFIER)? PERIOD ID_VAR LPAREN (
		expr (COMMA expr)*
	)* RPAREN                                             #statement_at;