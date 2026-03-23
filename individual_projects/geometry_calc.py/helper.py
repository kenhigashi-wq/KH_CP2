#Make a class for managing shapes
class ShapeManager:
    #initialize vars and stuff
    def __init__(self):
        self.shapes = []
        self.counter = 1
    
    #Make a funciton for adding the shape into the user portfolio
    def add_shape(self, shape):
        label = f"{shape.__class__.__name__} #{self.counter}"
        self.shapes.append((label, shape))
        self.counter += 1
        print(f"\nCreated {label}")

    #Make a function for the stuff in the list
    def list_shapes(self):
        if len(self.shapes) == 0:
            print("\nNo shapes created yet")

        print("\nShapes:")
        for i, (label, shape) in enumerate(self.shapes, start=1):
            print(f"{i}. {label}, Area {shape.area()}, Perimeter: {shape.perimeter()}")

    #make a funciton for getting the index stuff
    def get(self, index):
        #if the index is more than 1 and less then the lenght of the shape
        if 1 <= index <= len(self.shapes):
            #return the shape, minus 1 for accurate listing
            return self.shapes[index - 1]
        #Else, say invalid
        else:
            print("Invalid shape #")
            return None
        
    #Make a funciton for comparing the stuff
    def compare(self, s1, s2):
        label1, shape1 = s1
        label2, shape2 = s2

    #Compare the area of the shapes
        print("area comparison:")
        if shape1.area() > shape2.area():
            print(label1, "has a larger area")
        elif shape1.area() < shape2.area():
            print(label2, "Has a larger area")
        else:
            print("Areas are equal")

        #compare the shapes perimeter
        print("Perimeter Comparison")
        if shape1.perimeter() > shape2.perimeter():
            print(label1, "has a larger perimeter")
        elif shape1.perimeter() < shape2.perimeter():
            print(label2, "Has a larger perimeter")
        else:
            print("Perimeters are equal")

    #simple function for sorting
    def sort(self, mode):
        if mode == "area":
            self.shapes.sort(key=lambda s: s[1].area())
        else:
            self.shapes.sort(key=lambda s: s[1].perimeter())
            
        print("Shapes sorted")