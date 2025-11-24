"""
# Advance 6 (MAP)

students = [{"name":'Aman','marks':98},{'name':'Ritu','marks':76}]

names = list( map(lambda x:x['name'],students) )
print(names)


li = [23,67,90,67,34,78,89]
checkEven = lambda x:"Even" if x%2==0 else "Odd"
newli = list( map(checkEven,li) )
print(newli)


Exception Handling:-
Types of Error:-
1) Syntax Error / Compile Time Error
a = 10
print("Value of A is"a)
We forget to put a comma
You need to fix this error otherwise a program will not run

2) Logical Error / Run Time Error

a = 10
b = 0
print("Start")
print( a/b )
print("End")

this is run time error mostly depend on user input,
Thi error is also called exception
and we can handle it at run time so we can by pass this error
so our program will not crash

3) Symmetric Error
    a = 2
    b = 2
    print("Addition :",a*b)

This is human error or error in logic
you need to find it and fix it


Exception handling:-
try , except , finally , else , raise

when you have a doubt on any piece code, write that code
in try block it will run complete if there is no error
and take you to the except block if facing any issue.


a = 10
b = 0
print("Start")
try:
    print( a/b )
except:
    print("Division Not Possible")
print("End")



a = 10
b = 0
print("Start")
try:
    print( a/b )
except ZeroDivisionError as e:
    print("Error :",e)
print("End")



a = 10
b = 4
li = [23,67]
print("Start")
try:
    print( a/b )
    print(li[3])
except IndexError as e:
    print("Error :",e)
print("End")


a = 10
b = 4
li = [23,67]
m = '20'
print("Start")
try:
    print( a/b )
    print(li[1])
    print(m+20)
except IndexError as e:
    print("Error :",e)
except ZeroDivisionError as e:
    print("Error :",e)
except Exception as e:
    print("Error :",e)
print("End")



a = 10
b = 4
li = [23,67]
m = '20'
print("Start")
try:
    print( a/b )
    print(li[1])
    print(m+20)
except Exception as e:
    print("Error :",e)
print("End")



else block:-
If you face any error, try will take you to the except block
and if there is no error it will take you to else block

a = 10
b = 0
print("Start")
try:
    print( a/b )
except Exception as e:
    print("Error :",e)
else:
    print("Program Complete!")
print("End")


a = 10
b = 0
print("Start")
try:
    print( a/b )
except TypeError as e:
    print("Error :",e)
else:
    print("Program Complete!")
finally:
    print("Ye to hamesha chalega")
print("End")


# You can raise a custom exception

age = int(input("Enter Age : "))
if age<18 :
    raise ZeroDivisionError("Age should be 18+")
print("Login!")


class AgeError(Exception):
    pass

age = int(input("Enter Age : "))
if age<18 :
    raise AgeError("Age should be 18+")
print("Login!")


assert  Keyword

age = int(input("Enter Age : "))
assert age>17 
print("Login!")


age = int(input("Enter Age : "))
assert age>17, "Age should be 18+"
print("Login!")
"""
