import pandas as pd

#cargar datos para poderlos analizar
#1.declarar una variable donde almaceno la fuente de datos
fuenteDatos = pd.read_csv("./empleados.csv")
print(type(fuenteDatos))
#2.vamos a obtener N cantidad de datos (FILTRO)
filtroHead = fuenteDatos.head(20)
print(filtroHead)
filtradoTail = fuenteDatos.tail(20)
print("\n")
print(filtradoTail)

filtroNombre = fuenteDatos.nombres.head(20)
print("\n")
print(filtroNombre)

filtroIloc = fuenteDatos.iloc[5:10,0:3]
print("\n")
print(filtroIloc)

filtroIloc2 = fuenteDatos.iloc[[5,15,30]]
print("\n")
print(filtroIloc2)