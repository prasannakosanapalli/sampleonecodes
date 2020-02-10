#abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
#Input : 153
#Output : Yes
#153 is an Armstrong number.
#1*1*1 + 5*5*5 + 3*3*3 = 153
#Input : 1634
#Output : Yes
#1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
#Input : 1253
#Output : No
#1253 is not a Armstrong Number
#1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723

def arm_strong_num(a):
    global c
    b=str(a)
    c=len(b)
    #print(c)
    e=0
    for i in range(c):
        #print(b[i])
        d=int(b[i]) ** c
        #print(d)
        e=e+d
    print("total value is",e)
    if a==e:
        return print("yes {0} is a armstrong num".format(a))
    else:
        return print("no {0} is a not a armstrong num".format(a))
       
a=int(input("please enter number to verify it is armstrong or not: \n"))
arm_strong_num(a)        
        
        