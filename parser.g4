parser grammar ExprParser;
options { tokenVocab=ExprLexer; }

game: rules+;

rules
    : includeRule
    | canRule
    | canControlRule
    | predatesRule
    | mustRule
    ;

includeRule : ID INCLUDE list_id;

canRule : ID CAN list_id;

canControlRule: ID CAN_CONTROL list_id;

predatesRule : ID PREDATES ID;

mustRule: ID MUST ID WHILE ID;


list_id: ID (COMMA ID)* ;

