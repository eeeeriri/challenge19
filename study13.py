#1
class Rectangle:#長方形
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_perimeter(self):
        return self.base * 2 + self.height * 2 

class Square:#正方形
    def __init__(self, base):
        self.base = base

    def calculate_perimeter(self):
        return self.base * 4 

rectangle = Rectangle(3,5)#16
print(rectangle.calculate_perimeter())

square = Square(5)#20
print(square.calculate_perimeter())

#2 #1のSquareにchange_sizeメソッド追加
class Square:
    def __init__(self, base):
        self.base = base#5

    def calculate_perimeter(self):
        return self.base * 4

    def change_size(self, add):#change_sizeに増減したい値を渡す
        self.base += add

square = Square(5)
square.change_size(7)

print(square.base)
print(square.calculate_perimeter())
#3
class Shape:
    def what_am_i(self):
        print("I am a Shape")

shape = Shape()
shape.what_am_i()

class Rectangle(Shape):
    pass

class Square(Shape):
    pass
    
rectangle = Rectangle()
rectangle.what_am_i()

square = Square()
square.what_am_i()

#4
class Horse:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

ando = Rider("Ando Katsumi")
oguri = Horse("Oguri Cap", "Thoroughbred", ando)
print(oguri.owner.name)
