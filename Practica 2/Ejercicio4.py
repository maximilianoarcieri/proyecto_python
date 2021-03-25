cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")


if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
cant = 0

for i in cadena:
    if "@" == i or "!" == i:
        cant = cant + 1


if cant >= 1:
    print(f"Ingresaste {cant} de estos símbolos: @ o !" )
else:
    print("Ingreso OK")
