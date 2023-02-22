import pandas as pd

extranjeros = pd.read_csv("./exterior.csv")

print(extranjeros["Área Conocimiento"])
print("")
print(extranjeros.head(20))
print("")
print(extranjeros.tail(35))
print("")
print(extranjeros.head(1000).mean())
print("")
print(extranjeros.columns)

pd.set_option('max_rows', None)
pd.set_option('max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(extranjeros)