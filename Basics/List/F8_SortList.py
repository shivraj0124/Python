# sort() used to sort the list in ascending order 
myList = [1,7,2,8,5]
myList.sort()
print(myList)

# here we are going to sort list in descending order
myList.sort(reverse=True)
print(myList)

# sorting list using our own function
def myfunc(n):
    print(n)
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)


# when there are uppercase and lowercase elements present in list we can use str.lower
thislist = ["banana", "Orange", "Kiwi", "cherry", "Cat"]

thislist.sort(key=str.lower)

print(thislist)
