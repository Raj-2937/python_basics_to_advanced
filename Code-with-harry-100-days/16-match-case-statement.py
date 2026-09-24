x = int(input("enter the value of x:"))
# x is the variable to match 

match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")
    
    case _:
        print(x)
