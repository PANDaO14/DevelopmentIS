import pandas as pd

from Lexer.Lexer import Lexer
from Parser.LL1Parser import LL1Parser

df = pd.read_excel("РИС_ЛР_2.xlsx", index_col = "№")
print(df)

dictionary = {}
for i in range(1, df.shape[0] + 1):
  dictionary[i] = []
  for j in df.columns:
    dictionary[i].append(df[j][i])

inputs = ["27 - 10 * ( 10 + 6 / 7 - ( 30 - 2 ) )", "cos ( 120 )", "15 + 2 /"]
for input in inputs:
  lexer = Lexer(input)
  tokens = lexer.tokens
  ll1 = LL1Parser(dictionary)
  print(f"\nINPUT: {input}")
  print("----------------------------")
  ll1.process(tokens)
