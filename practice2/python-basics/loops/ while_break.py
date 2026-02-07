#1
i = 0
while True:
    i += 1
    print(i)
    if i == 5:
        break  
#2
i = 1
while i < 10:
    if i == 5:
        break 
    print(i)
    i += 1
#3
total = 0
i = 1
while True:
    total += i
    if total > 50:
        break
    i += 1
#4
a = 10
while a<120:
    print("speed:", a)
    if a == 70:
        print("Finish")
        break
    a+=10
#5
import random

while True:
    a = random.randint(1, 10)
    print(a)
    if a < 3:
        print("number less 3")
        break