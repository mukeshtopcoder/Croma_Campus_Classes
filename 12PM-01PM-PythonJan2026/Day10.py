"""
PATTERN PROGRAMMING

*****
*****
*****
*****
*****

print("*****")
print("*****")
print("*****")
print("*****")
print("*****")

for i in range(5):
    print("*****")

print("*****\n*****\n*****\n*****\n*****")

print("*****\n"*5)


for i in range(5,0,-1):
    print(i)

    
*****
*****
*****
*****
*****


for i in range(1,6):   
    for j in range(1,6): 
        print("*",end='')
    print()


*
**
***
****
*****

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()



1
12
123
1234
12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

1
22
333
4444
55555

for i in range(1,6): 
    for j in range(1,i+1):
        print(i,end="")
    print()

0
12
345
6789

val = 0
for i in range(1,5):
    for j in range(1,i+1):
        print(val,end="")
        val+=1
    print()

0
10
101
0101
01010


a = 0
b = 1
for i in range(1,6):
    for j in range(1,i+1):
        print(a,end="")
        a = a+b
        b = -b
    print()


val = 0
for i in range(1,6):
    for j in range(1,i+1):
        print(val%2,end="")
        val+=1
    print()


    *
   **
  ***
 ****
*****

for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

    *
   * *
  * * *
 * * * *
* * * * *

for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()

    
*********
*******
*****
***
*

for i in range(9,0,-2):
    for j in range(1,i+1):
        print("*",end="")
    print()


A
AB
ABC
ABCD
ABCDE
A => 1000001  => 65 , 66 , 67 , 68
a => 1100001  => 97

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()

A
BB
CCC
DDDD
EEEEE

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()

A
BC
DEF
GHIJ
KLMNO

val = 65
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(val),end="")
        val+=1
    print()

"""
