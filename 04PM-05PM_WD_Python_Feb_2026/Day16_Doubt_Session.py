"""
Q55-> IF_ELSE EXERCISE
Validate A Strong Password

Password Should Have
minimum 8 characters
At least 1 uppercase
At least 1 lowercase
At least 1 digit
At least 1 special character


p = input("Enter Your Password : ")
if len(p)<8:
    print("Password Must have At least 8 characters")
elif p.lower()==p:
    print("Password Must have At least 1 upper case")
elif p.upper()==p:
    print("Password Must have At least 1 lower case")
elif not any(char.isdigit() for char in p):
    print("Password Must have At least 1 digit")
elif not any(char in "!~@#$%^&*" for char in p):
    print("Password Must have At least 1 Special Character")
else:
    print("password is Valid!")


import random

guess = random.randint(1,6)  

while True:
    num = int(input("Select A Number (1-6) : "))
    if num==guess:
        print("You Got it\nYou Win!")
        break
    print("Wrong Guess\nTry Again!")



import random

print( random.randint(1000,9999) )
print( random.randint(100000,999999) )




a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
print("1.Addition\n2.Subraction\n3.Multiplication\n4.Division")
ch = int(input("Select Choice : "))
if ch==1:
    c = a+b
elif ch==2:
    c = a-b
elif ch==3:
    c = a*b
elif ch==4:
    c = a/b
else:
    print("Wrong Choice!")
print("Result :",c)



Fibonacci Series
0 1 1 2 3 5 8 13 21 34 etc

n = int(input("Enter Fibonacci Series Terms : "))
a = 0
b = 1
for i in range(n):
    c = a+b
    print(c)
    a = b
    b = c

    
"""

amt = int(input("Enter Order Amount : "))
dis = int(input("Enter Distance of Customer (KM) : "))
if dis<5:
    d = amt*0.05
elif dis<10:
    d = amt*0.10
elif dis<20:
    d = amt*0.15
else:
    d = amt*0.20
print("Delivery Charge : ",d)
print("Total Amount : ",amt+d)
    
