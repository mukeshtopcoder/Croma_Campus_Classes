"""
looping

while loop

Syntax:-

initilization
while condition:
    statement
    incr/decr

Example:-

a = 1
while a<5:
    print("Hello")
    a = a+1


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


a = 1
while a<=10:
    print("Hello")
    a = a+2



a = 1
while a<=10:
    print("Hello")
    a = a+2




# WAP to print counting from 1 to 10

a = 1
while a<=10:
    print(a)
    a=a+1


# WAP to print counting from 1 to N

n = int(input("Enter Range From 1 to : "))
a = 1
while a<=n:
    print(a)
    a=a+1


# WAP to print factors a number
HINT:-    12 =>  1,2,3,4,6,12

n = int(input("Enter Range From 1 to : "))
a = 1
while a<=n:
    if n%a==0:
        print(a)
    a=a+1


for and while difference
for => for itterates/traverse collections
range , string , list , tuple , set , dictionary , array

for a in [23,34,45,56,67]:
    print(a)

while can works with custom conditions

ch = 'Y'
while ch in "yY":
    name = input("Enter Employee Name : ")
    add = input("Enter Employee Address : ")
    ch = input("Do You Want To Continue (Y/N) : ")

# WAP to add all digits of a number
HINT:-    356  =>  3+5+6 => 14

add = 0
num = 364
while num>0:
    rem = num%10
    add = add+rem
    num = num//10  
print(add)


add = 0
num = 364
while num>0:
    add = add+num%10 
    num = num//10  
print(add)


# WAP to reverse a numbers
HINT:-  378  =>  873 (Reverse) 

add = 0
num = 38742
while num>0:
    add = add*10+num%10   
    num = num//10  
print(add)


# WAP to check a number is Armstrong or not
# HINT:-  153 => 1^3 + 5^3 + 3^3 => 1+125+27 => 153

add = 0
num = 153
while num>0:
    rem = num%10
    add = add+rem**3
    num = num//10
print(add)

"""
