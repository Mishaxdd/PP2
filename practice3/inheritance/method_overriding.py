# 1
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

Dog().speak()

# 2
class Vehicle:
    def move(self):
        print("Vehicle moves")

class Bike(Vehicle):
    def move(self):
        print("Bike rides")

Bike().move()

# 3
class Employee:
    def work(self):
        print("Employee working")

class Developer(Employee):
    def work(self):
        print("Developer coding")

Developer().work()

# 4
class Shape:
    def draw(self):
        print("Drawing shape")

class Triangle(Shape):
    def draw(self):
        print("Drawing triangle")

Triangle().draw()

# 5
class Bird:
    def fly(self):
        print("Bird flying")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

Penguin().fly()