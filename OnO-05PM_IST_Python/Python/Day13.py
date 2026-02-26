"""
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

