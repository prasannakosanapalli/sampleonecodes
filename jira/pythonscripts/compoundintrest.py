#compoundintrest= p*(1+r/100)^t

principle=float(input("please enter the principle amount in rupees:"))
time=int(input("please enter the time in years:"))
intreset=int(input("please enter the intrest_rate in percentaage:"))
def compoundintrest(principle,time,intreset):
    compound_intrest= principle * (1 + (intreset/100))**time
    
    total_intrest= compound_intrest - principle
    
    print("given principle: {0}, time:{1},intreset:{2} is".format(principle,time,intreset))
    print("total compound intreset is",compound_intrest)
    print("total intreset is",total_intrest)


compoundintrest(principle,time,intreset)

