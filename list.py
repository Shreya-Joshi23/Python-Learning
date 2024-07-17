# List is a collection which is ordered and changeable. Allows duplicate members.
# Adding new elements will add them at the end of the list

# PROGGRAM TO CREATE A LIST FROM INPUT ELEMENT AND SORTING THEM

def listinput(n):
    lst=[]
    for i in range(n):
        element=int(input("Enter an element"))
        lst.append(element)
        i+=1
    return lst


n=int(input("Enter the number of elements in a list"))
user_list=listinput(n)
user_list.sort()
print("The list created is:",user_list)
