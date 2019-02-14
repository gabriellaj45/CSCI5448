class Shape:

    area = 0

    def __init__(self, area):
        self.area = area

    def getArea(self):
        return None

    def display(self):
        print(self.name)


class Circle(Shape):
    name = "I am a circle with an area of "
    radius = 0

    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return self.radius * self.radius

    def display(self):
        print(self.name, self.getArea())


class Square(Shape):
    name = "I am a square with an area of "
    width = 0      

    def __init__(self, width):
        self.width = width

    def getArea(self):
        return self.width * self.width

    def display(self):
        print(self.name, self.getArea())


class Triangle(Shape):
    name = "I am a triangle with an area of "
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return 0.5 * self.width * self.height

    def display(self):
        print(self.name, self.getArea())
