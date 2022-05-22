pos=-1

n=int(input("enter the no of elements:"))

a=list(map(int,input("enter the elements of the list:").strip().split()))[:n]

s=int(input("enter the element to be searched:"))


def search(list,n):
    list.sort()
    l=0
    u=len(list)-1
    
    while l<=u:
        
        mid=(l+u) // 2 
        
        if list[mid]==n:
            
            globals()['pos']=mid 
            return True
        
        else:
            
            if n>list[mid]:
                
                l=mid+1
                
            else:
                
                u=mid-1
        
    return False
    
    
if search(a,s):
    
    print("found at",pos)
    
else:
    
    print("not found")