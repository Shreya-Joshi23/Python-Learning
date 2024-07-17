# Program to create array , display and access elements

# ARRAYS IN PYTHON

int_array=[]
n=int(input("Enter number of elements in array"))

for i in range(n):
    a=int(input("enter number"))
    int_array.append(a)

print("Array Elements:",int_array)

# Accessing individual elements
for idx in range(len(int_array)):
    print(f"Element at index {idx}:{int_array[idx]}")
