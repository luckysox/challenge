class Square:
    square_list =[]

    def __init__(self,s1):
        self.s1 = s1
        self.square_list.append(self.s1)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1,self.s1,self.s1,self.s1)

a_square = Square(29)
print(a_square)
