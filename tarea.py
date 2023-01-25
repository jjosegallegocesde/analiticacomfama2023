import pandas as pd

fuenteDatos=pd.read_csv("./empleados.csv")

# 1. primeros 50 empleados
filtrohead=fuenteDatos.head(60)
print("\n")
print("\n")
print("\n")
print(filtrohead)

# 2. primeros 50 empleados,salario
filtrohead2=fuenteDatos["salario"].head(50)
print("\n")
print("\n")
print("\n")
print(filtrohead2)

# 3.general 500 registros media aritmetica de los salarios
filtrohead3=fuenteDatos.describe()
print("\n")
print("\n")
print("\n")
print(filtrohead3)

# 4.datos 100,200,300,400
filtroIloc=fuenteDatos.iloc[[100,200,300,400]]
print("\n")
print("\n")
print("\n")
print(filtroIloc)

# 5. ultimos 3 empleados solo quiero ver el nombres y el salario
filtrotail=fuenteDatos.tail(3)["nombres","salario"]
print("\n")
print("\n")
print("\n")
print(filtrotail)