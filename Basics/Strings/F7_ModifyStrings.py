x = "hello world!"
print(x.upper()) #upper() returns string in Upper case
# -> ouput: HELLO WORLD!

x = "HELLO WORLD!"
print(x.lower()) #lower() returns string in Lower case 
# -> output: hello world!  

x = " HELLO WORLD! "
print(x.strip()) #strip() removes whitespaces from begning or end of string
# -> output:  HELLO WORLD!          

x = "hello world!"
print(x.replace("!"," Learn Python")) #replace() replace the string with another string
# output: hello world Learn Python

x = "helloworldLearnPython"
print(x.split("o")) # split() use to separate the string by specified separator
# here 'o' is separator
# output:  ['hell', 'w', 'rldLearnPyth', 'n']
