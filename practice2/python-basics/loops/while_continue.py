#1
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#2
i = 0
while i < 5:
    i += 1  
    if i % 2 == 0:
        continue  
    print(i)
#4
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
#5
n = 0
while n < 15:
    n += 1
    if n % 3 == 0 or n % 5 == 0:
        continue  
    print(n)