#Python program to check whether a number is Prime or not
#Given a positive integer N. The task is to write a Python program to check if the number is prime or not.
#Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and #itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}.

def primeornot(a):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                print(a,"not a prime")
                break
        else:
            print(a,"ita prime")



a=int(input("enter number to find it is prime or not :"))
primeornot(a)

"""
num = 11

# If given number is greater than 1
if num > 1:

   for i in range(2, num//2):
       if (num % i) == 0:
           print(num, "is not a prime number")
           break
   else:
       print(num, "is a prime number")

else:
   print(num, "is not a prime number")
"""