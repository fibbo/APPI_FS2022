import math

class Shape:
    def area(self):
        print("Shape base class, area not implemented")
    
    def circumference(self):
        print("Shape base class, circumference not implemented")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    def circumference(self):
        return 2 * (self.width + self.height)


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def circumference(self):
        return 4 * self.side_length

list_of_shapes = [Circle(2.3), Rectangle(1, 2), Circle(12), Rectangle(3, 4), Square(3)]

for apple in list_of_shapes:
    print(f"The area is {apple.area()}")
    print(f"The circumference is {apple.circumference()}")

