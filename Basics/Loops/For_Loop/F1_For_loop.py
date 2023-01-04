# for loop on list to access each element
languages = ['Python','Javascript','Java','Php']
for i in languages:
    print(i)

print('\n')
# for loop on string to access each character
for i in "Shivraj":
    print(i)

print('\n')
# break keyword is used break or end the loop
for i in languages:
    if i == 'Java':
        break
    print(i) 

print('\n')
# continue keyword is used to skip execution part(after continue keyword statements) at that iteration
for i in languages:
    if i == 'Java':
        continue
    print(i)

print('\n')

