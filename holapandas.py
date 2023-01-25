import pandas as pd
#cargar  datospara poder analizarlos
#1. es declara una variable onde almaceno la fuente de datos

fuenteDatos=pd.read_csv("./empleados.csv")

#2. obtener N cantidad de datos  (FILTRO)
#filtrohead= fuenteDatos.head(acá va la canidad de datos que necesito ver) o filtrohead= fuenteDatos.head() = me muestra los 5 primeros por defecto

filtrohead= fuenteDatos.head()
print(filtrohead)

filtrohead2= fuenteDatos.head(15)
print("\n")
print(filtrohead2)

#este es para ver los ultimos 5 filtrotail= fuenteDatos.tail() o filtrotail= fuenteDatos.tail(acá va la cantidad que necesito ver)

filtrotail= fuenteDatos.tail()
print("\n")
print(filtrotail)

#este sirve para flitar datos filtronombre=fuenteDatos.head(acá va la cantidad que quiero que me muestre)["acá va el atributo"]

filtronombre=fuenteDatos.head(15)["nombres"]
print("\n")
print(filtronombre)

#este es para obtener rangos filtroIloc= fuenteDatos.iloc[5:15]
filtroIloc= fuenteDatos.iloc[5:15]
print("\n")
print(filtroIloc)

#este es para obtener datos especifico  filtroIloc= fuenteDatos.iloc[[5,15,20]]

filtroIloc= fuenteDatos.iloc[[5,15,20]]
print("\n")
print(filtroIloc)