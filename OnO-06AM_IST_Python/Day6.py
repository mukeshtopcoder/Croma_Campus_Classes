"""
Control Statements
if , else , nested if else , elif , complex condition
loops:-  for , while

IF
Syntax:-
if condition:
    True Statements

if 10>50:
    print("Hello")
if 10>5:
    print("Hello")

if 10>50:
    print("Hello")
print("World")

if 10>5:
    print("Hello")
    print("Hello")
print("Hello")


IF_ELSE
Syntax:-
if condition:
    True Statement
else:
    False Statement

if 10>50:
    print("Hello")
else:
    print("Bye")

This syntax is called (tab) indentation

# WAP to check a number is even/odd.

num = 24
if num%2==0:
    print("Even")
else:
    print("Odd")


# WAP to find a greater value between two

n1 = 67
n2 = 356
if n1>n2:
    print(n1)
else:
    print(n2)

Nested IF_ELSE
if condition:
    if condition:
        True Statement
    else:
        False Statement
else:
    False Statement

# WAP to check a number is positive , negative or zero.
n1 = 45
if n1>0:
    print("Positive")
else:
    if n1<0:
        print("Negative")
    else:
        print("Zero")

# ELIF
if condition:
    True Statement
else:
    if condition
# Alternative
if condition:
    True Statement
elif condition:
    True Statement
elif condition:
    True Statement
else:
    False Statement

# WAP to check a number is positive , negative or zero.
n1 = -56
if n1>0:
    print("Positive")
elif n1<0:
    print("Negative")
else:
    print("Zero")

# WAP to find greater value among three.

n1 = 399
n2 = 54 
n3 = 354
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


# WAP to find greater value among three.

n1 = 240
n2 = 458
n3 = 46
if n1>n2 and n1>n3:
    print(n1)
elif n2>n3 and n2>n1:
    print(n2)
else:
    print(n3)


# WAP to check a character is vowel or consonant

ch = 'A'
if ch=='A':
    print("Vowel")
elif ch=='E':
    print("Vowel")
|
|
|
else:
    print("Consonant")

# WAP to check a character is vowel or consonant

ch = 'A'
if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("Vowel")
else:
    print("Consonant")

# WAP to check a character is vowel or consonant

ch = 'e'
if ch in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")


Looping:-
loop is a technique from which we can repeat a task again
and again

for loop
for var_name in range(start,stop,step):
    statements
print( *range(1,10,1) )
print( *range(1,10,2) )
print( *range(1,10,3) )

for var_name in range(start,stop,step):
    statements

for i in range(1,5,1):
    print("Hello")

for i in range(1,5,1):
    print(i)


# Counting from 1 to 10
for i in range(1,11,1):
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(1,11):   # by default step = 1
    print(i)

for i in range(5,11):   # by default step = 1
    print(i)


for i in range(5):   # by default step = 1
    print(i)         # by default start = 0


# WAP to print couting from 1 to 10
for i in range(1,11):
    print(i)


# WAP to print table of a number
for i in range(1,11):
    print(i*7)

# WAP to print table of a number
num = int(input("Enter A Number : "))
for i in range(1,11):
    print(i*num)


# WAP To add all natural numbers (1 to 100)
add = 0
for i in range(1,101):
    add=add+i
print(add)


# Find cube of numbers from 1 to 20
for i in range(1,21):
    print(i*i*i)

# WAP to print all factors of a number
# HINT:-  12   =>  1,2,3,4,6,12

num = 12
for i in range(1,num+1):
    if num%i==0:
        print(i)

# WAP to count all factors of a number
# HINT:-  12   =>  1,2,3,4,6,12  =>   6 factors

num = 22
count = 0
for i in range(1,num+1):
    if num%i==0:
        print(i)
        count=count+1
print("Total Factors: ",count)


# WAP to check a number is Prime or not.
# A number which has only and only 2 factors

num = 17
count = 0
for i in range(1,num+1):
    if num%i==0:
        print(i)
        count=count+1
print("Total Factors: ",count)
if count==2:
    print("Prime Number")
else:
    print("Not Prime")

num = 18
count = 0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("Prime Number")
else:
    print("Not Prime")


"""
