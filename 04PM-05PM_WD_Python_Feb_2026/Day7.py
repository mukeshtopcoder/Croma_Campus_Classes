"""
Conditonal Statements
Loopings
    for , while

looping:- is use to execute a task again and again for a finite time

for loop:-

Syntax:-
    for variable_name in range(start, stop , step):
            statements

Example

print( *range(1,51,1) )



for i in range(1,5,1):
    print("Hello")


for i in range(1,5,1):
    print(i)


for i in range(1,11,1):
    print(i)

for i in range(1,11,2):
    print(i)


for i in range(2,21,2):
    print(i)


print(  *range( 2,21,2 )  )


for i in range(1,11,3):
    print(i)


# By default step => 1
for i in range(1,5):
    print(i)


# By default step => 1
for i in range(5,9):
    print(i)


# By default step => 1
# By default start => 0
for i in range(5):
    print(i)


# WAP to print counting from 1 to 10
for i in range(1,11):
    print(i)

# WAP to print counting from 1 to N

n = int(input("Enter Range From 1 to : "))
for i in range(1,n+1):
    print(i)


# WAP to print table of a number

num = int(input("Enter A Number : "))
for i in range(1,11):
    print(i*num)



# WAP to print factors of a number
# HINT:-   12 =>  1,2,3,4,6,12 (factors)

num = int(input("Enter A Number : "))
for i in range(1,num+1):
    if num%i==0:
        print(i)


# WAP to count the factors of a number
HINT:   12 =>  1,2,3,4,6,12  => 6 factors

count = 0
num = int(input("Enter A Number : "))
for i in range(1,num+1):
    if num%i==0:
        print(i)
        count = count+1
print("Total factors :",count)


# WAP to check a number is Prime or not.

count = 0
num = int(input("Enter A Number : "))
for i in range(1,num+1):
    if num%i==0:
        print(i)
        count = count+1
print("Total factors :",count)
if count==2:
    print("Prime")
else:
    print("Not Prime")




# break:-   break exit from current loop
for i in range(1,11):
    print(i)
    if i==4:
        break



# break:-   break exit from current loop
for i in range(1,11,2):
    print(i)
    if i==4:
        break



# break:-   break exit from current loop
for i in range(1,6,2):
    print(i)
    if i==4:
        break



# break:-   break exit from current loop
for i in range(1,6):
    if i==4:
        break
    print(i)


# break:-   break exit from current loop
for i in range(1,6,2):
    if i==4:
        break
    print(i)


# continue:- continue will take your cursor to the
# next itteration

for i in range(1,6):
    if i==4:
        continue
    print(i)


# continue:- continue will take your cursor to the
# next itteration

for i in range(1,6):
    if i==3:
        continue
    print(i)


# continue:- continue will take your cursor to the
# next itteration

for i in range(1,6):
    print(i)
    if i==3:
        continue



# continue:- continue will take your cursor to the
# next itteration

for i in range(1,6):
    if i<=3:
        continue
    print(i)



# pass :- pass do nothing

for i in range(1,6):
    if i<=3:
        pass
    print(i)


# pass will simply pass the cursor to the next line
if 10>5:
    pass

print("Hello")


"""

