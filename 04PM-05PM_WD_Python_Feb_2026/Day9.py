"""
# NESTED FOR LOOP

# WAP to check a number is Prime or not

num = 17
count = 0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("Prime")
else:
    print("Not Prime")


# WAP to find all prime numbers from 1 to 100

for num in range(1,101):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print(num)

# PATTERN BUILDING

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


*****
*****
*****
*****
*****


for i in range(1,6):
    print("*****")



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

1
23
456
78910

k = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end="")
        k=k+1
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
        k=k+1
    print()



k = True
for i in range(1,6):
    for j in range(1,i+1):
        if k:
            print(1,end='')
            k=False
        else:
            print(0,end='')
            k= True
    print()


"""

