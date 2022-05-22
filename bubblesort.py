n=int(input("enter the number of elements:"))
a=list(map(int,input("enter the numbers:").strip().split()))[:n]

def sort(nums):
    for i in range(len(nums)):
        for j in range(0,len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                
        
sort(a)
print(a)