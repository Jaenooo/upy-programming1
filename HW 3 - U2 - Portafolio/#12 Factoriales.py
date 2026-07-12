#12 Factoriales
n = int(input("Ingresa un numero: "))
total = 1
i = 1
while (i <= n):
    total = total * i
    i = i+1
print("Factorial:", total)
    