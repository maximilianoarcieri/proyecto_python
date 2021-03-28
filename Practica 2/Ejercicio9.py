texto = input('Ingrese una frase: ')

ok = True
for i in texto:
    if ((texto.count(i) > 1) and (i != ' ')):
        ok = False
        break

print('Es un heterograma') if ok else print('No es heterograma')