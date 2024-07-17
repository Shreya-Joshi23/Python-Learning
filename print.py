#  we cannot combine strings and numbers like this:

# age = 21
# txt = "My name is Shreya, I am " + age
# print(txt)

# But we can combine strings and numbers by using f-strings or the format() method!

import math

def areaCircle():
    radius = float(input("enter radius"))
    return math.pi * pow(radius,2)

area = areaCircle()
print(f"Area of circle is {area}")
print("Area of the circle is {:.4f}".format(area))