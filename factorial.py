#iteratively
def factorial(x):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        
    return fact

n=int(input())
hello=factorial(n)
print(hello)    

#using recursion

def fact(x):
    
    if(x==0):
        return 1
    
    return x*fact(x-1)

n=int(input())   
result=fact(n)
print(result)