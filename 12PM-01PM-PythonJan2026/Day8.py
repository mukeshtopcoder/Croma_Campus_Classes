"""
Programming Questions:-
# WAP to print factorial of a number.
# HINT:-    5  => 5*4*3*2*1 => 120

num = 5
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("Factorial :",fact)


# Find GCD (HCF) of two numbers
# HCF => Highest Common Factor

n1 = int(input("Enter A Number : "))
n2 = int(input("Enter B Number : "))
hcf = 1
for i in range(1,n1+1):
    if n1%i==0 and n2%i==0:
        hcf = i
print("HCF :",hcf)


# Generate A Fibonacci Series upto 10 number
0 1 1 2 3 5 8 13 21 34 etc

a = 0
b = 1
print(a)
print(b)
for i in range(1,11):
    c = a+b
    print(c)
    a = b
    b = c

# WAP to add numbers from 1 to N

add = 0
n = int(input("Enter Range From 1 to : "))
for i in range(1,n+1):
    add = add+i
print(add)


n = int(input("Enter Range From 1 to : "))
print( n*(n+1)/2 )

"""
