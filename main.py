import pandas as pd

df = pd.read_excel("РИС_ЛР_2.xlsx", index_col = "№")
print(df)

dictionary = {}
for i in range(1, df.shape[0]+1):
  dictionary[i] = []
  for j in df.columns:
    dictionary[i].append(df[j][i])

print(dictionary)

