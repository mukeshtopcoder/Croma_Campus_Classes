"""
Nested Loop:-
for variable_name in range(start,stop,step):
    for variable_name in range(start,stop,step):
        statements

# WAP to count all prime numbers from 1 to 100
countPrime = 0
for num in range(1,101):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        countPrime+=1
        print(num)
print("Total Prime Numbers : ",countPrime)


# Count neg , zero and positive
pos = 0
neg = 0
zero = 0
for i in range(1,11):
    num = int(input(f"Enter {i} Number : "))
    if num>0:
        pos+=1
    elif num<0:
        neg+=1
    else:
        zero+=1
print("Postive : ",pos)
print("Negative : ",neg)
print("Zero : ",zero)


# WAP to count number of vowel in a string
name = "AMANKUMAR"
vowel = 0
for i in name:
    if i in "AEIOUaeiou":
        vowel+=1
print("Total Vowels :",vowel)


# WAP to count number of vowel in a string
name = "AMANKUMAR"
vowel = 0
vowels = "AEIOUaeiou"
for char in name:
    if char in vowel:
        vowel+=1
print("Total Vowels :",vowel)


for (iteration)

# WAP to count number of vowel in a string
name = "AMANKUMAR"
vowel = 0
vowels = "aeiou"
for char in name.lower():
    if char in vowels:
        vowel+=1
print("Total Vowels :",vowel)


# Fibonacci Series
# 0 1 1 2 3 5 8 13 21 34 ...

a = 0
b = 1
for i in range(10):
    c = a+b
    print(c,end="  ")
    a = b
    b = c

# WAP TO CHECK PALIDROME
num = 121
copy = num
rev = 0
print("Number :",num)
while num>0:
    rem = num%10
    rev = rev*10+rem
    num = num//10
print("Reverse :",rev)
if rev==copy:
    print("Palindrome")
else:
    print("Not Palindrome")
    

# Print all Palidromic Number from 100 to 200

for num in range(100,201):
    copy = num
    rev = 0
    while num>0:
        rem = num%10
        rev = rev*10+rem
        num = num//10
    if rev==copy:
        print(copy)

# Pattern Programming

*****
*****
*****
*****
*****


for i in range(5):
    print("*****")


for i in range(1,6):    
    for j in range(1,6):  
        print("*",end="")
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


1
23
456
78910

k = 1
for i in range(1,5):    
    for j in range(1,i+1): 
        print(k,end="")
        k+=1
    print()



1
01
010
1010
10101


k = 1
for i in range(1,6):    
    for j in range(1,i+1): 
        print(k%2,end="")
        k+=1
    print()


    *
   **
  ***
 ****
*****

for i in range(1,6):  
    for k in range(5,i,-1):         
        print(end=" ")
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
        print(end=" ")
    for j in range(1,i+1):
        print("* ",end="")
    print()


ASCII
A => 65 , B => 66 , C => 67 ------ Z => 90
a => 97 , b => 98 , c => 99 ------ z => 122


A
AB
ABC
ABCD
ABCDE

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

k=65
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(k),end="")
        k+=1
    print()


k=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(k),end="")
        k+=1
    print()

12344321
123**321
12****21
1******1

for i in range(4,0,-1):  
    for j in range(1,5):  
        if j<=i:
            print(j,end="")
        else:
            print("*",end="")
    for j in range(4,0,-1):  
        if j<=i:
            print(j,end="")
        else:
            print("*",end="")
    print()

"""
