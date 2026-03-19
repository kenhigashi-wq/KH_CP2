#

#E.G
class Dog:
    def __init__(self, name, breeds, age):
        self.name = name.capitalize()
        self.breed = breeds.title()
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}\nBreed: {self.breed}\nAge: {self.age}\n"
    
    def speak(self):
        return f"{self.name}: Bark"

doug = Dog("Doug", "Golden Retriever", 3)
pongo = Dog("Pongo", "Dalmation", 8)

print(doug)
print(pongo)
print(doug.speak())
