price = 150
#Children year < 12 = 30%
#Students 12<year<25 = 205 (with id)
#adults 26-64 = no disccount
#Old persons 65 or mrore = 40% discount
age = int(input("Ingresa la edad: "))
id = input("Tiene tarjeta? (Si/No): ")
if age < 12:
    rate = .30
elif age <= 25 and id == "si":
    rate = .20
elif age <= 64 and id:
    rate = 0.00
else:
    rate = 0.40
n_price = price * (1-rate)
print(f"Price $: {n_price}")