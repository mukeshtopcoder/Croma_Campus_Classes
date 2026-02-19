"""
Exception Handling:-
try , except
try:
    write your code here where you have a doubt of an error
except:
    alternative code if any error occur

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print( "Division :",a/b )
except:
    print("Found Error!")

    

else keyword

try:
    write your code here where you have a doubt of an error
except:
    alternative code if any error occur
else:
    write your code here, which will execute if there is no error
    
a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print( "Division :",a/b )
except:
    print("Found Error!")
else:
    print("Division Complete")
print("Program Complete!")


finally

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print( "Division :",a/b )
except ValueError as e:
    print("Found Error!")
else:
    print("Division Complete")
finally:
    print("Ye to Hamesha Chalega")
print("Program Complete!")


raise
raise keyword => is use to raise an error

age = int(input("Enter Your Age : "))
if age<18:
    raise ValueError("Age Should Be 18+")
print("Welcome!")


age = int(input("Enter Your Age : "))
try:
    if age<18:
        raise ValueError("Age Should Be 18+")
except ValueError as e:
    print("Error :",e)
print("Welcome!")


# CREATE CUSTOM EXCEPTION CLASS

class AgeError(Exception):
    pass
    
age = int(input("Enter Your Age : "))
if age<18:
    raise AgeError("Age Should Be 18+")
print("Welcome!")


assert
assert keyword is use to raise an error

age = int(input("Enter Age : "))
assert age>17
print("Welcome!")

age = int(input("Enter Age : "))
assert age>17 , "Age Should Be 18+..."
print("Welcome!")


assert:-
used for debugging
checks if something must be True
Maily for developers

raise:-
Used to explicitly throw an exception
Used in real error handling
for production code

"""

