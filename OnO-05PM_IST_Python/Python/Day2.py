"""

a = 10
b = 20
c = a+b
print(c)


built-in functions
print , 

a = 100
print("Hello")
print("a")
print(a)
print("Hello a")
print("Hello ",a)
print(f"Hello {a}")

input
input return text/string value
a = input("Enter A Number : ")
b = input("Enter B Number : ")
c = a+b
print("Addition :",c)


int (integer)
int will convert a string into integer

a = int( input("Enter A Number : ") )
b = int( input("Enter B Number : ") )
c = a+b
print("Addition :",c)


float
it convert string into numercial 23.34

a = float( input("Enter A Number : ") )
b = float( input("Enter B Number : ") )
c = a+b
print("Addition :",c)


WAP to calculate gross salary of an employee where HRA
is 20% and DA is 30% of his basic salary.
HINT:- Gross_Salary = Basic_Salary + HRA + DA

bs = float( input("Enter Basic Salary : ") )
hra = bs*0.20
da = bs*0.30
gs = bs+hra+da
print("Gross Salary :",gs)


Rules's for variable names
1- Unilimited Length
a , aman , amankumar
2- You can use numbers
    aman2375
3- You can not start with number
    27aman  X
4- You can not use special symbols besides _ underscore
    aman&826  X ,    aman_kumar
5- You can not use space
    aman kumar = 10    X  (you can use _ instead of space)
6- You can start with underscore
    _aman = 10

Literals (Variable , constant , data type)
DataType
1- Number
    - int 38,67,23,67,+45,-67
    - float 34.67 , -66.75
    - binary a = 0b1001
    - octal , hexadecimal 
2- String
    - A
    - Aman
3- Boolean Value
    - True
    - False
4- Sequential Data Type (List , Tuple)
    - list   a = [22,67,89,76,43]
    - tuple  a = (23,45,67,78,34)
5- SET
    - set    a = {23,56,78,89,23}
6- Dictionary
    - Dictionary a = {key:value , 'name':'Aman'}

Python Operators
1- Arithmetic Operator
2- Assignment Operator
3- Relational Operator
4- Membership Operator
5- Identity Operator
6- Logical Operator
7- Bitwise Operator

1- Arithmetic Operator
    + - * / % // **

a = 7
b = 5
print( a+b )
print( a-b )
print( a*b )
print( a/b )
print( a%b )     #  % modulus (use to calculate remainder)
print( 11%4 )
print( a//b )   #  // Truncation/Floor division (it divide and answer in integer not decimal)
print( 11//4 )
print( 5**3 )   # ** exponential (use to calculate power  5**3 => 5*5*5 )


2- Assignment Operator
    =
    +=  -=  *=  etc

a = 10
a += 1     # a = a+1
a *= 2
print( a )


a = 10
#  a += 1     a = a+1
a *= 2
print( a )


"""

