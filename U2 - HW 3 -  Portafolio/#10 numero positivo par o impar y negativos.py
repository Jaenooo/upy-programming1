#10 numero positivo par o impar y negativos
n=int(input("Ingresa un numero: "))
if n<0:
    print ("Es negativo")
elif n==0:
    print ("es cero")
elif n>0:
    print ("Es positivo")
    if n%2==0:
        print ("Es par")
    else:
        print ("Es impar")
    