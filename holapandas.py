import pandas as pd 

#cargar datos para poderlos analizar 

#1. declarar una variable donde almaceno la fuente de datos
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

filtroNombre=fuenteDatos["nombres"].head(10)
print("\n")
print(filtroNombre)

filtroIloc=fuenteDatos.iloc[[5,15,30]]
print("\n")
print(filtroIloc)


#1. priemros 50 empleados
filtrohead3=fuenteDatos.head(50)
print("\n")
print(filtrohead3)

filtroNomEmpleados=fuenteDatos.head(50)["salario"]
print("\n")
print(filtroNomEmpleados)

filtroMedia=fuenteDatos.describe()
print("\n")
print(filtroMedia)

filtroIloc=fuenteDatos.iloc[[100,200,300,400]]
print("\n")
print(filtroIloc)

filtrotail=fuenteDatos.tail(3)[["salario","nombres"]]
print("\n")
print(filtrotail)