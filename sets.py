# SET IN PYTHON
# A set is a collection which is unordered, unchangeable*, and unindexed unique elements.

set1={1,"hello",3.4,2,5}

#  Accessing set elemenets
for x in set1:
    print(x)

# Check if element exists
print("hello" in set1)

# Adding element
set1.add("apple")
print(set1)

set2={'a','b','c','d','a'}

# ERROR
# print(set1 + set2)

print(set1 | set2)
