#Water Bill Calculator
#Input
number = "0123456789"
finish = False
total_acumulado = 0
#procces
while not finish:
    m3_texto = input("Enter m3 consumed or exit to finish: ")    
    if m3_texto == "exit":
        finish = True
    else:
        es_numero = True
        for c in m3_texto:
            if c not in number:
                es_numero = False
        if not es_numero:
            print("Not a valid entry")
        else:
            m3 = int(m3_texto)
            if m3 <= 10:
                cargo = m3 * 8.00   
            elif m3 <= 20:
                cargo = m3 * 12.00   
            else:
                cargo = m3 * 18.00
#Output
            total_acumulado = total_acumulado + cargo
            print(f"Month charge: ${cargo:.2f} MXN")
print(f"Total: ${total_acumulado:.2f} MXN")