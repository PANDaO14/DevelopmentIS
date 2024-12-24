from States.ZeroState import ZeroState
from States.ErrorState import ErrorState
from States.ReturnErrorState import ReturnErrorState
from States.ReturnAcceptErrorState import ReturnAcceptErrorState
from States.AcceptErrorState import AcceptErrorState
from States.StackErrorState import StackErrorState
from States.Stack import Stack

from Lexer.Lexer import Lexer

class LL1Parser:
    def __init__(self, transitions):
        self.transitions = transitions
        self.state_map = {
            (0, 0, 0, 0): ZeroState,
            (0, 0, 0, 1): ErrorState,
            (0, 1, 0, 1): StackErrorState,
            (0, 0, 1, 1): AcceptErrorState,
            (1, 0, 0, 1): ReturnErrorState,
            (1, 0, 1, 1): ReturnAcceptErrorState
        }
        self.current_state = 1
        self.stack = Stack()
        self.lexer = None

    def process(self, tokens):
        self.lexer = Lexer(" ".join(tokens))
        current_token = self.lexer.get_current_token()
        
        while current_token is not None:
            if current_token == 'end' and self.stack.is_empty():
              print("Parsing complete")
              break

            state_data = self.transitions[self.current_state]
            print(f"State: {self.current_state}\t Token: {current_token}\t Stack: {self.stack}")

            valid_tokens, next_state, attr1, attr2, attr3, attr4 = state_data
            if not self.lexer.check(current_token, valid_tokens) and attr4 == 0:
                print(f"Unexpected symbol '{current_token}', skipping to state {self.current_state + 1}")
                self.current_state += 1
                current_token = self.lexer.get_current_token()
                continue

            state_key = (attr1, attr2, attr3, attr4)
            state_class = self.state_map[state_key]
            state_instance = state_class(self.current_state, current_token, next_state, self.stack, self.lexer, valid_tokens)
            self.current_state = state_instance.execute()
            current_token = self.lexer.get_current_token()

        print("Grammar is true")
