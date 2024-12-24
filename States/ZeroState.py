from States.IState import IState

class ZeroState(IState):
    def __init__(self, current_state, symbol, next_state, stack, lexer, valid_tokens):
        self.current_state = current_state
        self.symbol = symbol
        self.next_state = next_state
        self.stack = stack
        self.lexer = lexer

    def execute(self):
        return self.next_state
