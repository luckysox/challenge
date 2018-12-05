class Square():
    def __init__(self,s1):
        self.s1 = s1

    def change_size(self,new_size):
        self.s1 += new_size
    def calculate_perimeter(self):
        return self.s1 * 4

a_square = Square(35)
print(a_square.s1)

a_square.change_size(45)
print(a_square.s1)
