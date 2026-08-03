class ShoppingCart:
    def __init__(self):
        self.prices = []
        
    def add (self, price):
        self.prices.append(price)
    
    def total(self):
        total = 0
        for n in self.prices:
            total = total + n
        return total
    
cart = ShoppingCart()
for price in [50,30,20]:
    cart.add(price)
print(cart.total())
        
