#1
class Apple:
    def __init__(self, weight, color, size, area):
        self.weight = weight
        self.color = color
        self.size = size
        self.area = area
    print("Created!")
apple = Apple(12,"青","S","aomori")
print(apple.color)

#2 
import math
class Circle:
    def __init__(self,radius, en):
        self.radius = radius
        self.en = en

    #面積の計算
    def area(self):
        return self.radius * self.radius * math.pi

    def enshu(self):
        return self.en * math.pi * 2

circle = Circle(3,5)
print(circle.area())
print(circle.enshu())


#3
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base * self.height) / 2

print(Triangle(5,12).area())

#4
class Hexagon:
    def __init__(self, Neighborhood):
        self.Neighborhood = Neighborhood
    
    def calculate_perimeter(self):
        return self.Neighborhood * 6

print(Hexagon(10).calculate_perimeter())
