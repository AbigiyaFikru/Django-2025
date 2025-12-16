class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")


animal = Animal()
cat = Cat()

animal.make_sound()
cat.make_sound()