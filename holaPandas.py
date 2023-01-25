import pandas as pd

#cargar datos para poderlos analizar

#1. cargar una variable donde almaceno la fuente de datos

fuentedeDatos= pd.read_csv("./empleados.csv")

#2. obtener N cantidad e datos (FILTRO)


filtroHead=fuentedeDatos.head()
print(filtroHead)

filtroHead2=fuentedeDatos.head(15)
print("\n")
print(filtroHead2)

filtrotail=fuentedeDatos.tail(30)

print("\n")
print(filtrotail)

filtroNombre=fuentedeDatos["nombres"].head(10)
print("\n")
print(filtroNombre)

filtroIloc=fuentedeDatos.iloc[[5,15,50,90,400]]

print("\n")
print(filtroIloc)