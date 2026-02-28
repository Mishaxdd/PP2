# 1
def square_generator(n):
    for i in range(n + 1):
        yield i * i
for value in square_generator(5):
    print(value)
# 2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
n = int(input("Enter a number: "))
print(",".join(str(num) for num in even_numbers(n)))
# 3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for num in divisible_by_3_and_4(50):
    print(num)
# 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
for value in squares(3, 7):
    print(value)
    # 5.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
for number in countdown(5):
    print(number)