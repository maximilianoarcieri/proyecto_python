tabla = {'A','E','I','O','U','L','N','R','S','T'}
tabla2 = {'D','G'}
tabla3 = {'B','C','M','P'}
tabla4 = {'F','H','V','W','Y'}
tabla5 = {'K'}
tabla6 = {'J','X'}
tabla7 = {'Q','Z'}

tabla = dict.fromkeys(tabla,1)
tabla2 = dict.fromkeys(tabla2,2)
tabla3 = dict.fromkeys(tabla3,3)
tabla4 = dict.fromkeys(tabla4,4)
tabla5 = dict.fromkeys(tabla5,5)
tabla6 = dict.fromkeys(tabla6,8)
tabla7 = dict.fromkeys(tabla7,10)

tabla.update(tabla2)
tabla.update(tabla3)
tabla.update(tabla4)
tabla.update(tabla5)
tabla.update(tabla6)
tabla.update(tabla7)

palabra = input('Ingrese una palabra: ')

valor = 0
for letra in palabra:
    valor = valor + tabla.get(letra.upper())

print(f"El valor de '{palabra}' es de {valor} puntos")