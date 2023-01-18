#creando diccionarios en python

persona ={
    'Nombre':"Omar Daniel",
    'Edad' : 35,
    'Estatura' : 1.72,
    'Yadesayuno' : False,
    'EquiposFavoritos' :['Nacional','RealMadrid','Boca','juventus']
}

#creando un diccionario vacio
ciudad = []

# accedamos a u diccionario
print ( persona )
print ( ciudad) 

# acceder a un solo atrivito o clave del diccionario
nombre = persona['Nombre']
print ( nombre )
print ( persona [ 'Nombre' ] )
persona [ 'Nombre' ] = ' James Rodriguez '
print ( persona [ ' Nombre ' ] )

persona ['saldoencuenta'] =0
print (persona ['saldoencuenta'])
print (persona)

# recorriendo un diccionario
for valor in  persona.values():
    print ( 'valor' )