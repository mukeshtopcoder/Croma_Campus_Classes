"""
Looping:- for and while
for loop
syntax:-

for variable_name in range(start,stop,step):
    statements

Example:-
for a in range(1,7,1):
    print("Hello India")

for a in range(1,7,1):
    print(a)


# WAP to print counting from 1 to 10

for a in range(1,11,1):
    print(a)


for a in range(1,11,2):
    print(a)
# 1 3 5 7 9


for a in range(1,11,3):
    print(a)
# 1 4 7 10


for a in range(1,5,1):
    print(a)
# 1234

for a in range(1,5):    # default step value is 1
    print(a)


for a in range(1,5):    # default step value is 1
    print(a)


for a in range(5,9):
    print(a)
# 5 6 7 8


for a in range(5):    # default start value is 0
    print(a)
# 0 1 2 3 4


for a in range(3):    # default start value is 0
    print(a)
# 0 1 2 

# WAP to print counting from 1 to 10
for a in range(1,11):
    print(a)


# WAP to print counting from 1 to N
num = int(input("Print Counting From 1 To : "))
for a in range(1,num+1):
    print(a)



# WAP to print table of a number.
num = int(input("Enter Number To Print Table: "))
for a in range(1,11):
    print(a*num)



# WAP to print all the factors of a number
# HINT:-   12 =>  1,2,3,4,6,12
num = 12
for a in range(1,num+1):
    if num%a==0:
        print(a)


# WAP to print all the factors of a number
# HINT:-   12 =>  1,2,3,4,6,12
num = int(input("Enter A Number : "))
for a in range(1,num+1):
    if num%a==0:
        print(a)


# WAP to count the factors of a number
# HINT:-   12 =>  1,2,3,4,6,12  =>  6 factors
count = 0
num = int(input("Enter A Number : "))
for a in range(1,num+1):
    if num%a==0:
        print(a)
        count = count+1
print("Total Factor :",count)


# WAP to check a number is prime
count = 0
num = int(input("Enter A Number : "))
for a in range(1,num+1):
    if num%a==0:   
        print(a)
        count = count+1
print("Total Factor :",count)
if count==2:
    print("Prime")
else:
    print("Not Prime")
    
"""
