"""
UDF:- User Define Function

def function_name(parameters):
    definition
    return result

function_name(argument)

# WAF to check a number is prime.
def checkPrime(num):
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    return True

print( checkPrime(18) )


Recursion:-
def hello():
    print("Hello India")
    hello()

hello()


# WAP to calculate factorial of a number.

def fact(num):
    if num==0 or num<0:
        return 1
    else:
        return num*fact(num-1)

print( fact(5) )

# WAF to add all natural numbers using recursion.

def add(num):
    if num==0 or num<0:
        return 0
    else:
        return num+add(num-1)

print( add(10) )

# WAP to calculate cube of all numbers of a list.

def cube(num):
    return num**3

li = [1,2,3,4,5,6,7,8,9,10]
for i in li:
    print(cube(i))


def cube(num):
    return num**3

li = [1,2,3,4,5,6,7,8,9,10]
cubes = []
for i in li:
    cubes.append(cube(i))

print(cubes)


Advance Python
lambda expression

def cube(num):
    return num**3

function_name = lambda parameter : definition
cube = lambda num:num**3

cube = lambda num:num**3

li = [1,2,3,4,5,6,7,8,9,10]
cubes = []
for i in li:
    cubes.append(cube(i))

print(cubes)


# WAP To filter all even numbers from a list.

even = lambda num:num%2==0

li = [1,2,3,4,5,6,7,8,9,10]
for i in li:
    if even(i):
        print(i)


# WAP to find factorial of a number
def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)

print(fact(5))


fact = lambda num:1 if num==0 else num*fact(num-1)

print(fact(5))

# lambda
# map , filter , reduce
map :- map is a iterator
it iterate all the values of a collection and return some
output for every value.

# WAP to calculate the cubes of all elements of a list


cube = lambda num:num**3
li = [1,2,3,4,5,6,7,8,9,10]

result = list(map(cube , li))
print(result)


cube = lambda num:num**3
li = [1,2,3,4,5,6,7,8,9,10]

print( list(map(cube , li)) )


cube = lambda num:num**3

print( list(map(cube , [1,2,3,4,5,6,7,8,9,10])) )


# lambda / anonymous function
print( list(map(lambda num:num**3, [1,2,3,4,5,6,7,8,9,10])) )


# filter :- it is also iterator
it iterate every value of a collection and return value
on a boolean result
# WAP to filter all odd numbers from a list

li = [32,56,90,65,78,64,24,67,80,91,68,35,24]
even = lambda num:num%2!=0
result = list(filter(even,li))
print(result)



li = [32,56,90,65,78,64,24,67,80,91,68,35,24]
print( list(filter(lambda num:num%2!=0,li)) )


# reduce :- It is also a iterator
it reduce a complete collection to a single value.

# WAP to add all values of a list
from functools import reduce
li = [*range(1,11)]
print( reduce(lambda a,b:a+b , li) )


# WAP to find all the even numbers of a list and calculate
the cube of all values and print their sum.

from functools import reduce
li = [1,2,3,4,5,6,7,8,9,10]
even = filter(lambda num:num%2==0 , li)
cubes = map(lambda num:num**3 , even)
add = reduce(lambda a,b:a+b , cubes)
print(add)


from functools import reduce
li = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda a,b:a+b , map(lambda num:num**3 , filter(lambda num:num%2==0 , li)) ))


"""

