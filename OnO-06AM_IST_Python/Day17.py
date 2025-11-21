"""
UDF:- User Define Functions

def function_name(parameter):
    definition

functions_name(argument)

def greet():
    print("Good Morning")

greet()
greet()


def greet(value):
    print("Good",value)

greet("Morning")
greet("Noon")
greet("After Noon")


def add(val1,val2):
    print("Addition :",val1+val2)

add(10,20)
add(35,78)


Function:- A function is a block of statements that perform
a specific task and return a value.

def add(val1,val2):
    return val1+val2

print( add(10,20) )


# WAF to check a number is prime or not
def checkPrime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True

if checkPrime(18):
    print("Prime")
else:
    print("Not Prime")



# WAF to find all the prime numbers from 1 to 1000
def checkPrime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True

for i in range(2,100):
    if checkPrime(i):
        print(i,end=" ")


def add(v1=0,v2=0,v3=0):
    return v1+v2+v3

print( add(10,20) )
print( add(10,20,30) )


def add(v1,v2,v3=0):
    return v1+v2+v3

print( add(10,20) )


def add(v1=0,v2=0,v3=0,v4=0,v5=0,v6=0):
    return v1+v2+v3+v4+v5+v6

print( add(10,20,30,40,50) )


def add(*v1):
    print(v1)
    print(type(v1))
    return sum(v1)

total = add(10,20,30,40,50,60,70,80)
print("Addition :",total)



def add(**v1):
    return v1


print( add(name='rahul',clas='Raju',address='Noida') )


# Advance Python
# lambda Expression

def cube(num):
    return num**3
print( cube(3) )


cube = lambda x:x**3
print( cube(5) )




add = lambda a,b:a+b
print( add(10,20) )



add = lambda *a:sum(a)
print( add(10,20,30,40) )



import math
sq = lambda a,b: math.sqrt(a+b)

print( sq(20,16) )


li = [1,2,3,4,5,6,7,8,9,10]
sq = []
for x in li:
    sq.append(x**2)

print(sq)



cube = lambda num:num**3
li = [1,2,3,4,5,6,7,8,9,10]
cub = []
for x in li:
    cub.append(cube(x))

print(cub)



# map Expression/function/class

cube = lambda num:num**3
li = [1,2,3,4,5,6,7,8,9,10]
cub = list( map(cube,li) )
print(cub)



# filter Expression/Function/class

cube = lambda num:num%2==0
li = [1,2,3,4,5,6,7,8,9,10]
cub = list( filter(cube,li) )
print(cub)


# reduce Expression/Function/built-in library function

import functools
li = [1,2,3,4,5,6,7,8,9,10]
add = lambda a,b:a+b

output = functools.reduce(add,li)
print(output)


from functools import reduce
li = [1,2,3,4,5,6,7,8,9,10]
add = lambda a,b:a+b

output = reduce(add,li)
print(output)


from math import sqrt,factorial

print( sqrt(9) )
print( factorial(5) )


from functools import reduce
li = [1,2,3,4,5,6,7,8,9,10]
add = lambda a,b:(a+1)+(b)

output = reduce(add,li)
print(output)

"""

