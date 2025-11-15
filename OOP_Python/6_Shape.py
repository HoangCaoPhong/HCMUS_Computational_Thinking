class Shape:
    #@abstractmethod
    def area():
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

shapes = [Circle(3), Rectangle(1,2)]

total_area = sum(shape.area() for shape in shapes)

print(f"Total Area: {round(total_area, 2)}")