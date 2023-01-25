import pandas as pd

#cargar datos para poderlos analizar

#1 declarar una variable donde almaceno la fuente de datos
fuentedatos=pd.read_csv("./empleados.csv")

#2 vamos a obtener n cantidad de datos (FILTRO)
filtrohead=fuentedatos.head()
print(filtrohead)

filtrohead2=fuentedatos.head(15)
print("\n")
print(filtrohead2)

filtrotail=fuentedatos.tail()
print("\n")
print(filtrotail)

filtronombre=fuentedatos["nombres"].head(10)
print("\n")
print(filtronombre)

filtroiloc=fuentedatos.iloc[[5,15]]
print("\n")
print(filtroiloc)