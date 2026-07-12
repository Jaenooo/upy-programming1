#11 Suma de numeros N
n = int(input("Ingresa hasta donde quieres sumar: "))
suma = 0
while n>0:
    suma=suma+n
    n=n-1
print ("La suma de ese intervalo de numeros es: ", suma)