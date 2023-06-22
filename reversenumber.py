'''a = str(input())
rev_a = ""
for char in a:
    rev_a = char+rev_a 
print(rev_a)''' 

def reverse_num(num):
    num_str = str(num)
    reverse_str = num_str[::-1]
    reverse_int = int(reverse_str)

    return reverse_int 
num = 12345 
a = reverse_num(num) 
print(a)