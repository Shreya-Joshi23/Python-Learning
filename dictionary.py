# // create a dictionary and perform the operations - copy,pop,update,clear,length etc..q

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

my_dict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
# Creating copy
# 
dict_copy1=my_dict.copy()
# or
dict_copy2=dict(my_dict)

print(dict_copy1)
print(dict_copy2)

# Popping an element
popped_element=my_dict.pop('year')
print("Popped element:",popped_element)
print("Dictionary after popping",my_dict)

# Updating 
my_dict.update({'year':1964,'remarks':"Good model"})
print("dict after updating:",my_dict)

# Getting length of the dict
dict_length=len(my_dict)
print("Length of dict",dict_length)

# Clearing the dict
my_dict.clear()
print("Dictionary after clearing:",my_dict)

# del my_dict
# This will give error bcoz dict no longer exists
# print("dictionary after deleting",my_dict) 

