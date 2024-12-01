lexer grammar ExprLexer;

INITIALIZE: 'initialize';
COMMAND: 'command';
MOVE: 'move';
ROTATE: 'rotate';
FIRE: 'fire';
USE: 'use';
STATUS: 'status';
WIN: 'win';
OBJECT: 'object';
PLAYER: 'player';

TO: 'to';
COMMA: ',';
COLON: ':';
EQUALS: '=';

NUMBER: [0-9]+;
ID: [a-zA-Z_][a-zA-Z_0-9]*;

WS: [ \t\r\n]+ -> skip;
