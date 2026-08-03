class Thermostat:
    def __init__(self, temperature):
        self.temperature = temperature
    
    def check(self):
        if self.temperature < 20:
            return "Heating"
        elif self.temperature > 25:
            return "Cooling"
        else:
            return "Ok"

print(Thermostat(40).check())