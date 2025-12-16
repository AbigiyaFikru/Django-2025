class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def info(self):
        return f"{self.brand} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    
    def info(self):  
        return f"{self.brand} {self.model} ({self.year})"


vehicle = Vehicle("Generic", 2020)
car = Car("Toyota", 2022, "Camry")

print(f"Vehicle: {vehicle.info()}")
print(f"Car: {car.info()}")