n = int(input())
factors = 0 
for i in range(2,n):
    if (n%i == 0):
        factors = factors+1 
if factors == 0:
    print(n , "is a prime number") 
else:
    print(n, "is not a prime number")