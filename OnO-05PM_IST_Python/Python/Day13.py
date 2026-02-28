
"""

 count = 0
n =int(input("Enter range from 1 to : "))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        count = count+1
print("Total Factor:",count)
if count==2:
    print("prime")
else:
    print("Non Prime")

"""
"""
Write a program to check whether a number is a palindrome.

Number 521
"""
"""
num = int(input("Enter a number: "))
add = 0
while num>0:
    rem = num%10
    add = add*10+rem
    num = num//10

print(add)

"""
"""
Write a program to print the Fibonacci series up to n terms.

0,1,1,2,3,5,8,13
"""
"""
a = 1
num = int(input("Enter a number: "))
b = 0
c = 1
while a<num:
    d = b+c
    print(d)
    b = c
    c = d
    a = a+1



Number Guessing Game

import random

guess = random.randint( 1,6 )
num = 0
while True:
    num = int(input("Guess A Number Between 1 to 6 :"))
    if num==guess:
        print("You Got it! WIN!")
        break
    print("\n\tTry Again!")



Write a program to simulate an ATM menu
using a while loop.


while True:
    print("\n1. Cash Withdrawl")
    print("2. Check Balance")
    print("3. Change PIN")
    print("0. Exit")
    ch = int(input("Enter Your Choice : "))
    if ch==0:
        print("Bye Bye")
        break


"""

