nombres = '''Agustin',
 'Alan', 
 'Andres', 
 'Ariadna', 
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabian',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'Maria',
 'MATEO',
 'Matias',
 'Nicolas',
 'NICOLAS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomas',
 'Ulises',
 'Yanina'''



eval1 = '''81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74'''



eval2 = '''30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10'''


nombres = nombres.split()
notas1 = eval1.split()
notas2 = eval2.split()

nombres = [nombre.strip(',').strip('\'') for nombre in nombres]
notas1 = [int(nota.strip(',').strip('\'')) for nota in notas1]
notas2 = [int(nota.strip(',').strip('\'')) for nota in notas2]

total = []
suma = 0
for notas1,notas2 in zip(notas1,notas2):
    total.append(sum([notas1,notas2]))
    suma += sum([notas1,notas2])
nombres_notas = list(zip(nombres,total))
print(nombres_notas)
print()

prom = suma / len(nombres)
print(f'El promedio de las notas es {prom:.2f}')
print('Los que obtuvieron menos que el promedio son:')
for i in range(len(nombres_notas)):
    if nombres_notas[i][1] < prom:
        print('- ',nombres_notas[i])