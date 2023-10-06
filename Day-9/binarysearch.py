def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            return mid-1
        else:
            return mid+1
    return -1
arr=list(map(int,input().split()))
target=int(input())
a=binary_search(arr,target)
if a!=-1:
    print("element is found")
else:
    print("element is not found")