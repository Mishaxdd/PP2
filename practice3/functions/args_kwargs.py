#1
def sumall(*args):
    print(sum(args))

sumall(1, 2, 3, 4)
#2
def fff(*args):
    for i in args:
        print(i)
    
fff("apple", "banana", "tomato")
#3
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")
#4
def multiply(*numbers):
    result = 1
    for n in numbers:
        result *= n
    print(result)

multiply(2, 3, 4)
#5
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")