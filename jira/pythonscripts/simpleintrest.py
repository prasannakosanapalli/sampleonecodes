#simpleintrest= (P*R*T)/100

principle=float(input("please enter the principle amount in rupees:"))
time=int(input("please enter the time in years:"))
intreset=int(input("please enter the intrest in percentaage:"))
simpleintrest=( principle * time * intreset )/100
totalamount= principle + simpleintrest

print("given principle: {0}, time:{1},intreset:{2} is".format(principle,time,intreset))
print("total simple intrest is",simpleintrest)
print("total amount is",totalamount)

