# Nested for loop
colours =['red','green','blue']
objects =['pen','ball']
for i in colours:
    for x in objects:
        print(i,x)

print('\n')


# --> Nested for loop using range() method

languages = ['Python','Javascript','Java','Php']
extentions = ['.py','.js','.java','.php']

for i in range(len(languages)):
    for x in range(len(extentions)):
        if i==x:
            print(languages[i],extentions[x])