"""
^ XOR (Bitwise)
XOR
INPUTS    OUTPUT
0   0       0
1   1       0
1   0       1
0   1       1


a = 7
b = 5
print( a^b )
Output :--  2

Variable's Name creation Rules
a = 10
b = 20
aman = 20
abc = 30
1- Variable's name can be anything
amankumar = 12
2- Variable's name can have a numeric value
aman725 = 100
3- Variable's name can not start with number
272aman = 100  X
4- Variable's name do not support space (whitespace)
aman kumar = 100    X
5- Variable's name can not have special symbol
besides underscore (_)
aman_kumar = 100
6- You can start with _
_aman = 100 , _236aman = 238


# WAP to swap two numbers.
a = 10 , b = 20 ==>>   a = 20 , b = 10

a = 10
b = 20
a , b = b , a
print("A : ",a)
print("B : ",b)


# WAP to swap two numbers without dual assignment.

a = 10
b = 20
c = a
a = b
b = c
print("A : ",a)
print("B : ",b)

# WAP to swap two numbers without dual assignment,
without third variable.

a = 10
b = 20
a = a+b
b = a-b
a = a-b
print("A : ",a)
print("B : ",b)


a = 10
b = 20
a = a*b
b = a//b 
a = a//b
print("A : ",a)
print("B : ",b)

# WAP to swap two numbers without dual assignment,
without third variable and arithmetic operators.

a = 7
b = 5
a = a^b
b = a^b
a = a^b
print("A : ",a)
print("B : ",b)
"""
