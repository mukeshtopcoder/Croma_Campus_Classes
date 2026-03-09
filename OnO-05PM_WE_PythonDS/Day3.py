"""
Conditional Statements
if , if_else, Nested if_else , elif , Complex Conditions
looping statments :-   for , while


if condition:
    True_statement

if 10>5:
    print("Hello India")

if 10>50:
    print("Hello India")

if_else
if condition:
    True_Statement
else:
    False_Statement


if 10>5:
    print("Hello")
else:
    print("Bye")


# WAP to check an entered number is even/odd

num = int(input("Enter A Number : "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")


# WAP to find which number is greater b/w two

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
if a>b:
    print("Greater Value :",a)
else:
    print("Greater Value :",b)


Nested if_else
if condition:
    if condition:
        True_Statement
    else:
        False_Statement
else:
    if condition:
        True_Statement
    else:
        False_Statement


# WAP to check an entered number is positive, negative
or zero

num = int(input("Enter A Number : "))
if num>0:
    print("Positive")
else:
    if num<0:
        print("Negative")
    else:
        print("Zero")


# WAP to check which number is greater b/w two or equal

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
if a>b:
    print("Greater Value :",a)
else:
    if b>a:
        print("Greater Value :",b)
    else:
        print("Numbers Are Equal")

# WAP to check a character is vowel or consonant
# HINT:- A,E,I,O,U are the vowels

ch = input("Enter A Character : ")
if ch=='A':
    print("Vowel")
else:
    if ch=='E':
        print("Vowel")
    else:
        if ch=='I':
            print("Vowel")
        else:
            if ch=='O':
                print("Vowel")
            else:
                if ch=='U':
                    print("Vowel")
                else:
                    print("Consonant")



# WAP to check a character is vowel or consonant
# HINT:- A,E,I,O,U are the vowels


ELIF


ch = input("Enter A Character : ")
if ch=='A':
    print("Vowel")
elif ch=='E':
    print("Vowel")
elif ch=='I':
    print("Vowel")
elif ch=='O':
    print("Vowel")
elif ch=='U':
    print("Vowel")
else:
    print("Consonant")


# WAP to check a character is vowel or consonant
# HINT:- A,E,I,O,U are the vowels

Complex Condition
You use logical operators to write all the condition together

ch = input("Enter A Character : ")
if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("Vowel")
else:
    print("Consonant")


ch = input("Enter A Character : ")
if ch in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")




Looping statements
for
if you have a task and you want perform that task again
and again for a finite times so you can use loop

FOR
syntax:-

for variable_name in range(start, stop , step):
    statements

Example:-


print( *range(1,5,1) )
print( *range(2,21,2) )


for a in range(1,5,1):
    print("Hello")


for a in range(1,5,1):
    print(a)

for a in range(1,11,1):
    print(a)


for a in range(2,21,2):
    print(a)


for a in range(1,11,3):
    print(a)


# By default step => 1
for a in range(1,5):
    print(a)


# By default step => 1
for a in range(5,9):
    print(a)



# By default step => 1
# By default start => 0
for a in range(5):
    print(a)


# WAP to print counting from 1 to 10
for i in range(1,11):
    print(i)

# WAP to print counting from 1 to N

n = int(input("Enter Range From 1 To : "))
for i in range(1,n+1):
    print(i)


# WAP to print all factors of a number
HINT:-  12  =>  1,2,3,4,6,12

n = int(input("Enter A Number : "))
for i in range(1,n+1):
    if n%i==0:
        print(i)

# WAP to count all the factors of a number
HINT:-  12  =>  1,2,3,4,6,12  => 6 factors

count = 0
n = int(input("Enter A Number : "))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        count+=1
print("Total Factors :",count)


# WAP to check a number is Prime or Not
count = 0
n = int(input("Enter A Number : "))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        count+=1
print("Total Factors :",count)
if count==2:
    print("Prime Number")
else:
    print("Not Prime Number")




count = 0
n = int(input("Enter A Number : "))
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("Prime Number")
else:
    print("Not Prime Number")


"""

