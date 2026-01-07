"""
Data Type
Number
    - int 34 , -567 , 0 etc
    - float  34.67 , -456.567 , 57.0 , 0.45 etc
    - binary number   0b1001  , 0b101201 X
    - Octal number   0,1,2,3,4,5,6,7
            0o456 , 0o563 , 0o569  X
    - Hexadecimal Number (Hex 6 + Dec 10 => 16)
        0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
            0x628 , 0xAB34
    - Complex Number (a+jb)
            3+8j
            a = 3+7j
            print( a )
            print( a.real )
            print( a.imag )
String
    String  :-   'A' , 'a' , '$', 'Aman' , "AMAN" , '''AMAN''' ,  
Boolean
    True / False
Sequence Data Type
    LIST     a = [32,45,67,89]
    TUPLE    a = (23,56,78,89)
SET          a = {23,45,67,89}
DICTIONARY   a = {1:35 , 3:56}  key:value (pair)

Python is a dynamic programming language
a = 'Aman'
print( type(a) )

Variable's name rules
1- Unlimited Length
2- You can use numbers
    aman75 = 10
3- You can not start with a number
    27aman X
4- You can not use special symbol, besides underscore _
    aman# X  ,  aman_kumar = 10
5- You can start with underscore
    _aman = 10 , _275aman = 276
6- You can not use space

WAP to swap two numbers.

a = 7
b = 5
temp = a
a = b
b = temp
print( a )
print( b )

WAP to swap two numbers without using third variable

a = 7
b = 5
a = a+b
b = a-b
a = a-b
print(a)
print(b)


a = 7
b = 5
a = a*b
b = a//b
a = a//b
print(a)
print(b)

WAP to swap two numbers without using third variable,
and without using arithmetic operator
a = 7
b = 5
111  => 7
101  => 5
010  => 2

010
101
111  => 7

010
111
101  => 5

a = 7
b = 5
a = a^b   
b = a^b
a = a^b
print(a)
print(b)

WAP to swap two numbers without using third variable,
and without using arithmetic operator and logical/bitwise
operator

a = 7
b = 5
a,b = b,a
print(a)
print(b)

WAP to swap two numbers without using third variable,
and without using arithmetic operator and logical/bitwise
operator and without using assignment operator


class name:
    c = 10   # local variable
    
a = 20       # Global Variable
print(a)


Python is a interpreted dynamic programming language

"""

