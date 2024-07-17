# Area of Rectangle

# Variables in python are declared as we assign values to them
def findarea():
    length = float(input("Enter length of rectangle"))
    width = float(input("Enter width"))
    return length * width

area = findarea()
print(f"Area of the rectangle is {area}")
