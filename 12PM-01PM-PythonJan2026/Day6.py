"""
Conditional Statements
if , if_else , Nested if_else , elif , Complex Condition
Looping:-   for , while

if
if condition:
    True_statement

if 10>5:
    print("Hello India")

if 10>50:
    print("Hello India")

if 10>50:
    print("Hello India")
print("Hello World")


if_else
if condition:
    True_statement
else:
    False_statement


if 10>5:
    print("Hello")
else:
    print("Bye")


if 10>50:
    print("Hello")
else:
    print("Bye")


WAP to find greater value between two

n1 = 100
n2 = 20
if n1>n2:
    print("Greatest Value :",n1)
else:
    print("Greatest Value :",n2)


WAP to check an enetered number is even/odd

num = int(input("Enter A Number : "))
if num%2==0:
    print("Even")
else:
    print("Odd")


Nested if_else
if condition:
    if condition:
        True_Statement
    else:
        False_statement
else:
    if condition:
        True_statement ...

WAP to check a number is positive , negative or zero.

num = 33
if num>0:
    print("Positive")
else:
    if num<0:
        print("Negative")
    else:
        print("Zero")

WAP to check an entered character is vowel or consonant
HINT:-    A E I O U

ch = 'E'
if ch=='A':
    print("Vowel")
else:
    if ch=='E':
        print("Vowel")
    else:
        if ch=='I':
            print("Vowel")
        else:
            if ch=="O":
                print("Vowel")
            else:
                if ch=='U':
                    print("Vowel")
                else:
                    print("Consonant")



WAP to check an entered character is vowel or consonant
HINT:-    A E I O U

ch = input("Enter A Character : ")
if ch=='A':
    print("Vowel")
elif ch=='E':
    print("Vowel")
elif ch=='I':
    print("Vowel")
elif ch=="O":
    print("Vowel")
elif ch=='U':
    print("Vowel")
else:
    print("Consonant")

WAP to check an entered character is vowel or consonant
HINT:-    A E I O U

ch = input("Enter A Character : ")
if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("Vowel")
else:
    print("Consonant")


WAP to check an entered character is vowel or consonant
HINT:-    A E I O U

ch = input("Enter A Character : ")
if ch in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")


# WAP to find greater value among three

n1 = 100
n2 = 300
n3 = 200
if n1>n2:
    if n1>n3:
        print(n1)
    else:
        print(n3)
else:
    if n2>n3:
        print(n2)
    else:
        print(n3)


n1 = 100
n2 = 30
n3 = 20
if n2>n1 and n2>n3:
    print(n2)
elif n3>n1 and n3>n2:
    print(n3)
else:
    print(n1)


WAP to calculate gross salary of an employee where HRA
is 20% and DA is 30% of his basic salary if the basic
salary is above 30000 otherwise HRA and DA are 15% and 20%
HINT:- Gross_Salary  = Basic_Salary + HRA + DA

"""
bs = float(input("Enter Basic Salary : "))
if bs>30000:
    hra = bs*0.20
    da = bs*0.30
else:
    hra = bs*0.15
    da = bs*0.20






