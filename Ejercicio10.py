'''Tablas de valores de cada letra'''
tabla = {'A','E','I','O','U','L','N','R','S','T'}
tabla2 = {'D','G'}
tabla3 = {'B','C','M','P'}
tabla4 = {'F','H','V','W','Y'}
tabla5 = {'K'}
tabla6 = {'J','X'}
tabla7 = {'Q','Z'}

'''Actualizo para tener solo una tabla'''
tabla = dict.fromkeys(tabla,1)
tabla.update(dict.fromkeys(tabla2,2))
tabla.update(dict.fromkeys(tabla3,3))
tabla.update(dict.fromkeys(tabla4,4))
tabla.update(dict.fromkeys(tabla5,5))
tabla.update(dict.fromkeys(tabla6,8))
tabla.update(dict.fromkeys(tabla7,10))

'''Comprobar valores de la tabla'''
#for i in tabla:
#    print(f"{i}: {tabla.get(i)}")

palabra = input('Ingrese una palabra: ')
valor = 0
'''Para cada letra se busca su valor en la tabla y se suma a la variable'''
for letra in palabra:
    valor = valor + tabla.get(letra.upper())
print(f"El valor de '{palabra}' es de {valor} puntos")