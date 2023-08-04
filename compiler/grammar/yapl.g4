grammar yapl;

import lexers;

program: (classDefinition SEMICOLON)+;

formal: ID_VAR COLON TYPE_IDENTIFIER;

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
    ID_VAR LPAREN (expr (COMMA expr)*)* RPAREN
	| expr (AT TYPE_IDENTIFIER)? PERIOD ID_VAR LPAREN (
		expr (COMMA expr)*
	)* RPAREN	
    | IF expr THEN expr ELSE expr FI
    | WHILE expr LOOP expr POOL
    | LBRACE (expr SEMICOLON)+ RBRACE
    | LET varTypescript (COMMA varTypescript)* IN expr
    | NEW TYPE_IDENTIFIER
    | NEGATIVE expr
    | ISVOID expr
    | expr MULT expr
    | expr DIV expr
    | expr PLUS expr
    | expr MINUS expr
    | expr LESS_EQUAL expr
    | expr LESS_THAN expr
    | expr EQUAL expr
    | NOT expr
    | LPAREN expr RPAREN
    | ID_VAR
    | INT_VAR
    | STR_VAR
    | BOOL_VAR
    | <assoc = right> ID_VAR ASSIGN expr;