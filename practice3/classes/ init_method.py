# 1
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.name)
# 2
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

l = Laptop("HP", 1200)
print(l.brand, l.price)
# 3
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

r = Rectangle(5, 10)
print(r.width * r.height)
# 4
class User:
    def __init__(self, username):
        self.username = username

u = User("admin")
print(u.username)
# 5
class Animal:
    def __init__(self, species):
        self.species = species

a = Animal("Cat")
print(a.species)
