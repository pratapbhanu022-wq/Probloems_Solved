def is_palindrome(x:int)->bool:
    if x<0:
        return False
    original=x
    rev=0
    while x>0:
        digit=x%10
        rev=rev*10+digit
        x//=10
    return rev==original
i=int(input("Enter number : "))
print(is_palindrome(i))