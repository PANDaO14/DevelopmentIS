from States.IState import IState

class AcceptErrorState(IState):
    def __init__(self, current_state, symbol, next_state, stack, lexer, valid_tokens):
        self.current_state = current_state
        self.symbol = symbol
        self.next_state = next_state
        self.stack = stack
        self.lexer = lexer
        self.valid_tokens = valid_tokens

    def execute(self):
        self.lexer.error(self.symbol, self.valid_tokens)
        print(f"ACCEPTING: {self.symbol}")
        self.lexer.accept(self.symbol)
        return self.next_state
