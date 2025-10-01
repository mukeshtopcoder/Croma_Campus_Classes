"""
UDF:- User Define Functions
Syntax:-
def function_name(arguments):
    definition

function_name(parameter)

Example:-

def greet():
    print("Good Morning!")

greet()
greet()
greet()



def greet(var):
    print("Good",var)


greet("Noon")
greet("Morning")
greet("After Noon")
greet(2735)



Example:- WAP function to add two numbers.
def add():
    a = 10
    b = 20
    print(a+b)


add()


def add(x,y):
    print(x+y)

a = 10
b = 20
add(a,b)


def add(x,y):
    return x+y

a = 10
b = 20
print( add(a,b) )

What  is a function?
A function is a block of statements, that perform a specific
task and return a value.

# WAF to check a number is prime.

def is_Prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False

# WAP to find all prime numbers from 1 to 100.

def is_Prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False

for k in range(1,101):
    if is_Prime(k):
        print(k , end='  ')



libraries
How to import library and functions
import library_name

import math
print( math.sqrt(9) )
print( math.factorial(5) )


from library_name import function_name

from math import sqrt
print( sqrt(9) )

math library:-
sqrt , power , fabs etc

random library

import random
# it will print a random number from 0 to 1
print( random.random() )
print( random.random()*100 )
print( int(random.random()*100) )


import random
# it will print a random number from start to end number
print( random.randint(1,6) )
print( random.randint(1000,9999) )
print( random.randint(100000,999999) )


import random
li = ['Apple','Banana','Cherry','Dates']
print(random.choice(li))


# it can repeat the value
import random
li = ['Apple','Banana','Cherry','Dates']
print(random.choices(li , k=2))

# it will generate a unique value always
import random
li = ['Apple','Banana','Cherry','Dates']
print(random.sample(li , k=2))

"""
