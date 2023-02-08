import pandas as pd

extranjeros = pd.read_csv("./exterior.csv")

print(extranjeros["Área Conocimiento"])
print("")
print(extranjeros.head(20))
print("")
print(extranjeros.tail(35))
print("")
print(extranjeros.mean())
print("")
print(extranjeros.columns)