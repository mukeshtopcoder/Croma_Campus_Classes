"""
Exception Handling:-
Errors:-
1. Syntax Error (Compile Error)
a = 10
print("Hello'a)
You need to fix them if you want to execute the program
This kind or error flaged by the interpreter at compilation
time

2. Runtime Error (Logical Error) / Exception
li = [23,56,78,90]
print("Hello")
print(li[29])
print("Bye")
It will raise an error/exception at runtime, program will
successfully execute and run partial program
This kind of error can not be flaged by interpreter
You can handle this error/exception at run time

3. Symantic Error

a = 10
b = 20
print(a*b)
We want to print the addition but we are using multiply
sign but it will not raise any error


Exception handling:-
A runtime error is called exception

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
print("Division : ",a/b)
print("Program Complete!")

if a = any number and b is 0 then, it will raise an error

to handle an exception
try , except , finally , else

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division : ",a/b)
except:
    pass
print("Program Complete!")



a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division : ",a/b)
except:
    print("Found An Error!")
print("Program Complete!")




a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division : ",a/b)
except:
    print("Found An Error!")
else:
    print("Division Successful!")
print("Program Complete!")




a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division : ",a/b)
except:
    print("Found An Error!")
else:
    print("Division Successful!")
finally:
    print("Ye to hamesha chalega")
print("Program Complete!")



try:
    # write your code
except:
    # write code/msg if it raise error
else:
    # write code/msg if there is no error
finally:
    # this part will execute always
    # write code/msg you want to execute always


# Nested except
a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
d = 7
li = [1,2,4]
try:
    print("Division : ",a/b)
    print(d)
    print(li[11])
except ZeroDivisionError as e:
    print("Found Error :",e)
except NameError as e:
    print("Found Error :",e)
except IndexError as e:
    print("Found Error :",e)
print("Program Complete!")





# Nested except
a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
d = 7
li = [1,2,4]
try:
    print("Division : ",a/b)
    print(d)
    print(li[1])
    print(10/'5')
except ZeroDivisionError as e:
    print("Found Error :",e)
except NameError as e:
    print("Found Error :",e)
except IndexError as e:
    print("Found Error :",e)
except:
    print("Unknown Error!")
print("Program Complete!")



# Exception Classes
a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
d = 7
li = [1,2,4]
try:
    print("Division : ",a/b)
    print(d)
    print(li[1])
    print(10/'5')
except Exception as e:
    print("Found Error :",e)
print("Program Complete!")


# raise
If you want to raise an error with a new condition
age = int(input("Enter Your Age :"))
if age<18:
    raise ValueError("Age should be 18+")
else:
    print("Welcome!")


age = int(input("Enter Your Age :"))
if age<18:
    raise ZeroDivisionError("Age should be 18+")
else:
    print("Welcome!")


# Custom Exception
class CreateAnyExceptionName(Exception):
    pass


class AgeError(Exception):
    pass
age = int(input("Enter Your Age :"))
if age<18:
    raise AgeError("Age should be 18+")
else:
    print("Welcome!")
"""
