"""
Looping :- It perform a task again and again for a finite time
for , while

FOR
for variable_name in range(start , stop , step):
    statements

print( *range(1,5,1) )


Example:-
for a in range(1,5,1):
    print("Hello India")

for a in range(1,11,1):
    print("Hello India")

for a in range(1,11,1):
    print(a)

for a in range(1,5,1):
    print(a)

for a in range(1,11,2):
    print(a)

for a in range(1,11,3):
    print(a)

for a in range(1,11,4):
    print("Hello")

for a in range(1,11,4):
    print(a)

# By default step value is 1
for a in range(1,11):
    print(a)

# By default step value is 1
for a in range(5,9):
    print(a)

# By default step value is 1
# By default start value is 0
for a in range(5):
    print(a)

# WAP to print counting from 1 to 10
for i in range(1,11):
    print(i)

# WAP to print counting from 1 to N
n = int(input("Enter range From 1 To : "))
for i in range(1,n+1):
    print(i)

# WAP to find all factors of a number
HINT:- 12 :-  1,2,3,4,6,12
n = int(input("Enter range From 1 To : "))
for i in range(1,n+1):
    if n%i==0:
        print(i)

# WAP to count factors of a number
HINT:-  12:-    1 2 3 4 6 12  =>  6 Factors
count = 0
n = int(input("Enter range From 1 To : "))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        count = count+1
print("Total Factors :",count)

# WAP to check a number is Prime or not.
Prime Number:-

count = 0
n = int(input("Enter range From 1 To : "))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        count = count+1
print("Total Factors :",count)
if count==2:
    print("Prime Number")
else:
    print("Not Prime Number")

# break , continue , pass
"""
