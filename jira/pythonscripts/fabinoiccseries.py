#Python Program for n-th Fibonacci number
#In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
#    Fn = Fn-1 + Fn-2

def fabinac_ser(a):
    b=[x for x in range(0,2)]
    for i in range(2,a):
        c=b[-1]+b[-2]
        b.append(c)
    print(b)















a=int(input("enter max value to need fabinaoc series: \n "))
fabinac_ser(a)
