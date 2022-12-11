# The count() method returns the number of times the given value has occurred within the given string.
str1 = "Hello World! Hello!" 
countStr = str1.count("l")
print(countStr)

# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str2 = "VS code is the best !!!"
print(str2.endswith("!!!"))
# We can check the value is in between the string by it's index
print(str2.endswith("the",10,14))

# find() will return the index of given value in string
str3 ="VS code is the best !!!"
print(str2.find("code")) # if value is not present in string it will return -1

# index() returns the index of given value
str4 = "VS code is the best !!!"
print(str4.index("best")) # if given value is not present the it will raise the exception

# isalnum() returns True only if string consists A-Z, a-z, 0-9
str5="PythonJavaJavascript"
print(str5.isalnum())

# isalpha() returns True only if string consits A-Z, a-z
str6="PythonJavaJavascript"
print(str6.isalpha())

# islower() returns True only if all the characters are in lower case
str7="python java javascript"
print(str7.islower())

# isupper() returns True only if all the characters are in Upper case
str8 = "PYTHON JAVA JAVASCRIPT"
print(str8.isupper())

# isspace() returns True only if string contains white spaces
str9 = "    "
print(str9.isspace())

# istitle() returns True if first letter of each word in string is in Upper case
str10 = "Python Javascript Java"
print(str10.istitle())

# startswith() return True if string starts with given value
str11="Python Javascript Java"
print(str11.startswith("Python"))

# swapcase() converts Uppercase to lower and lower to Uppercase
str12="Python Javascript Java"
print(str12.swapcase())

# title() it converts the first letter of each word of string to Upper case
str13="Python is a popular programming language"
print(str13.title())