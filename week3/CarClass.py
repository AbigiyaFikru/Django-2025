class Car:
    def __init__(self, make):
        self.make = make
    
    def get_make(self):
        return self.make

# Test the class
car = Car("Toyota")
print(f"Car make: {car.get_make()}")