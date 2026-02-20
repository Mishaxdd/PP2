# 1
class A:
    def method_a(self):
        print("From A")

class B:
    def method_b(self):
        print("From B")

class C(A, B):
    pass

c = C()
c.method_a()
c.method_b()

# 2
class Father:
    def skills(self):
        print("Driving")

class Mother:
    def talents(self):
        print("Cooking")

class Child(Father, Mother):
    pass

Child().skills()
Child().talents()

# 3
class Writer:
    def write(self):
        print("Writing")

class Speaker:
    def speak(self):
        print("Speaking")

class Author(Writer, Speaker):
    pass

a = Author()
a.write()
a.speak()

# 4
class Flyable:
    def fly(self):
        print("Can fly")

class Swimmable:
    def swim(self):
        print("Can swim")

class Duck(Flyable, Swimmable):
    pass

d = Duck()
d.fly()
d.swim()

# 5
class Engine:
    def start(self):
        print("Engine started")

class Radio:
    def play(self):
        print("Radio playing")

class Car(Engine, Radio):
    pass

car = Car()
car.start()
car.play()