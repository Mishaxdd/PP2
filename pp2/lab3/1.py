a = input().strip()
booll = True
for i in a:
    if int(i) % 2 != 0:
        booll = False
        break
    
if booll:
        print("Valid")
else:
        print("Not valid")
