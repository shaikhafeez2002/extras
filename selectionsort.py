from tempfile import tempdir


n=int(input("enter the number of elements:"))
a=list(map(int,input("enter the numbers to be sorted:").strip().split()))[:n]

def sort(nums):
    
    for i in range(len(nums)):
        minpos=i
        
        for j in range(i+1,len(nums)):
            if nums[j] < nums[minpos]:
                minpos=j
                
        nums[i],nums[minpos]=nums[minpos],nums[i]
       
    
sort(a)
print(a)