class Triangle():
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

Triangle = Triangle(6,3)
print(Triangle.area())
