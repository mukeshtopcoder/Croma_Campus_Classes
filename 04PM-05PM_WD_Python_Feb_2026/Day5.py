"""
Q6.
print(256 is 256)  # True
print(257 is 257)  # True


Q15.
x = 10
y = 20
print(x & y | x ^ y)  # 30
# x 01010
# y 10100
# & 00000
# ^ 11110
# | 11110   => 30


Q18.
print(5 + True * False + ( not False ) )
    #  5+ 1*0 + 1


and =>   1 and 1 => 1  other wise 0
or =>    0 or  0 => 0  other wise 1
xor =>   0 0 => 0 , 1 1 => 0  otherwise 1


Data Types

Numbers
    int => 34,56,-56, 0
    float=> 34.56 , -4.6 , 4.0
    binary =>  0b10101
    octal =>   0o165
    hexadecimal => 0,1,2---9,A,B,C,D,E,F
        0x23D
    complex number
            a+jb  =>   3+7j

a = 25
print(bin(25))
            
String/text
    'A'  ,  'Aman' , "A" , "Aman"
    
Boolean (True/False)

Sequence Data Type
    LIST [23,67,54] , Tuple (34,56,78)
    
Key Value Pair
    SET {5,67,89} , DICTIONARY  {2:45,3:67}


Rules for Python Variable's name
1- Unlimited Length
    asdfjbfgjsfngjfdnglsfkgnfdlkgndkfg = 10
2- You can use numbers
    aman265 = 10
3- You can not start with a number
    24aman  X
4- You can not use special symbols besides underscore _
    aman_265 = 10
5- You can start with underscore
    _aman265 = 10  ,  _2376aman
6- You can not use space
    aman kumar   X    aman_kumar , amanKumar
7- You can not use a keyword as a variable


BITWISE OPERATOR
    ~ (tiled operator)


a = -
print( ~a )


Python is a dynamic programming

days = 2853
print( "Year ",days//365 )
print( "Month", (days%365)//30 )
print( "Days", (days%365)%30)

"""
