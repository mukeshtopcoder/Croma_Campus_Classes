"""
break , continue , pass , else

# break:- break will exit the current loop
for i in range(1,6):
    if i==3:
        break
    print(i)


# break:- break will exit the current loop
for i in range(1,6):
    print(i)
    if i==3:
        break


# continue :- continue will take the cursor to the next
# itteration or to the next loop's value
# continue will skip the upcoming code and go to the loop again
for i in range(1,6):
    if i==3:
        continue
    print(i)



# continue will skip the upcoming code and go to the loop again
for i in range(1,6):
    print(i)
    if i==3:
        continue

# pass : pass do nothing, pass will pass cursor to the
# next line
for i in range(1,6):
    if i==3:
        pass
    print(i)


ELSE with for loop

for i in range(1,6):
    print(i)
else:
    print(0)


for i in range(1,6):
    if i==3:
        break
    print(i)
else:
    print(0)

# it will not go to the else part

for i in range(1,6):
    if i==3:
        continue
    print(i)
else:
    print(0)


for i in range(1,6):
    print(i)
    if i==5:
       break
else:
    print(0)


WHILE LOOP

intilization
while condition:
    Statements
    incr/dec

Example
a = 1
while a<=5:
    print("Hello")
    a = a+1


a = 1
while a<=5:
    print(a)
    a = a+1


a = 1
while a<=10:
    print(a)
    a = a+2


# WAP to print counting from 1 to 10
a = 1
while a<=10:
    print(a)
    a = a+1

# WAP to print counting from 1 to N

n = int(input("Print Counting From 1 to : "))
a = 1
while a<=n:
    print(a)
    a = a+1


# WAP to find all factors of a number
HINT:-   12 => 1,2,3,4,6,12

n = int(input("Enter A Number : "))
a = 1
while a<=n:
    if n%a==0:
        print(a)
    a = a+1

# WAP to count the factors
HINT:- 12 => 1,2,3,4,6,12  =>  6 factors

n = int(input("Enter A Number : "))
a = 1
count = 0
while a<=n:
    if n%a==0:
        print(a)
        count+=1
    a = a+1
print("Total Factors :",count)


# WAP to check a number is prime or not

n = int(input("Enter A Number : "))
a = 1
count = 0
while a<=n:
    if n%a==0:
        print(a)
        count+=1
    a = a+1
print("Total Factors :",count)
if count==2:
    print("Prime")
else:
    print("Not Prime")


break , continue , pass , else

a = 1
while a<=5:
    if a==3:
        break
    print(a)
    a=a+1


"""

