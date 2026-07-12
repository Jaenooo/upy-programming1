#Season classifier
number = "0123456789"
finish = False
while not finish:
    mes_texto = input("Enter month number or exit to finish: ")
    if mes_texto == "exit":
        finish = True
    else:
        es_numero = True
        for c in mes_texto:
            if c not in number:
                es_numero = False
        if not es_numero:
            print("Not a valid entry")
        else:
            mes = int(mes_texto)
            if mes < 1 or mes > 12:
                print("Invalid month. Please enter a number between 1 and 12.")
            elif mes == 12 or mes == 1 or mes == 2:
                print("Winter")
            elif mes >= 3 and mes <= 5:
                print("Spring")
            elif mes >= 6 and mes <= 8:
                print("Summer")
            else:
                print("Fall")