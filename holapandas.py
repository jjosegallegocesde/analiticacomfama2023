import pandas as pd

#cargar datos para poderlos analizar

#1. Declarar una variable donde almaceno la fuente de datos
fuenteDatos=pd.read_csv("./empleados.csv")

#2. obtener N cantidad de datos (FILTRO)
filtrohead=fuenteDatos.head()
print(filtrohead)

filtrohead2=fuenteDatos.head(15)
print("\n")
print(filtrohead2)

filtrotail=fuenteDatos.tail(30)
print("\n")
print(filtrotail)

filtroNombre=fuenteDatos.head(10)["nombres"]
print("\n")
print(filtroNombre)

filtroIloc=fuenteDatos.iloc[[5,15,30]]
print("\n")
print(filtroIloc)



