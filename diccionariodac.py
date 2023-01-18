#creando diccinarios en python

persona={
    'nombre':"daniela",
    'edad':28,
    'estatura': 1.64,
    'yadesayuno':True,
    'equipoFavorito':['medellin','argentina']
}

#creando un diccionario vacio

ciudad={}

#acceder a un diccionario

print(persona)
print(ciudad)

#accesder a un solo atributo o clave del diccionario
#aca nombramos una variable en este caso nombre= al nombre del diccionario y en el print llamamos a la variable
nombre=persona["nombre"]
print(nombre)
#o tambien se puede directamente ahorrando una línea
print(persona["nombre"])

#para hacer cambios a un valor es

persona["nombre"]="DANIELA"
print(persona["nombre"])

#aca le asignamos un nuevo atributo con su valor

persona["saldoEnCuenta"]=0
print(persona["saldoEnCuenta"])

#aca miramos cuantos atributos tenemos o llaves
print(persona)

#Recorriendo un diccionario, valor es una variable
for valor in persona.values():
    print(valor)
