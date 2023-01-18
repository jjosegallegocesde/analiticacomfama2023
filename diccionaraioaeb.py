#creando diccionarios en python

persona = {
    'nombre':"Anderson Echavarria",
    'edad': 25,
    'estatura':1.68,
    'yaDesayuno':True,
    'equiposFavoritos':['nacional','liverpool','psg']
}
#creando un diccionaro vacio
ciudad={}

#accedamos a un diccionario
print(persona)
print(ciudad)

#acceder a un dolo atributo o key del diccionario
nombre=persona["nombre"]
print(nombre)
print(persona["nombre"])

persona["nombre"]= "James Rodriguez"
print (persona["nombre"])
print (persona)

persona["saldoEnCuenta"]=0
print(persona["saldoEnCuenta"])
print(persona)

#recorriendo un diccionario

for value in persona.values():
    print(value)
