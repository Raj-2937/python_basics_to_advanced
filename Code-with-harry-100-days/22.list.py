list = [45,6,53,346,245 ,"aman" , "aryan" ,"karan", "rohit"]
print(list)

print(type(list))
print(list[1:5])
print(list[2:9])
print(list[0:5])
print(list[3])
print(list[4])
print(list[5])
print(list[6])


print(list[-3])#Negative index
print(list[len(list)-3])#Positive index

print(list[5-3]) #postive index
print(list[2]) #postive index

if "aman" in list: # for checking the value in present in list. 
    print("yes")
    
else:
    print("no")
    