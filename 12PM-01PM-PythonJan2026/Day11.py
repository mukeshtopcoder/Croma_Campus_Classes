"""
Pattern Building

*****
*****
*****
*****
*****

print("*****\n"*5)

*
**
***
****
*****

for i in range(1,6):
    print("*"*i)

    *
   **
  ***
 ****
*****

for i in range(1,6):
    print(" "*(5-i)+"*"*i)

    *
   * *
  * * *
 * * * * 
* * * * *

for i in range(1,6):
    print(" "*(5-i)+"* "*i)

*****
****
***
**
*

for i in range(5,0,-1):
    print("*"*i)

*****
 ****
  ***
   **
    *

for i in range(5,0,-1):
    print(" "*(5-i)+"*"*i)

* * * * *
 * * * *
  * * *
   * *
    *

for i in range(5,0,-1):
    print(" "*(5-i)+"* "*i)


1
12
123
1234
12345

st = ""
for i in range(1,6):
    st = st+str(i)
    print(st)

1
22
333
4444
55555

for i in range(1,6):
    print(str(i)*i)


A
AB
ABC
ABCD
ABCDE

st = ""
for i in range(1,6):
    st = st + chr(i+64)
    print(st)

A
BB
CCC
DDDD
EEEEE

for i in range(1,6):
    print(chr(i+64)*i)

0
909
89098
7890987
678909876
56789098765
4567890987654
345678909876543
23456789098765432
1234567890987654321

st = "0"
for i in range(10,0,-1):
    if i!=10:
        st = str(i) + st + str(i)
    print(st)

Que 16
num = 1
while num!=0:
    num = int(input("Enter A Number : "))
else:
    print("Bye")


Que 20
import random

num = random.randint(1,6)
while True:
    ch = int(input("We Generate A Number Guess The Number : "))
    if ch==num:
        print("You Win")
        break
    else:
        print("Try Again!")

Que 24

bal =13703
while True:
    print("\n\t\t  ATM MACHINE")
    print("\n\t\t1. Check Balance")
    print("\t\t2. Deposit Balance")
    print("\t\t3. Withdrawl Balance")
    print("\t\t4. Exit")
    ch = int(input("\n\t\tEnter Your Choice: "))
    if ch==4:
        print("Bye_Bye")
        break
    elif ch==1:
        print("\n\t\tCurrent Balance :",bal)
    elif ch==2:
        b = int(input("Enter Amount to Deposit : "))
        bal = bal+b
        print("Balance Deposit Successfully!")

Que 26 IF_ELSE

unit = int(input("Enter Usage Electricity UNITS : "))
if unit<100:
    amt = unit*5
else:
    if unit<500:
        amt = unit*7
    else:
        if unit<1000:
            amt = unit*9
        else:
            amt = unit*10

print("Bill Amount :",amt)

"""
