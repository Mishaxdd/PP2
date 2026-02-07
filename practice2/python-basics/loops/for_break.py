#1
for i in range(10):
    if i == 4:
        break
    print(i)
#2
a = [2,6,-7,34]
for n in a:
    if n < 0:
        break
    print(n)
#3
total = 10
for i in range(10):
    if i == 5 :
        break
    total+=i
    print(total)
#4
for a in range(10, 120, 10):
    print("speed:", a)
    
    if a == 70:
        print("Finish")
        break
#5
for i in range(1, 10):
    if i % 2 == 0:
        break
    print(i)