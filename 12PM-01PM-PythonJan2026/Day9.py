"""
WHILE LOOP
Syntax:-
initilization
while condition:
    statements
    incr/decr

Example:-
a = 1
while a<5:
    print("Hello India")
    a = a+1

a = 1
while a<=5:
    print("Hello India")
    a = a+1

# WAP TO PRINT COUNTING FROM 1 TO 10

a = 1
while a<=10:
    print(a)
    a = a+1

num = int(input("Enter A Number : "))
a = 1
while a<=num:
    print(a)
    a = a+1

# break , continue , pass , else

num = 6
a = 1
while a<=num:
    print(a)
    if a==3:
        break
    a = a+1
else:
    print("Hello")

num = 6
a = 1
while a<=num:
    print(a)
    a = a+1
else:
    print("Hello")


num = 6
a = 1
while a<=num:
    if a==3:
        continue
    print(a)
    a = a+1
else:
    print("Hello")


a = 1
while a<=6:
    a=a+1 
    print(a)


a = 1
while a<=6:
    a=a+1
    if a==3:
        break
    print(a)


a = 1
while a<=6:
    a=a+1
    if a==3:
        continue
    print(a)


# WAP to check a number is prime or not

num  = 17
count = 0

a = 1
while a<=num:
    if num%a==0:
        count=count+1
    a=a+1
if count==2:
    print("Prime")
else:
    print("Not Prime")

# WAP to add all digits of a number
# 123   =>   1+2+3 => 6 Answer

num = int(input("Enter A Number : "))
add = 0
a = 1
while a<=num:
    rem = num%10  
    add = add+rem
    num = num//10
print(add)

# WAP to reverse a number
HINT :-    123   =>  321

num = int(input("Enter A Number : "))
add = 0
a = 1
while a<=num:  
    rem = num%10  
    add = add*10+rem 
    num = num//10
print("Reverse Number  :",add)


# WAP to check a number is palindrome
# HINT:-   123 = Reverse 321 (Not Palindrome)
# HINT:-   121 = Reverse 121 (Palindarome)

num = int(input("Enter A Number : "))
copy = num
add = 0
a = 1
while a<=num:  
    rem = num%10  
    add = add*10+rem 
    num = num//10
print("Reverse Number  :",add)
if copy==add:
    print("Palindrome")
else:
    print("Not Palindrome")

    
"""

