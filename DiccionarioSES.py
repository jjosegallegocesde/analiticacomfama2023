#Crear diccionarios en python
persona = {
    'nombre': 'Sebastian',
    'edad': 21,
    'estatura': 1.95,
    'peso': 66,
    'yaDesayuno': False,
}

#Crear diccionario vació
ciudad = {}

#accedamos a un diccionario
print(list(persona.values()))
print(ciudad)

#recorriendo un diccionario
for valor in persona.values():
    print(valor)