"""
Error:-
Mainly 3 types of error in python
1- Syntax Error (Compile Time Error)
a = 10
print("Value of A is"a)
we forget to put a comma in print statement, thats why this
program will raise an syntax error and flaged by interpreter.
program can run only when we fix the error

2- Logical Error (Run Time Error) / Exception
a = float(input("Enter A Number : "))
b = float(input("Enter B Number : "))
print("Division of A and B (A/B) :", a/b)
print("Program Completed!")

this program will raise an exception if user will enter
value of B 0 .  (ZeroDivisionError)

3- Symantic Error
a = float(input("Enter A Number : "))
b = float(input("Enter B Number : "))
print("Addition of A+B ",a*b)

this program is suppose to be print Addition of two numbers
but coder applied multiplication in code
Sometimes you will get right answers if inputs are 0 and 0
or 2 and 2 but wrong rest all the time.

Exception Handling:-
try , except , finally , else , raise
Exception Handling is a way to manage errors that occur
while a program runs, so that our code doesn't crash
unexpectedly
It lets you detect , responed to and recover from errors

Basic Syntax:- (Exception Handling)

try:
    -- Write You Python Code (may be exception)
except:
    -- code in case if found any exception

# Example
try:
    a = float(input("Enter A Number : "))
    b = float(input("Enter B Number : "))
    print("Division of A and B (A/B) :", a/b)
except:
    print("Division Not Possible")
print("Program Completed!")

# Another way!
try:
    a = float(input("Enter A Number : "))
    b = float(input("Enter B Number : "))
    print("Division of A and B (A/B) :", a/b)
except ZeroDivisionError as e:
    print("Found Error :",e)
print("Program Completed!")


# Multiple Except
try:
    a = float(input("Enter A Number : "))
    b = float(input("Enter B Number : "))
    print("Division of A and B (A/B) :", a/b)
except ZeroDivisionError as e:
    print("Found Error :",e)
except ValueError as e:
    print("Found Error :",e)
print("Program Completed!")



# Another Way

li = [2,56,78,223]
try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division of A and B (A/B) :", a/b)
    print("Value of index",a,"is :",li[a])
except ZeroDivisionError as e:
    print("Found Error :",e)
except ValueError as e:
    print("Found Error :",e)
except IndexError as e:
    print("Found Error :",e)
print("Program Completed!")

# Another Way
li = [2,56,78,223]
try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division of A and B (A/B) :", a/b)
    print("Value of index",a,"is :",li[a])
except ZeroDivisionError as e:
    print("Found Error :",e)
except ValueError as e:
    print("Found Error :",e)
except Exception as e:
    print("Found Error :",e)
print("Program Completed!")


# Exception class (Mother class of all exception classes)
li = [2,56,78,223]
try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division of A and B (A/B) :", a/b)
    print("Value of index",a,"is :",li[a])
except Exception as e:
    print("Found Error :",e)
print("Program Completed!")


# ELSE Block
a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division of A and B (A/B) :", a/b)
except Exception as e:
    print("Found Error :",e)
else:
    print("Division Completed!")
print("Program Completed!")


# FINALLY BLOCK

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division of A and B (A/B) :", a/b)
except ZeroDivisionError as e:
    print("Found Error :",e)
else:
    print("Division Completed!")
finally:
    print("Ye To Hamesha Chalega")
print("Program Completed!")


# RAISE an artificial error
age = int(input("Enter Your Age : "))
if age<18:
    raise ZeroDivisionError("You Sould Be 18+")
print("Welcome!")

# Create Customer Error

class AgeError(Exception):
    pass

age = int(input("Enter Your Age : "))
if age<18:
    raise AgeError("You Sould Be 18+")
print("Welcome!")

"""
