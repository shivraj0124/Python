# remove() method removes the given element from list
thislist = ["Python","Javascript","Java","C","C++","Php"]
thislist.remove("Java")
print(thislist)
# result will be ['Python', 'Javascript', 'C', 'C++', 'Php']

# pop() method is used to remove the element with specified index
thislist = ["Python", "Javascript", "Java", "C", "C++", "Php"]
thislist.pop(2)
print(thislist)
# result will be ['Python', 'Javascript', 'C', 'C++', 'Php']

# If index is not specified in pop() method it will remove last element
thislist = ["Python", "Javascript", "Java", "C", "C++", "Php"]
thislist.pop()
print(thislist)
# result will be ['Python', 'Javascript', 'Java', 'C', 'C++']

# clear() will remove all elements of list
thislist = ["Python", "Javascript", "Java", "C", "C++", "Php"]
thislist.clear()
print(thislist)
# result will be []

# del keyword is used to delete or remove element of specified index
thislist = ["Python", "Javascript", "Java", "C", "C++", "Php"]
del thislist[1]
print(thislist)
# result will be ['Python', 'Java', 'C', 'C++', 'Php']

# Using del keyword we can delete the list
thislist = ["Python", "Javascript", "Java", "C", "C++", "Php"]
del thislist
print(thislist)
# result will be -->
# NameError: name 'thislist' is not defined
# hence list is deleted successfully