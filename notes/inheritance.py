# Inheritance
#adsdabfubgiuabgv
# Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Vroooom!")

#
# Child
#Compisition
class Engine:
    def __init__(self, model):
        self.cylinders = model

    def __str__(self):
        return self.model

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.engine = Engine("v8")

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

print(car.engine)

#Aggregate Classes
class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog

    def add_book(self, book):
        self.catalog.append(book)

    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("Invalid")

    def view_catalog(self):
        for book in self.catalog:
            print(book)

    
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
lib = Library("Provo Libary")

lib.add_book(Book("The way of kings", "Brandon Sanderson"))
lib.add_book(Book("Test_book", "Test_author"))
lib.add_book(Book("The last Battle", "C.S Lewis"))

lib.view_catalog()

