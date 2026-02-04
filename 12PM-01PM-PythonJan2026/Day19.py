"""
UDF:- User Define Functions
Built-in Libraries
    math , random

import libarary_name

library_name.function_name(arguments)

Example

import math

print( math.sqrt(9) )
print( math.pow(5,3) )


from library_name import funtion_name
function_name(arguments)
Example

from math import factorial
print( factorial(5) )


import random
print( random.random() )
print( random.random()*100 )
print( int(random.random()*100) )

import random
print( random.randint(1,6) )
print( random.randint(1000,9999) )
print( random.randint(100000,999999) )


UDF:- User Define Functions
Syntax:-

def function_name(parameter):
    definition of function

function_name(argument)

Example

def greet():
    print("Good Morning")


greet()
greet()
greet()


Function:- A function is a block of statements that
perform a specific task, and return a value.

def greet(val):
    print("Good",val)


greet("Morning")
greet("Noon")
greet("After Noon")
greet("Evening")



def add(n1 , n2):
    return n1+n2


print( add(20,30) )

def add(a,b=0):
    return a+b

print( add(10,20) )
print( add(10) )


def add(a=0,b=0,c=0,d=0):
    return a+b+c+d
print( add() )
print( add(20) )
print( add(20,30) )
print( add(40,60,80) )
print( add(40,60,80,90) )


def add(*a):   #  *a   will behave like a tuple
    return sum(a)


print( add(10,20,40,70) )
print( add(23,34,4,54,56,67,34,8,89,9,990,9,0) )


def fun(**a):  # **a  will behave like a dictionary
    return a


print( fun( name="Rahul" ) )


*args => it is a typle in a def with name args
**kagrs => it is a dictionary in a def with kargs


Recursion:- Recursion is a property of a function,
a function calls itself

def greet():
    print("Good Morning")
    greet()


greet()


# WAP to calculate the factorial of a number with UDF
and recursion

def fact(num):
    f = 1
    for i in range(1,num+1):
        f = f*i
    return f

print( fact(5) )


def fact(num):
    if num == 1:    
        return 1
    else:
        return num * fact(num-1)

print( fact(5) )

# WAP to add all natura numbers from 1 to N

def add(num):
    if num==1:
        return 1
    else:
        return num+add(num-1)

print(add(100))

"""
