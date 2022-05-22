def reverse(n):
    rev=0
    while n>0:
          x=n%10
          rev=rev*10+x
          n=n//10
          
    return str(rev)
 
a=int(input())    
result=reverse(a) 
print(result)