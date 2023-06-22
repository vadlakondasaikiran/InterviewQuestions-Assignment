a = input()
sum = 0 
length = len(a)
for digit in a:
    sum = sum + (int(digit)**length)

if sum == int(a):
    print(a, "Armstrong number")
else:
    print(a, "Not a Armstrong number")