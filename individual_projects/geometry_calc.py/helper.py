class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.counter = 1

    def add_shape(self, shape):
        label = f"{shape.__class__.__name__} #{self.counter}"
        self.shapes.append((label, shape))
        self.counter += 1
        print(f"\nCreated {label}")

    def list_shapes(self):
        if len(self.shapes) == 0:
            print("\nNo shapes created yet")

        print("\nShapes:")
        for i, (label, shape) in enumerate(self.shapes, start=1):
            print(f"{i}. {label}, Area {shape.area()}, Perimeter: {shape.perimeter()}")

    def get(self, index):
        if 1 <= index <= len(self.shapes):
            return self.shapes[index - 1]
        else:
            print("Invalid shape #")
            return None
        
    def compare(self, s1, s2):
        label1, shape1 = s1
        label2, shape2 = s2

        print("area comparison:")
        if shape1.area() > shape2.area():
            print(label1, "has a larger area")
        elif shape1.area() < shape2.area():
            print(label2, "Has a larger area")
        else:
            print("Areas are equal")

        print("Perimeter Comparison")
        if shape1.perimeter() > shape2.perimeter():
            print(label1, "has a larger perimeter")
        elif shape1.perimeter() < shape2.perimeter():
            print(label2, "Has a larger perimeter")
        else:
            print("Perimeters are equal")

    def sort(self, mode):
        if mode == "area":
            self.shapes.sort(key=lambda s: s[1].area())
        else:
            self.shapes.sort(key=lambda s: s[1].perimeter())
            
        print("Shapes sorted")