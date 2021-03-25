texto = "Esta es una oracion que escribi para comprobar el funcionamiento del Ejercicio 3 de la Practica 2"
texto = texto.split(' ')


car = input('Ingrese una letra (# para terminar): ')
while car != '#':
    if car == -1:
        break
    else:
        if car.isalpha():
            for i in texto:
                if i.startswith(car):
                    print(i)
        else:
            print('No se ingreso una letra')
    print('-----------------------')
    car = input('Ingrese una letra (# para terminar): ')