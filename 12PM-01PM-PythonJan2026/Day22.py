"""
Errors:-
1- Syntax Error

a = 100
print("Hello India"a)

An error occur at compile time is called Syntax Error
An error flaged by compiler/interpreter

Solution:-
you need to fix the error.
a = 100
print("Hello India",a)


2- Logical Error/Runtime Error

a = int( input("Enter A Number : ") )
b = int( input("Enter B Number : ") )
print("Division :",a/b)

if USER enter 0 for b variable
user will get an error ZeroDivisionError
This type of error is called Run Time Error.
And it can not flagged by Compiler/Interpreter


Solution:-
You need to handle the error
It is called Exception Handling


3- Symantic Error
a = 10
b = 20
print("Addition :",a*b)

In this case you need to find the logical error and fix it


Expection Handling
    try , except 

try:
    Code here
except:
    alternate code


try:
    a = int( input("Enter A Number : ") )
    b = int( input("Enter B Number : ") )
    print("Division :",a/b)
except:
    print("Division is not possible")



else

try:
    a = int( input("Enter A Number : ") )
    b = int( input("Enter B Number : ") )
    print("Division :",a/b)
except:
    print("Division is not possible")
else:
    print("Division Successfull")

if an error occur in try block
it will take cursor to the except block
if there is no error than it will take cursor to the
else block


finally

try:
    a = int( input("Enter A Number : ") )
    b = int( input("Enter B Number : ") )
    print("Division :",a/b)
except:
    print("Division is not possible")
else:
    print("Division Successfull")
finally:
    print("Ye to Hamesha Chalega")

finally block will execute always
if there is an error occur or not or program crashed


Types of Exception

try:
    a = int( input("Enter A Number : ") )
    b = int( input("Enter B Number : ") )
    print("Division :",a/b)
except ZeroDivisionError as e:
    print("Found Error :",e)


Nested except
try:
    a = int( input("Enter A Number : ") )
    b = int( input("Enter B Number : ") )
    print("Division :",a/b)
except ZeroDivisionError as e:
    print("Found Error :",e)
except ValueError as e:
    print("Found Error :",e)



try:
    a = int( input("Enter A Number : ") )
    b = int( input("Enter B Number : ") )
    print("Division :",a/b)
    print(a[0])
except ZeroDivisionError as e:
    print("Found Error :",e)
except ValueError as e:
    print("Found Error :",e)
except Exception as e:
    print("Found Error :",e)


Exception class is the mother class of every exceptional class



try:
    a = int( input("Enter A Number : ") )
    b = int( input("Enter B Number : ") )
    print("Division :",a/b)
except Exception as e:
    print("Found Error :",e)



assert
it is use to raise an custom error

age = int(input("Enter Age : "))
assert age>=18 , "Age Can not be less then 18"
print("Welcome")


try:
    age = int(input("Enter Age : "))
    assert age>=18 , "Age Can not be less then 18"
except Exception as e:
    print("Error :",e)
else:
    print("Welcome")


raise
it is also use to raise an custom error

age = int(input("Enter Age : "))
if age<18:
    raise ValueError("Age Should Be 18 or Above")
else:
    print("Welcome")


age = int(input("Enter Age : "))
if age<18:
    raise ZeroDivisionError("Age Should Be 18 or Above")
else:
    print("Welcome")


CUSTOM EXCEPTION CLASS


class AgeError(Exception):
    pass
age = int(input("Enter Age : "))
if age<18:
    raise AgeError("Age Should Be 18 or Above")
else:
    print("Welcome")

"""

