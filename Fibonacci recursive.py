def fibonacci(b):
    if b <=1 :
        return b 
    return fibonacci(b-1)+fibonacci(b-2)
b = int(input())
for i in range (0,b):
    print(fibonacci(i))
