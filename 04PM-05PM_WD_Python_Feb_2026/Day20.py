"""
UDF:- User Define Functions
Syntax:-
def function_name(parameter):
    definition

function_name(argument)

Example:-
def greet():
    print("Good Morning")

greet()
greet()
greet()


What is function?
A function is a block of statement that perform a specific
task and return a value.

Why we need UDF (User Define Function)?
To reduce the redundancy of code and
to divide a big code into pieces to reduce the complexity

Example

def greet(val):   # parameter
    print("Good",val)

greet("Morning")  # Argument
greet("Noon")
greet("After Noon")
greet("Evening")


def add(a,b):
    print(a+b)

add(10,20)
add(24,56)


The number of arguments should be equal to number
of parameters


def add(a,b,c):
    print(a+b+c)

add(10,20,30)

def add(a,b):
    print(a+b)

add(10,20)

# this sum function will return 6 but we need print it
li = [1,2,3]
print( sum(li) )


def add(a,b):
    return a+b
print( add(23,56) )


# WAP to check a number is Prime or not using UDF.

def checkPrime(num):
    for i in range(2,num):   
        if num%i==0:
            return "Not Prime"
    return "Prime"

print( checkPrime(27) )



# WAP to find all the Prime Number from 1 to 100

def checkPrime(num):
    for i in range(2,num):   
        if num%i==0:
            return False
    return True

for i in range(2,101):
    if checkPrime(i):
        print(i,end="  ")
        
"""
