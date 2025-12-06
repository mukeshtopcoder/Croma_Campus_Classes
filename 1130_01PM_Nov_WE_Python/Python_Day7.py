"""
Conditional Statements:-
if , if_else , Nested if_else , elif , complex condition
Looping:-  for and while

if
Syntax:-
if condition:
    your code/statement (True Statement)

Example:-
if 10>5:
    print("Hello India")


if 10>50:
    print("Hello India")


if 10>50:
    print("Hello India")
print("Hello World")


IF_ELSE
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

# WAP TO CHECK AN ENTERED NUMBER IS Even/Odd

num = int(input("Enter A Number : "))
if num%2==0:
    print("Even Number")
else:
    print("Odd Number")

# WAP to find greater value between two


n1 = int(input("Enter A Number : "))
n2 = int(input("Enter B Number : "))
if n1>n2:
    print(n1)
else:
    print(n2)

# WAP to validate a candidate is eligible for vote or not
# HINT:-   candidate is eligible if he is 18 or 18+

age = int(input("Enter Candidate Age : "))
if age>17:
    print("Eligible for Vote")
else:
    print("Not Eligible")

Nested if else
if condition:
    if condition:
        true_statement
    else:
        false_statement
else:
    if condition:
        true
    else:
        false

# WAP to check a number is positive, negative or zero
num = int(input("Enter A Number : "))
if num>0:
    print("Positive")
else:
    if num<0:
        print("Negative")
    else:
        print("Zero")

# WAP to check a character is vowel or consonant
# HINT:-  A,E,I,O,U are the vowels and rest are consonant

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


# ELIF => else_if
if condition:
    true_statement
elif condition:
    true_statement
elif condition:
    true_statement
elif condition:
    true_statement    
else:
    false_statement



# WAP to check a character is vowel or consonant
# HINT:-  A,E,I,O,U are the vowels and rest are consonant

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


# Complex Condition
# WAP to check a character is vowel or consonant
# HINT:-  A,E,I,O,U are the vowels and rest are consonant

ch = input("Enter A Character : ")
if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("Vowel")
else:
    print("Consonant")


# WAP to check a character is vowel or consonant
# HINT:-  A,E,I,O,U are the vowels and rest are consonant

ch = input("Enter A Character : ")
if ch in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")

"""
