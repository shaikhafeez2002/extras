a=int(input())
temp=a

def palindrome(n):
    rev=0
    while n!=0:
        x=n%10
        rev=rev*10+x
        n=n//10
    
    return rev

hello=palindrome(a)

if(hello==temp):
    print("it is a palindrome")
else:
    print("not a palindrome")
