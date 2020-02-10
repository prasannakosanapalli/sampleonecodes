"""
Python Program for How to check if a given number is Fibonacci number?
Given a number \’n\’, how to check if n is a Fibonacci number. First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 141, ..
Input : 8
Output : Yes
Following is an interesting property about Fibonacci numbers that can also be used to check if a given number is Fibonacci or not.
A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square (Source: Wiki)
"""

import math
def issqurt(n):
    c=int(math.sqrt(n))
    return c*c == n

def isfabin(n):
    return issqurt(5*n*n + 4 ) or issqurt(5*n*n + 4 )


n=int(input("given number to check"))
if isfabin(n) == True:
    print("its a fabinoic",n)
else:
    print("it not fabnoic",n)
