#1
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#2
def my_function(name): 
  print("Hello", name)

my_function("Emil") 
#3
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")
#4
def sum(a, b):
    print(a + b)

sum(3, 7)
#5
def rectangle_area(length, width):
    print(length * width)

rectangle_area(4, 6)