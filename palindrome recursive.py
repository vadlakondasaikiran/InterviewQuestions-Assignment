n = int(input())
def reverse(num):
    if num<10:
      return num 
    else:
      return int(str(num%10) + str(reverse(num//10)))
def isPalindrome(num):
    if num == reverse(num):
        return 1
    return 0
if isPalindrome(n) == 1:
    print(n, "number is a palindrome")
else:
    print(n,"number is a not palindrome") 