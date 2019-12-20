#1
class Square:
    square_list = []
    def __init__(self, base):
        self.base = base
        self.square_list.append((self.base))

    def calculate_perimeter(self):
        return self.base * 4

    def change_size(self, add):#change_sizeに増減したい値を渡す
        self.base += add

square = Square(5)
square.change_size(7)

print(square.base)
print(square.calculate_perimeter())

square = Square(4)
square = Square(6)
square = Square(10)

print(square.square_list)


#2
class Square:
    def __init__(self, base):
        self.base = base

    def change_size(self):
        print("{} by {} by {} by {}".format(self.base, self.base, self.base, self.base))

square = Square(29)
print(square.change_size())

#3
#二つのパラメーターを受けとる関数
def param(x,y):
    if x is y:
        print("True")
    else:
        print("False")

param(2,3)