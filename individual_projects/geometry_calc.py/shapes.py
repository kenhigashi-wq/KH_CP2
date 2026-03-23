#KH page shapes
#Import math
import math

#make a class for circla
class Circle:
    #initialize the class things
    def __init__(self, radius):
        self.radius = radius

    #make the function for area
    def area(self):
        return round(2 * math.pi * self.radius, 2)
        
    #make the function for perimeter
    def perimeter(self):
        return round(math.pi ** (self.radius), 2)
    
    #Display all the info        
    def display_info(self):
        print("Circle:")
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Diameter: {self.radius * 2}")

#make class for a rectangle
class Rectangle:
    #initialize th class
    def __init__(self, length, width):
        self.length = length
        self.width = width

    #make a function for the area
    def area(self):
        return round(self.length * self.width, 2)
    
    #make the funciton for the perimeter
    def perimeter(self):
        return round(2 * (self.length + self.width), 2)
    
    #make the function for displaying everybting
    def display_info(self):
        print("Rectangle")
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

#make a class for a square
class Square:
    #Initialize
    def __init__(self, side):
        self.side = side

    #make a funciton for the area
    def area(self):
        return round(self.side * self.side, 2)
    
    #make the perimeter
    def perimeter(self):
        return round(4 * self.side, 2)
    
    #display everything
    def display_info(self):
        print("Square:")
        print(f"Side: {self.side}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

#Make a class for a triangle
class Triangle:
    #make a function for initialin the things
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    #Make the function for calcing the area
    def area(self):
        return round(.5 * self.base * self.height, 2)
    
    #now one for calculaing the perimter
    def perimeter(self):
        hypotenuse = math.sqrt(self.base ** 2 + self.height ** 2)
        return round(self.base + self.height + hypotenuse, 2)
    
    #display all infos
    def display_info(self):
        print("Right Triangle")
        print(f"Base: {self.base}")
        print(f"Height: {self.height}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

