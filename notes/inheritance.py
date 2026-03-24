# Inheritance

# Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Vroooom!")

# Child
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Chhaaaaaaaa!")

class Plane(Vehicle):
    def move(self):
        print("Swoosh!")

car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Airbus", "Vi 400")

for x in (car, boat, plane):
    print(x.brand)
    print(x.model)
    x.move()