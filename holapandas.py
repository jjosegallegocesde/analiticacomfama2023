import pandas as pd

#cargar datos para poder analizarlos

# 1 declarar una variable donde almaceno la fuente de datos
fuenteDedatos = pd.read_csv ("./empleados.csv")

# 2 obtener N cantidad de datos (Filtro)

filtrohead = fuenteDedatos.head()
print ( filtrohead)

filtrohead2 = fuenteDedatos.head(15)
print ('/n')
print ( filtrohead2)

filtrotail=fuenteDedatos.tail()
print ('/n')
print ( filtrotail) 

filtroNombre = fuenteDedatos['nombres'].head(25)
print ('/n')
print ( filtroNombre)

filtroIloc = fuenteDedatos.iloc[[5,15,]]
print ('/n')
print ( filtroIloc)
