#creando diccionarios en python
persona={
    'nombre':'juan gabriel',
    'edad':19, 
    'estatura':1.65,
    'yaDesayuno':True,
    'equiposFavoritos':['Deportivo Independiente Medellin','Real Madrid','Arsenal','1k']
}

#creando un diccionario vacio
ciudad={}

#accedamos a un diccionario
print(persona)
print(ciudad) 

#acceder a un solo atributo o clave del diccionario
nombre=persona['equiposFavoritos']
print(nombre)

print(persona['equiposFavoritos'])

persona['nombre']='cristiano ronaldo'
print(persona['nombre'])

persona['saldocuenta']=1000000
print(persona['saldocuenta'])
print(persona)

#recorriendo un diccionario
for valor in persona.values():
        print(valor)