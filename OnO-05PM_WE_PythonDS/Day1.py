# Single Line Comment
"""
Multiline Comments
Built-in Functions  ( print , input , int , float )
    print 

print( "Message" )
print( 'Message' )
print( '''Message''' )

a = 10
print( 'a' )
print( a )
hello = 20
print( hello )


a = 'aman'
print("Value ",a)
print("Value "+a)
print( f"Value {a} " )


a = 10
b = 20
c = a+b
print("Addition :",c)


    input
        input function always return a text

a = input("Enter A Number : ")
b = input("Enter B Number : ")
c = a+b
print("Addition :",c)


    int

a = int( input("Enter A Number : ") )
b = int( input("Enter B Number : ") )
c = a+b
print("Addition :",c)


    float

a = float( input("Enter A Number : ") )
b = float( input("Enter B Number : ") )
c = a+b
print("Addition :",c)


# WAP to calculate the gross salary of an employee
where HRA is 20% and DA is 30% of his basic Salary
HINT:-  Gross_Salary = Basic_Salary + HRA + DA

bs = float( input("Enter Basic Salary : ") )
hra = bs*0.20
da = bs*0.30
gs = hra+da+bs
print("Gross Salary :",gs)


Python's Operator
a+b    =>  a,b => operands  ,  +  =>  Operator

1- Arithmetic Operators
    + - * / // % **

a = 7
b = 5
print( a+b )
print( a-b )
print( a*b )
print( a/b )
print( a%b )    #  % modulus (it is use to calculate the remainder)
print( a//b )   #  //  floor division/truncation 
print( 5**3 )   #  **  Exponential  (it is use to calculate the power)
# 5 to the power 3


2- Relational Operator  ( Return Boolean Answer True/False )
    > < >= <= != ==

a = 7
b = 5
print( a>b )
print( a<b )
print( a>=b )
print( a<=b )
print( a!=b )   # != is not equal to 
print( a==b )

3- Assignment Operator
    =  , += , -= , *= , /= , //= etc
a = 10       # a is assign to 10
print( a )

a = 10
a += 1    # a = a+1
a *= 2
print(a)

4- Membership Operators  (Return Boolean Answer)
    in , not in  ( check the existance of the data )

a = "aman"
b = "amankumar"
print( a in b ) 
print( "ankum" in b )
print( "ka" in b )
print( "ka" not in b )


a = [1,2,3]
b = [1,2,3]
c = [1,2,[1,2,3],3]
d = 3
print( a in b )
print( a in c )    
print( d in a )


5- Identity Operators  ( check the exact match in variable not with objects because it works with memory not with data )
    is , is not   (Return Boolean Answer)

a = "aman"
b = "aman"
print( a is b )
a = [1,2,3]
b = [1,2,3]
print( a is b )

6- Logical Operators
    and , or , not   (Return Boolean Answer)

and :- if both inputs are True, Output is True otherwise False
or :- if both inputs are False, Output is False otherwise True
not :-  if input is True, Output is False and vice-versa
    not gate is also called the invertor gate

a = 7
b = 5
print(a>b and b>8)
print(a>b and b>3)


a = 7
b = 5
print(a>b or b>8)
print(a>b or b>3)
print(a>10 or b>25)


a = 7
b = 5
print( not a>b )


a = 7
b = 5
print( not (a>b and b>a) )


7- Bitwise Operator

"""

