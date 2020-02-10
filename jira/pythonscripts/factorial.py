#n!=n * (n-1)!
#n!=1 if n=0 or n=1
def factorial(n):
    return 1 if (n==0 or n==1) else n*factorial(n-1)
 
n=int(input("enter number for to find factorial:"))
factorial(n)
print("factorial of {0} is {1}".format(n,factorial(n)))
