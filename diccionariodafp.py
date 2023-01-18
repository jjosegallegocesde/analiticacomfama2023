#creando diccionario en python

persona={
    'nombre':"Daniela",
    'edad':21,
    'estatura':1.62,
    'yadesayuno':True,
    'equiposFavoritos':['nacional','liverpool','olimpiakos','CR7']
}

#creando un diccionario vacio
cuidad={}


#accedamos a un diccionario
print(persona)
print(cuidad)

#acceder a u solo atributo o clave del diccionario
nombre=persona['nombre']
print(nombre)

print(persona['nombre'])

persona['nombre']="carlos"
print(persona['nombre'])

persona["saldoEncuenta"]=0
print(persona["saldoEncuenta"])
print(persona)

#Recorriendo un diccionario
for Valor in persona.values():
    print(Valor)