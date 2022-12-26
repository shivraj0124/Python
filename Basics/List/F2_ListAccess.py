thislist = ["apple", "banana", "cherry"]
print(thislist[0]) # Accessing list using its Index

# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# we can identify element At -1 position,by following way
# (Length - Given index) 
# (3 - 1 = 2) it will print "cherry"

# Range
thislist = ["apple",6, "cherry","mango","Grape"]
print(thislist[2:4])
# it will print elements at index 2 and 3 

#  Here starting index is 2 and ending is 4 
# bydefault starting index is 0 and ending index is the length of List
print(thislist[:4])

print(thislist[2:])