import pandas as pd
#Cargar datos para poder analizar
#1. declarar variable donde almacenar la fuente de datos
fuenteDatos=pd.read_csv("./empleados.csv")
print(type(fuenteDatos))
#Obtener N cantidad de datos (Filtro)
#ver primeros registros
filtrohead=fuenteDatos.head()
print (filtrohead)
print("\n")
#ver una cantidad de registros en el inicio
filtrohead2=fuenteDatos.head(15)
print ("\n")
print(filtrohead2)
print("\n")
#ver ultimos 5 registros
filtrotail=fuenteDatos.tail()
print (filtrotail)
print("\n")
#ver ultimos registros dependiendo el numero seleccionado
filtrotail2=fuenteDatos.tail(30)
print(filtrotail2)
print("\n")


#acceder a un solo atributo o clave del diccionario

filtroNombre=fuenteDatos.head(10)["nombres"]
print(filtroNombre)
print("\n")

#Filtros por filas

filtroIloc=fuenteDatos.iloc[[5,15]]
print(filtroIloc)
print("\n")