# for loop is used for reapeating statements , also use for iterating a string,list, etc

name = "Google" 
for i in name:
    print(i) # prints each character present in name variable

game = ["Cricket","Football","Kabaddi"]
for j in game:
    print(j)

# range() is used when our loop execute no. of times we specified
# Bydefault ,
#    ---->    it starts with 0 and end till given number
#    ---->    if range(n) loop will iterate n times 
#    ---->    increment by 1 :

print("Loop with range only:")
for i in range(5): # by default i starts from 0 and loop will continue till i=4
    print(i)

print("Loop with starting point and range:")
for i in range(2,20): # loop starts with i=2 and loop will continue till i=19
    print(i)
    
print("Loop with starting point ,range and with customize increment:")
for i in range(2,20,3): # loop starts with i=1 and loop will continue till i=19
    print(i)
    

print("For loop with else:")
# when loop's condition get false else part will execute
for i in range(5):
    print(i)
else:
    print("This is else part")

# --> The else block will NOT be executed if the loop is stopped by a break statement.

print("\nNested for loop:\n")
# nested loop is loop inside a loop
# inner loop will execute for every iteration of outer loop

colours = ["blue","black","red"]
objects = ["pen","cover","pencil"]

for i in colours:
    for j in objects:
        print(i + " " + j)
    print("\n")