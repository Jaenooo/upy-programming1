#15 primer multiplos de 7 entre 1 ramgo/break y continues/
#Ingresa dos numeros, A y B, %/, break para parar el codigo

a = int(input("Ingresa un numero para el rango: "))
b = int(input("Ingresa un numero para el rango de finalizacion:" ))
for n in range(a,b+1):
    if n%7==0:
        print ("Primer multiplo de 7:", n)
        break