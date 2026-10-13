# set is collection of well defined object.


#factorial(7)= 7*6*5*4*3*2*1
#factorial(6)= 6*5*4*3*2*1
#factorial(5)= 5*4*3*2*1
#factorial(4)= 4*3*2*1
#factorial(3)= 3*2*1
#factorial(2)= 2*1
#factorial(1)= 1

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(3))


def fibonacci_sequence(f):
    f(0) = 0
    f(1) = 1
    f(2) = f1 + f0 
    f(n) = f(n-1) + f(n-2)
    
    fibonacci_sequence(2)
print(fibonacci_sequence)

