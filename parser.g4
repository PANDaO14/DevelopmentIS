parser grammar ExprParser;
options { tokenVocab=ExprLexer; }

game
    : initialization command+;

initialization
    : INITIALIZE playerShipList;

playerShipList
    : playerShip (COMMA playerShip)*;

playerShip
    : PLAYER ID EQUALS OBJECT ID;

command
    : moveCommand
    | rotateCommand
    | fireCommand
    | useCommand
    | statusCommand
    | winCommand;

moveCommand
    : COMMAND ID MOVE ID TO NUMBER;

rotateCommand
    : COMMAND ID ROTATE ID TO ID;

fireCommand
    : COMMAND ID FIRE ID TO ID;

useCommand
    : COMMAND ID USE ID TO ID;

statusCommand
    : COMMAND ID STATUS ID;

winCommand
    : COMMAND ID WIN ID;
