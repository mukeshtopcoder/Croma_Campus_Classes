"""
Conditional Statements
if, if_else , Nested if_else , elif , complex Cond
Looping:-   for , while

if
Syntax:-
if condition:
    True_statement

print("Hello")    # it will print always

if 10>5:
    print("Hello")   # it depends on condition

if 10>50:
    print("Hello")

if_else
Syntax:-
if condition:
    True_statement
else:
    False_statement


if 10>50:
    print("Hello")
else:
    print("Bye")


# WAP to find greater value between two.

n1 = 100
n2 = 20
if n1>n2:
    print("Greatest Value :",n1)
else:
    print("Greatest Value :",n2)


# WAP to check an entered number is Even/Odd

num = 19
if num%2 == 0:
    print("Even")
else:
    print("Odd")


Nested if_else
Syntax:-
if condition:
    if condition:
        Statement
    else:
        Statement
else:
    if condition:
        Statement
    else:
        Statement

# WAP to check an entered number is positive, negative
or zero.

num = 0
if num>0:
    print("Positive")
else:
    if num<0:
        print("Negative")
    else:
        print("Zero")

# WAP to find greater value among three

n1 = 300
n2 = 200
n3 = 500
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

# WAP to check an entered character is Vowel or Consonant

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



# WAP to check an entered character is Vowel or Consonant

ELIF

ch = 'O'
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

# WAP to check an entered character is Vowel or Consonant
Complex Condition   (using logical gates/operator)

ch = 'M'
if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("Vowel")
else:
    print("Consonant")

# WAP to check an entered character is Vowel or Consonant

ch = 'e'
if ch in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")
"""

