"""
if , if_else , Nested if_else , elif , complex condition

a = 23
b = 45
c = 56
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)


for loop
for variable_name in range(start,stop,step):
    statement

Example:-
num = int(input("Enter A Number : "))
for a in range(1,11):
    if (a*num)%2==0:
        print(a*num)

# WAP to print only factors of a number.
# HINT:-   12 =>  1,2,3,4,6,12

num = 12
for i in range(1,num+1):
    if num%i==0:
        print(i)

# WAP to count only factors of a number.
# HINT:-   12 =>  1,2,3,4,6,12   => 6

num = int(input("Enter A Number : "))
count = 0
for i in range(1,num+1):
    if num%i==0:
        print(i)
        count=count+1
print("Total Factors :",count)

# WAP to count only factors of a number.
# HINT:-   12 =>  1,2,3,4,6,12   => 6

num = int(input("Enter A Number : "))
count = 0
for i in range(1,num+1):
    if num%i==0:
        print(i)
        count=count+1
print("Total Factors :",count)
if count==2:
    print("Prime Number")
else:
    print("Not Prime Number")
    
while loop

initilization
while condition:
    statements
    incr/decr

Example
a = 1
while a<5:
    print("Hello")
    a = a+1

# Counting from 1 to 12
num = 12
a = 1
while a<=num:
    print(a)
    a = a+1


# Table Print
num = 12
a = 1
while a<=10:
    print(a*num)
    a = a+1

# Find all factors of a number
num = 12
a = 1
while a<=num:
    if num%a==0:
        print(a)
    a = a+1


# Count all factors of a number
num = 22
a = 1
count = 0
while a<=num:
    if num%a==0:
        print(a)
        count=count+1
    a = a+1
print("Total Factors :",count)


# Check Prime Number
num = 17
a = 1
count = 0
while a<=num:
    if num%a==0:
        print(a)
        count=count+1
    a = a+1
print("Total Factors :",count)
if count==2:
    print("prime")
else:
    print("not prime")


ch = "y"
while ch in "Yy":
    name = input("Enter Employee Name : ")
    add = input("Enter Employee Address : ")
    ch = input("Do You Want To Add More Employee(Y/N) : ")

# WAP to reverse a number.

num = 123
num = int(str(num)[::-1])
print(num)

# WAP to add all digits of a number
num = 736
add = 0
while num>0:
    rem = num%10
    add = add+rem
    num = num//10
print(add)

# WAP to reverse a number

num = 456
add = 0
while num>0:
    rem = num%10
    add = add*10+rem
    num = num//10
print(add)
"""

