from Shapes import *

if __name__ == '__main__':
    
    shapeList = []

    square1 = Square(4)
    square2 = Square(8)
    square3 = Square(12)
    triangle1 = Triangle(3, 1)
    triangle2 = Triangle(6, 2)
    triangle3 = Triangle(9, 3)
    circle1 = Circle(5)
    circle2 = Circle(10)
    circle3 = Circle(15)

    shapeList.append(square1)
    shapeList.append(square2)
    shapeList.append(square3)
    shapeList.append(triangle1)
    shapeList.append(triangle2)
    shapeList.append(triangle3)
    shapeList.append(circle1)
    shapeList.append(circle2)
    shapeList.append(circle3)

    print("There are ", len(shapeList), " shapes in this \"database\"")

    # the shapes are being sorted by their name in alphabetical order
    shapeList.sort(key=lambda x: x.name, reverse=False)
    for shape in shapeList:
        shape.display()
        shape.getArea()

