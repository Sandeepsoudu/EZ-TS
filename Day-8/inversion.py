def inversion(a):
    count=0
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]<a[j]:
                count+=1
    return count
a=list(map(int,input("enter the numbers").split()))
print(inversion(a))