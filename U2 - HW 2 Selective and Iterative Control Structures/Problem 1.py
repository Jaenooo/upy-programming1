#Grade Averaging System
#INPUT
digitos = "0123456789"
suma = 0
total = 0
terminado = False

# PROCESS
while not terminado:
    g = input("Enter the grade of the student (or 'done' to finish): ")

    if g == "done":
        terminado = True
    else:
        es_numero = True
        for c in g:
            if c not in digitos:
                es_numero = False

        if not es_numero:
            print("Not a valid entry")
        else:
            g = int(g)
            if g < 0 or g > 100:
                print("Not a valid grade please try it later")
            else:
                suma = suma + g
                total = total + 1
# OUTPUT
if total == 0:
    print("No grades entered, please enter at least one grade")
else:
    promedio = suma / total
    if promedio >= 7.0:
        print(f"Average: {promedio:} Passed")
    else:
        print(f"Average: {promedio:} Failed")