#creando diccionarios en python
persona={
    'nombre': "thomas alberto",
    'edad': "18",
    'estatura': "1.76",
    'yaDesayuno':True,
    'equiposFavoritos':['nacional','liverpool','barcelona',]
}

#creando un diccionario vacio
ciudad={}

#accediendo a un diccionario
print(persona)
print(ciudad)

#acceder a un solo atributo o clave del diccipnario
nombre=persona["nombre"]
print (nombre)
print(persona["nombre"])

persona["nombre"]="leo messi"
print(persona["nombre"])
print(persona)

persona["saldoEnCuenta"]=0
print(persona["saldoEnCuenta"])
print(persona)

#recorriendo un diccionario

for valor in persona.values():
    print(valor)


