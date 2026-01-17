"""
UDF:- User Define Functions
Function:- A function is a block of statements that
perform a specific task and return a value

li = [34,56,89,56,35,68,35]
print( sum(li) )

here sum is a function

def function_name(parameters):
    definition

USE CASE:-
function_name(argument)

def greet():
    print("Good Morning!")


greet()
greet()
greet()


def greet(val):
    print("Good",val)


greet("After Noon")



def add(a , b):
    return a+b

print( add(10,20) )
print( add(34,78) )


def add(a=0,b=0,c=0):
    return a+b+c

print( add(20,50) ) 
print( add(20,30,50) )


def add(a=0,b=0,c=0):
    return a+b+c


print( add(20) ) 

sum([20,50])


def add(*a):
    return sum(a)


print( add(10,20,30,40,50) ) 

"""
