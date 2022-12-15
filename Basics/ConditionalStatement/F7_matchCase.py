x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 10:
        print("case is 4")
    # default case
    case _ :
        print("default")