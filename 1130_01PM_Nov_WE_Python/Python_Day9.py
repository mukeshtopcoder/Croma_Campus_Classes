"""
Nested Loop

# WAP to check a number is prime.
count = 0
num = int(input("Enter A Number : "))
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print(num)

# WAP to find all Prime Numbers from 1 to 100

for num in range(1,101):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print(num)

# PATTERN PROGRAMMING

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


for i in range(1,6): 
    for j in range(1,6): 
        print("*",end="")
    print()


*
**
***
****
*****


for i in range(1,6):  # rows  
    for j in range(1,i+1):        
        print("*",end="")
    print()


    *
   **
  ***
 ****
*****

for i in range(1,6):
    for s in range(5,i,-1):
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
    for s in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):        
        print("* ",end="")
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

k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end="")
        k=k+1
    print()

"""
