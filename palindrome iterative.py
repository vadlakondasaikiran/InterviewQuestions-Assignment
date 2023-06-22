a = str(input())
a = a.lower()
rev_a = ""
for char in a:
    rev_a = char+rev_a 
if a == rev_a:
    print(a, "is a palindrome")
else:
    print(a, "is not a palindrome")