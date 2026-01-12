"""
Looping:- Looping is a statement which is use to perform
a task again and again
FOR , WHILE

FOR
for variable_name in range(start,stop,step):
    statement

Example:-

print( *range(1,11,1) )



for i in range(1,5,1):
    print("Hello India")

for i in range(1,5,2):
    print("Hello India")

for i in range(1,5,1):
    print(i)

for i in range(1,11,1):
    print(i)

for i in range(1,11,2):
    print(i)

# By default step = 1
for i in range(1,6):
    print(i)

# By default step = 1
for i in range(5,9):
    print(i)


# By default step = 1
# By default start = 0
for i in range(5):
    print(i)

# By default step = 1
# By default start = 0
for i in range(0):
    print(i)


# WAP to print counting form 1 to 10
for i in range(1,11):
    print(i)

# WAP to print counting from 1 to N

n = int(input("Enter Range From 1 to : "))
for i in range(1,n+1):
    print(i)

# WAP to find all factors of a number
HINT: 12:-   1,2,3,4,6,12

n = int(input("Enter Range From 1 to : "))
for i in range(1,n+1):
    if n%i==0:
        print(i)

# WAP to count the factors of a number
HINT:- 12:-  1,2,3,4,6,12 => 6 factors

count = 0
n = int(input("Enter Range From 1 to : "))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        count=count+1
print("Total Factors :",count)

# WAP to check a number is Prime
Prime:-  A number who has only and only 2 factors

count = 0
n = int(input("Enter Range From 1 to : "))
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("Prime")
else:
    print("Not Prime")

# break , continue , pass

# break :-  break exit from the current loop
for i in range(1,6):
    print(i)
    if i==3:
        break

# break :-  break exit from the current loop
for i in range(1,6):
    if i==3:
        break
    print(i)


# continue :-  continue take cursor to the next iteration/loop
for i in range(1,6):
    if i==3:           
        continue
    print(i)


# continue :-  continue take cursor to the next iteration/loop
for i in range(1,6):
    print(i) 
    if i==3:           
        continue

# pass:- Pass do nothing 
for i in range(1,6):
    if i==3:           
        pass
    print(i)

if 10>5:
    pass
print("Hello")


else

for i in range(1,6):
    print(i)
else:
    print(0)

Output: 1 2 3 4 5 0

for i in range(1,6):
    print(i)
    if i==3:
        break
else:
    print(0)

Output: 1 2 3 

for i in range(1,6): 
    if i==3:
        break
    print(i)
else:
    print(0)


for i in range(1,6): 
    if i==3:
        continue
    print(i)
else:
    print(0)
    
"""
