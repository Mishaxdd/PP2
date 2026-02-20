# 1
class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    pass
Dog().speak()
# 2
class Vehicle:
    def move(self):
        print("Vehicle is moving")
class Car(Vehicle):
    pass
Car().move()
# 3
class Person:
    def info(self):
        print("I am a person")
class Student(Person):
    pass
Student().info()
# 4
class Shape:
    def draw(self):
        print("Drawing shape")
class Circle(Shape):
    pass
Circle().draw()
# 5
class Device:
    def power_on(self):
        print("Device is on")
class Phone(Device):
    pass
Phone().power_on()