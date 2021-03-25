frase = """
Si trabajas mucho CON computadoras, eventualmente encontraras que te gustaria
automatizar alguna tarea. Por ejemplo, podrias desear realizar una busqueda y
reemplazo en un gran numero DE archivos de texto, o renombrar y reorganizar
un monton de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequena base de datos personalizada, o una aplicacion
especializada con interfaz grafica, o UN juego simple.
"""

frase = frase.split()

lista = []

for palabra in frase:
    if lista.count(palabra.lower()) == 0:
        lista.append(palabra.lower())

print(lista)