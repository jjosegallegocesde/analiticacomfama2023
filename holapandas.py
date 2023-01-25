import pandas as pd

#cargar datos para poder analizar

#1. es declarar una variable donde almaceno la fuente de datos
fuenteDatos=pd.read_csv("./empleados.csv")

#print(fuenteDatos)

#2. obtener n cantidad de datos (FILTRO)
filtrohead=fuenteDatos.head()
print(filtrohead)

filtrohead2=fuenteDatos.head(60)
print("\n")
print("\n")
print("\n")
print(filtrohead2)

filtrotail=fuenteDatos.tail(30)
print("\n")
print("\n")
print("\n")
print(filtrotail)

filtroName=fuenteDatos["nombres"].head(10)
print("\n")
print("\n")
print("\n")
print(filtroName)

filtroIloc=fuenteDatos.iloc[[5,15]]
print("\n")
print("\n")
print("\n")
print(filtroIloc)