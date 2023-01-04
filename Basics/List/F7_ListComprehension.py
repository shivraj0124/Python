# List comprehension offers shorter syntax when we have to create new list based on existing list
thislist = ["Python","Javascript","Java","C","C++","Php"]
newList=[]

for x in thislist:
    if 'a' in x:
        newList.append(x)
print(newList)


# List comprehension in one line
thislist = ["Python", "Javascript", "Java", "C", "C++", "Php"]
newList = [x for x in thislist if 'a' in x]
print(newList)
