row=9
col=9
for i in range(row):
    for j in range(col):
        if i==j or i+j==9-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()