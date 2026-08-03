#7 listas de compra de una tienda (name y age)
#loop, se entregan como tuplas
#persona > 20. su edad y nombre
records = [("Karla", 20),("Juan", 18),("Sofia",40),("Francisco",22)]
for name,age in records:
    if age >= 20:
        print(name)