import requests
import csv


def evaluar(lista_lenguajes):
    return ("ES" in lista_lenguajes)


ruta = "C:\\Users\\maxip\\Documents\\Archivos\\appstore_games.csv"

file = open(ruta,"r")
csvreader = csv.reader(file,delimiter=',')
cabecera = next(csvreader)


best_raiting = []

print("Los juegos gratuitos y en español son:")
for linea in csvreader:
    if linea[7] == "0" and evaluar(linea[12]):
        print(f"-- Nombre: {linea[2]}")

    if (linea[6] != ""):
        best_raiting.append([linea[2],linea[6]])
file.close()


print("-"*60)
print("Los 10 juegos mejor valorados son:")
best_raiting_top = sorted(best_raiting, key = lambda puntos: puntos[1], reverse = True)

for i in range(10):
    juego = best_raiting_top[i]
    print(f"-- Nombre: {juego[0]} - Puntaje: {juego[1]}")
