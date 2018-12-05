class Hexagon():
    def __init__(self,sides):
        self.sides = sides

    def calculate_perimeter(self):
        return self.sides * 6

Hexagon = Hexagon(13)
print(Hexagon.calculate_perimeter())
