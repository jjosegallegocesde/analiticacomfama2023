import pandas as pd

#cargar datos para poderlos analizar

#1.Declarar una variable donde almeceno una fuente de datos
fuenteDatos=pd.read_csv("./empleados.csv")

#2. obtener n cantidad de datos (filtro)
filtrohead=fuenteDatos.head()
print(filtrohead)

filtrohead2=fuenteDatos.head(500)
print("\n")
print(filtrohead2)

filtrotail=fuenteDatos.tail()
print("\n")
print(filtrotail)

filtronombre=fuenteDatos["nombres"].head(10)
print("\n")
print(filtronombre)

filtroiloc=fuenteDatos.iloc[[5,15,30]]
print("\n")
print(filtroiloc)
