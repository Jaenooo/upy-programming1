#8 Estado del agua en base a la temperatura en celcius
n=int(input("Ingresa la temperatura: "))
if n <=0:
    print ("El agua esta en estado solido (Hielo)")
elif 0 < n < 100:
    print ("El agua esta en estado liquido (Agua)")
elif  n >= 100:
    print ("El agua esta en estado gaseoso (Nubes/gas)")