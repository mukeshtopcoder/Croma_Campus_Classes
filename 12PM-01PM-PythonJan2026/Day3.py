"""
Built-in Functions
print , input , float , int

Python Operator's
a+b   =>  a,b => Operand   ,   + => Operator

1- Arithmetic Opertor
    + , - , * , / , // , % , **

a = 7
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)    # // truncation/Floor Division (remove decimal value)
print(a%b)     # %  modulus (calculate remainder)
print(11%4)
print(5**3)    # **   Exponential (calculate power 5**3 => 5*5*5)

2- Assignment Operator
    = , += , -= , *= etc
a = 10
c = a+b
a = 10
a += 1        #     =>     a = a+1
a *= 2        #     =>     a = a*2
print(a)


3- Relational / Conditional Operators (Return Boolean Answer)
    >, < , >= , <= , == , !=          (Boolean => True/False)

a = 7
b = 5
print( a>b )
print( a<b )
print( a>=b )
print( a<=b )
print( a!=b )    #  !=   is not equal to
print( a==b )    #  ==   is equal to

4- Membership Opertor (Return Boolean)
    Check Existance
        in , not in

a = "aman"
b = "amankumar"
print( a in b )
print( "ankum" in b )
print( "ka" in b )
print( "ka" not in b )


a = "aman"
b = "aman"
print( a in b )     # True

a = [1,2,3]
b = [1,2,[1,2,3],3]
print( a in b )    # True

5- Identity Operator (Return Boolean)
        Check Exact Match
    is , is not

a = "aman"
b = "aman"
c = "amankuamr"
print( a is c )
print( a is b )
print( a == b )
print( a is not c )

# identity operator works on MEMORY
a = [1,2,3]    #  it is an object (and every object has its own memory)
b = [1,2,3]
print( a is b )  

6- logical Operator
    and , or  , not
and:- if both are TRUE , Result is True otherwise FALSE
or:- if both are FALSE , Result is FALSE otherwise TRUE
not:- It is also called invertor gate
if input is TRUE , result will be FALSE and vice-versa

print( 10>6 and 20>5 )
print( 10>6 and 20>50 )
print( 10>6 or 20>50 )
print( 10>60 or 20>50 )
print( not 10>60 )

print( int(True) )
print( int(False) )

print( bool(1) )
print( bool(0) )
print( bool("aman") )
# Every value is True besides zero.

a = 7
b = 5
print( a and b )
print( b and a )


a = 7
b = 0
print( a or b )
print( b or a )


"""
