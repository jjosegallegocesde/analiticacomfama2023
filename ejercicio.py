import pandas as pd
#cargar  datospara poder analizarlos
#1. es declara una variable onde almaceno la fuente de datos

fuenteDatos=pd.read_csv("./empleados.csv")
#punto1 filtrar los primero 50 empleados
filtroempleado= fuenteDatos.head(50)["nombres"]
print("\n")
print(filtroempleado)


#punto2 filtrar primero  50 empleados y salario
filtrosalario= fuenteDatos.head(50)[["nombres","salario"]]
print("\n")
print(filtrosalario)



#punto3 filtar la media aritmetica de salario

filtropromedio=fuenteDatos.describe()

print("\n")
print (filtropromedio)



#punto 4 filtar las posiciones 100,200,300,400

filtroIloc= fuenteDatos.iloc[[100,200,300,400]]
print("\n")
print(filtroIloc)

#punto 5 filtar las ultimas 3 posiciones por nombre y salario solamente

print("\n")
filtronomysala=fuenteDatos.tail(3)[["nombres","salario"]]

print(filtronomysala)