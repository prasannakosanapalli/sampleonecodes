def arrayrotation(a,n):
    for i in range(0,n):
        a.append(a.pop(0))
    print(a)
    for j in range(0,len(a)):
        print(a[j],end=' ')


a=[1,2, 3, 4, 5, 6, 7, 8, 9]
arrayrotation(a,3)