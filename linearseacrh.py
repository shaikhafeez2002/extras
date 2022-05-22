pos=-1
n=int(input("enter the no of element:"))
a=list(map(int,input("enter the list elements: ").strip().split()))[:n]
s=int(input("enter the element to find:"))

def search(list,n):
 i=0  
 while i < len(list):
    if list[i]==n:
        globals()['pos']=i
        return True
    i=i+1
    
 return False
    
    
if search(a,s):
    print("element at",pos)
else:
    print("not found")