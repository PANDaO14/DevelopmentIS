class Lexer:
    def __init__(self, input_string):
        self.tokens = self.tokenize(input_string)
        self.current_index = 0

    def tokenize(self, input_string):
        terminal_symbols = [",", ")", "(", "true", "false", "*", "/", "+", "-", "or", "and", "not", "end", "const", "def", "=", "<", ">"]
        words = input_string.split()
        tokens = []

        for i, word in enumerate(words):
            if word.isdigit():
                tokens.append("const")
            elif word not in terminal_symbols:
                tokens.append("def" if (i + 1 < len(words) and words[i + 1] == "(") else "var")
            else:
                tokens.append(word)

        tokens.append("end")
        return tokens

    def get_current_token(self):
        if self.current_index < len(self.tokens):
            return self.tokens[self.current_index]
        return None

    def accept(self, symbol):
        current_token = self.get_current_token()
        if current_token == symbol:
            self.current_index += 1
            return True
        return False

    def error(self, symbol, valid_symbols):
        if symbol not in valid_symbols:
            raise ValueError("ERROR")

    def check(self, symbol, valid_symbols):
      return symbol in valid_symbols
