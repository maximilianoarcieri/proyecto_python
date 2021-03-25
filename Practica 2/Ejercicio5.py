frase = input('Ingrese la frase: ')
frase = frase.split(' ')

palabra = input('Ingrese la palabra: ')
palabra = palabra.lower()

cant = 0
for i in frase:
    print(i.lower())
    if i.lower().strip(',') == palabra:
        cant = cant + 1

print(f"La palabra '{palabra}' se repite {cant} veces")