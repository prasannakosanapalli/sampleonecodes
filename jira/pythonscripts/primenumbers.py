#Python program to print all Prime numbers in an Interval
#Given two positive integer start and end. The task is to write a Python program toprint all Prime numbers in an Interval.
#Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}.

def prime_number(a,b):
    c=[]
    for val in range(a,b + 1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                c.append(val)
    print(c)


x, y = [int(x) for x in input("Enter two value: ").split()]
prime_number(x,y)

"""

"""
