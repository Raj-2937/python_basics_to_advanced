a = input("enter the number :")

print(f"mutiplication of table of {a} is :")


try:
    for i in range (1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e :
    print("invalid input!")    

print("Some imp line of code")
print("end of program") 
    