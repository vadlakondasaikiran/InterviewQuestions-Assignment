a = int(input())
b = int(input())
c = int(input())

if a > b:
    greater = a 
else:
    greater = b 
if c > greater:
    greater = c 
print(greater, "is a gretest number")