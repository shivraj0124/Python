# we can add an element in the list using append() method
thislist = ["Javascript", "Python", "Java"]
thislist.append("C++")
print(thislist)
# result will be ['Javascript', 'Python', 'Java', 'C++']
# the element will add at end of the list


# We can add element in list at particular index using insert() method
thislist = ["Javascript", "Python", "Java"]
thislist.insert(1,"C++")
print(thislist)
# the result will be ['Javascript', 'C++', 'Python', 'Java']


# we can also add tuple,set,dictionary using extend() method
thislist = ["Javascript", "Python", "Java"]
thistuple =("C","C++")
thislist.extend(thistuple)
print(thislist)
# the result will be ['Javascript', 'Python', 'Java', 'C', 'C++']
