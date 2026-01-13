"""
Programming Questions Related to Nested Loop
A loop inside a loop is called Nested Loop

# WAP to check a Number is prime or not

num = 21
count = 0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(num)
else:
    print("Not Prime")

# WAP to find all prime numbers from 1 to 100

for num in range(1,101):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)

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


print("*****\n*****\n*****\n*****\n*****")


print("*****\n"*5)

Nested Loop

*****
*****
*****
*****
*****

for i in range(1,6):      # rows 
    for j in range(1,6):      # columns/values
        print("*",end='')
    print()


*
**
***
****
*****

for i in range(1,6):      # rows 
    for j in range(1,i+1):      # columns/values
        print("*",end='')
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

num = 0
for i in range(1,5):  
    for j in range(1,i+1):   
        print(num,end="")
        num = num+1
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


12344321
123**321
12****21
1******1

for i in range(4,0,-1):
    for j in range(1,5):
        if j>i:
            print("*",end="")
        else:
            print(j,end="")
    for j in range(4,0,-1):
        if j>i:
            print("*",end="")
        else:
            print(j,end="")
    print()


"""
  
