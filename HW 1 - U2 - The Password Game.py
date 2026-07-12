from datetime import datetime

# INPUT
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnñopqrstuvwxyz"
digitos = "0123456789"
especiales = "!@#$%^&"
mes_actual = datetime.now().strftime("%B").lower()

valida = False

while not valida:
    password = input("Ingresa tu contraseña: ")

    # PROCESS
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_digito = False
    tiene_especial = False
    suma_digitos = 0

    for c in password:
        if c in mayusculas:
            tiene_mayuscula = True
        elif c in minusculas:
            tiene_minuscula = True
        elif c in digitos:
            tiene_digito = True
            suma_digitos = suma_digitos + int(c)
        elif c in especiales:
            tiene_especial = True

    longitud = len(password)
    divisores = 0
    for i in range(2, longitud):
        if longitud % i == 0:
            divisores = divisores + 1

    # OUTPUT
    hay_error = False

    if longitud < 8:
        print("Your password must be at least 8 characters.")
        hay_error = True

    if not tiene_mayuscula:
        print("Add at least one uppercase letter.")
        hay_error = True

    if not tiene_minuscula:
        print("Add at least one lowercase letter.")
        hay_error = True

    if not tiene_digito:
        print("Add at least one number.")
        hay_error = True

    if not tiene_especial:
        print("Add at least one special character (!@#$%^&).")
        hay_error = True

    if suma_digitos != 25:
        print("The digits in your password must add up to 25.")
        hay_error = True

    if divisores > 0 or longitud < 2:
        print("Your password length must be a prime number.")
        hay_error = True

    if mes_actual not in password:
        print("Your password must include the current month in lowercase.")
        hay_error = True

    if hay_error == False:
        valida = True
        print("¡Contraseña válida! Cumples con todas las reglas.")
    else:
        print("Intentalo de nuevo")