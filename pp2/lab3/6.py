class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

data = list(map(int, input().split()))

if len(data) >= 2:
    l = data[0]
    w = data[1]
    r = Rectangle(l, w)
    print(r.area())