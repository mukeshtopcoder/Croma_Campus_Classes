"""
UDF - User Define Functions
Function:- A block of statements that perform a specific
task and return a value. 

Syntax:-
def function_name(parameter):
    definition

function_name(argument)

Example:-
def greet():
    print("Good Morning!")

greet()



def greet(val):
    print("Good",val)

greet("Morning")
greet("Noon")
greet("After Noon")
greet("Evening")



def add(x,y):
    print(x+y)

add(376,275)


# this is the right way to define a function
def add(x,y):
    return x+y

print( add(10,20) )



def add(x,y,p,q):
    return x+y+p+q


print( add(10,20,30,40) )




def add(x=0,y=0,p=0,q=0):
    return x+y+p+q


print( add(10,20,30) )



def add(x,y=0,p=0,q=0):
    return x+y+p+q


print( add(100) )


# It is a syntax error
def add(x=0 , y):
    return x+y


print( add(100,200) )
# You need to define the value of first parameter



def add(a=0,b=0,c=0,d=0,e=0,f=0,g=0):
    return a+b+c+d+e+f+g


print( add(23,567,89,467,788) )


#  *args  => it represents to a tuple
def add(*num):
    return sum(num)

print( add(23,24,5,67,89) )


#  **kargs  => it represents to a dictionary
def add(**num):
    return num

print( add(name="Ravi",clas="XII") )

"""
