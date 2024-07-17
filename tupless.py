# Program to create a tuple and tuples convert to list

# Tuples are used to store multiple items in a single variable.
# Tuple items are ordered, unchangeable, and allow duplicate values.

my_tuple=(1,"shreya",23.5,"joshi")
print("Original tuple",my_tuple)

# tuples are unchangeable but we can convert it into list and then update
my_list=list(my_tuple)
my_list[1]="Kartikeya"

# converting back to tuple
my_tuple=tuple(my_list)
print("Tuple after updating:",my_tuple)

# accessing tuple elements
print(my_tuple[1])
print(my_tuple[2:])
print(my_tuple[:2])
print(my_tuple[1:3])
