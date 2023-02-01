import pandas as pd

#cargar datos para poderlos analizar
#1.declarar una variable donde almaceno la fuente de datos
fuenteDatos = pd.read_csv("./empleados.csv")

empleados50 = fuenteDatos.nombres.head(50)
print(empleados50)
print("\n")

empleadosSalarios = fuenteDatos.salario.head(50)
print(empleadosSalarios)
print("\n")

seleccionarDatos = fuenteDatos.iloc[[100,200,300,400]]
print(seleccionarDatos)
print("\n")

mediaSalarios = fuenteDatos.salario.mean()
print(mediaSalarios)
print("\n")

seleccionardatos2 = fuenteDatos[["salario", "nombres"]].tail(3)
print(seleccionardatos2)
print('')

print(fuenteDatos.describe())
print('')

