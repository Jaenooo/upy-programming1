#Shipping cost calculator
number = "0123456789"
finish = False
total_acumulado = 0
while not finish:
    peso_texto = input("Enter weight in kg or exit to finish: ")
    if peso_texto == "exit":
        finish = True
    else:
        distancia_texto = input("Enter distance in km: ")
        peso_valido = True
        for c in peso_texto:
            if c not in number:
                peso_valido = False   
        distancia_valida = True
        for c in distancia_texto:
            if c not in number:
                distancia_valida = False
        if not peso_valido or not distancia_valida:
            print("Not a valid entry")
        else:
            peso = int(peso_texto)
            distancia = int(distancia_texto)
            if distancia <= 100:
                if peso <= 5:
                    costo = 50.00
                else:
                    costo = 80.00
            else:
                if peso <= 5:
                    costo = 120.00
                else:
                    costo = 200.00
            total_acumulado = total_acumulado + costo
            print(f"Shipping cost: ${costo:} MXN")
print(f"Total: ${total_acumulado:} MXN")