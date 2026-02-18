"""
Errors:- A mistake in a piece of code
Types of Errors:-
1- Syntax Error
    A mistake in your codes
a = 10
print "Value :",a

# it will raise an Syntax error, because of ( ) in print functions
Syntax error can be flaged by interpreter
# In case of Syntax error program will not run
It is a Syntax error and you need to fix it.

2- Runtime Error / Exception
    An error at the time of running program

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
print( "Division A/B :",a/b )
print("Division Complete!")

# in this case if you will enter the value of b  0
then it will raise an runtime error and crash the program
# this error can not flaged by interpreter
It is a runtime error and you can handle it.

3- Symantic Error (A human error in his logic)

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
print("Addition :",a*b)

it can not flaged by interpreter and it do not harm
to the running error
it will not generate the desired output
It is a human error and you need to fix it.

------------------------------------------------------

Exception Handling:-
    try , except , finally , else

try:
    write your code here, where you have doubt of error
except:
    write alternate code here

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print( "Division A/B :",a/b )
except:
    print("Division is not possible")
print("Program Complete!")


try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print( "Division A/B :",a/b )
except:
    print("Division is not possible")
print("Program Complete!")


try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print( "Division A/B :",a/b )
    print( "Done!" )
except:
    print("Division is not possible")
print("Program Complete!")



try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print( "Division A/B :",a/b )
except ZeroDivisionError as e:
    print("Error :",e)
print("Program Complete!")



# Multiple Except

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print( "Division A/B :",a/b )
except ZeroDivisionError as e:
    print("1Error :",e)
except ValueError as e:
    print("2Error :",e)
print("Program Complete!")


try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print( "Division A/B :",a/b )
    print(a[1])
except ZeroDivisionError as e:
    print("1Error :",e)
except ValueError as e:
    print("2Error :",e)
except Exception as e:
    print("3Error :",e)
print("Program Complete!")



# Exception class can handle any type of error

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print( "Division A/B :",a/b )
    print(a[1])
except Exception as e:
    print("3Error :",e)
print("Program Complete!")


"""

