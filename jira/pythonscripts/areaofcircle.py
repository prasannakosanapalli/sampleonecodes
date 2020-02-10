#area of circle= pie * r^2


import math

def area_circle(radius):
    area=math.pi*(radius**2)
    return print("area of circle is {}".format(area)) 

  
radius=int(input("please enter radius of circle : \n"))
area_circle(radius)