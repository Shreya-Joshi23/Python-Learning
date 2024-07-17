# Program for tuple operations 

my_tuple=(1,5,3,4,2)
print("Original tuple:",my_tuple)

# Swapping elements in a tuple
temp_list=list(my_tuple)
# Simultaneous assignement
temp_list[0],temp_list[-1]=temp_list[-1],temp_list[0]
my_tuple=tuple(temp_list)
print("Swapped tuple:",my_tuple)

# Copy
copied_tuple=my_tuple
print("Copied tuple:",copied_tuple)

# Modify
temp_list[1]=1000
my_tuple=tuple(temp_list)
print("Modified tuple:",my_tuple)

#sort
sorted_list=sorted(my_tuple)
my_tuple=tuple(sorted_list)
print("Sorted tuple:",my_tuple)

# reversing
reversed_tuple=tuple(reversed(my_tuple))
print("Reversed tuple:",reversed_tuple);
