#IMC
#IMC < 18.5 = flaco
#18.5 <= IMC < 25 = Normal
#25 <= IMC < 30 = gordito
#IMC >= 30 = Majin boo
weight = float(input("Ingresa tu peso: "))
height = float(input("Ingresa tu altura (M): "))
IMC = weight / (height*height)
if IMC < 18.5:
    print ("Desnutrido")
elif 18.5 <= IMC < 25:
    print ("Normal")
elif  25<= IMC <= 30:
    print ("Gordito")
else:
    print ("Majin boo")