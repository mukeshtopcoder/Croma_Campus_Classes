"""
Conditional Statement
if , if_else , Nested if_else , elif , complex condition
Looping:-     for , while

if
Syntax:-

if condition:
    statement

A statement under execute only if the condition is TRUE

if 10>5:
    print("Hello")

if 10>50:
    print("Hello")


if_else
Syntax:-

if condition:
    True_Statement
else:
    False_Statement


if 10>5:
    print("Hello")
else:
    print("Bye")


if 10>50:
    print("Hello")
else:
    print("Bye")


# WAP to find greater value between two

a = 10
b = 5
if a>b:
    print(a)
else:
    print(b)


# WAP to check a entered number is even/odd

num = int(input("Enter A Number : "))
if num%2==0:
    print("Even")
else:
    print("Odd")


Nested IF
Syntax:-

if condition:
    if condition:
        true_statement
    else:
        False_Statement
else:
    if condition:
        True_Statement
    else:
        False_Statement

# WAP to check a number is positive negative or zero

num = 0
if num>0:
    print("Positive")
else:
    if num<0:
        print("Negative")
    else:
        print("Zero")


# WAP to check an entered character is vowel or consonant

ch = 'M'
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


ELIF

ch = 'I'
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


Complex Condition

writing conditions using logical operator

ch = 'M'
if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("Vowel")
else:
    print("Consonant")


ch = 'e'
if ch in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")


WAP to find greater value among three

a = 10
b = 2
c = 5
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

    
"""
