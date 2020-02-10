def fabinac_ser(a):
    b=[x for x in range(0,2)]
    for i in range(2,a):
        c=b[-1]+b[-2]
        b.append(c)
    #print(b)
    print(b[d-1])
    print("Position of n'th multiple of k inFibonacci Seires is",b.index(b[d-1]))



b=int(input("enter number for multiple: \n "))
c=int(input("enter multiples of number: \n "))
d=int(b*c)

fabinac_ser(d)
#print("Position of n'th multiple of k inFibonacci Seires is")