from States.IState import IState

class StackErrorState(IState):
    def __init__(self, current_state, symbol, next_state, stack, lexer, valid_tokens):
        self.current_state = current_state
        self.symbol = symbol
        self.next_state = next_state
        self.stack = stack
        self.lexer = lexer
        self.valid_tokens = valid_tokens

    def execute(self):
        self.lexer.error(self.symbol, self.valid_tokens)
        print(f"Pushing to stack: {self.current_state}")
        self.stack.push(self.current_state + 1)
        return self.next_state
