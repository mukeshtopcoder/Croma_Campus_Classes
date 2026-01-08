"""
WAP to print counting from 1 to N

n = int(input("Enter Range to Print Number 1 to : "))
for i in range(1,n+1):
    print(i)


WAP to print factors of a Number
HINT:- 12 =>  1,2,3,4,6,12

n = int(input("Enter Range to Print Number 1 to : "))
for i in range(1,n+1):
    if n%i==0:    
        print(i)


WAP to count factors of a number
HINT: 12 => 1,2,3,4,6,12  => 6 Factors

count = 0
n = int(input("Enter Range to Print Number 1 to : "))
for i in range(1,n+1):
    if n%i==0:    
        print(i)
        count = count+1
print("Total Factors :",count)


WAP to check an entered number is Prime or not.
HINT:- A number which is divisible 1 and itself
HINT:- A number which has only and only two factors

count = 0
n = int(input("Enter Range to Print Number 1 to : "))
for i in range(1,n+1):
    if n%i==0:    
        count = count+1
print("Total Factors :",count)
if count==2:
    print("Prime Number")
else:
    print("Not Prime Number")


Nested Loop
for i in range(1,5,1):
    for j in range(1,5,1):
        print("Hello")

WAP to print all the prime numbers from 1 to 100.

for num in range(1,101):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)

# WAP to print all the prime numbers from 1 to N.

n = int(input("Enter Range From 1 to : "))
for num in range(1,n+1):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)

WAP to calculate factorial of a number
HINT:-   5  =>  1*2*3*4*5 => 120

num = int(input("Enter A Number : "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("Factorial :",fact)


WAP to print Fibonacci Series
 0 1 1 2 3 5 8 13 21 34 etc

a = 0
b = 1
for i in range(1,11):
    c = a+b
    print(c)
    a = b 
    b = c


"""
