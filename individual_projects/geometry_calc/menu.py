#KH function
#Import needed functions
from shapes import Circle, Rectangle, Square, Triangle
from helper import ShapeManager

#make a function for getting the input, make idiot proof in here too
def get_number(text):
    while True:
        try:
            n = float(input(text))
            if n > 0:
                return n
            else:
                print("Enter a positive number")
        except:
            print("Invalid, try again")

def create_shape(manager):
    print("\nChoose a shape type")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Triangle")

    choice = input("Enter choice: ")

    if choice == "1":
        r = get_number("Radius: ")
        manager.add_shape(Circle(r))

    elif choice == "2":
        l = get_number("Length: ")
        w = get_number("Width: ")
        manager.add_shape(Rectangle(l, w))

    elif choice == "3":
        s = get_number("Side: ")
        manager.add_shape(Square(s))

    elif choice == "4":
        b = get_number("Base: ")
        h = get_number("Height: ")
        manager.add_shape(Triangle(b, h))

    else:
        print("Invalid Choice")

def menu():
    manager = ShapeManager()

    while True:
        print("Geometry Calculator")
        print("")
        print(f"Shapes Created: {len(manager.shapes)}")

        print("1. Create New Shape")
        print("2. View All Shapes")
        print("3. Select Shape")
        print("4. Compare Shapes")
        print("5. Sort Shapes")
        print("6. Formula Guide")
        print("7. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_shape(manager)

        elif choice == "2":
            manager.list_shapes()

        elif choice == "3":
            manager.list_shapes()
            num = int(get_number("Enter shape #:"))
            shape = manager.get(num)
            if shape:
                print("")
                shape[1].display_info()


        elif choice == "4":
            manager.list_shapes()
            num_1 = int(get_number("First Shape #: "))
            num_2 = int(get_number("Second Shape #: "))
            s1 = manager.get(num_1)
            s2 = manager.get(num_2)
            if s1 and s2:
                manager.compare(s1, s2)

        elif choice == "5":
            print("Sort by: ")
            print("1. Area")
            print("2. Perimeter")
            c = input("Enter choice: ")
            if c == "1":
                manager.sort("area")
            else:
                manager.sort("perimeter")

        elif choice == "6":
            Circle.formula_guide()
            Rectangle.formula_guide()
            Square.formula_guide()
            Triangle.formula_guide()
            
        elif choice == "7":
            print("Goodbye")
            break

        else:
            print("Invalid")


