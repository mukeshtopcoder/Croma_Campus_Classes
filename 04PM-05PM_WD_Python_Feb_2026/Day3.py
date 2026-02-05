"""
Python Operators
a+b  =>     a,b  (Operands)     + => Operator
Operator operates on operands

1- Arithmetic Operator
    + - * / % // **

a = 7
b = 5
print( a+b )
print( a-b )
print( a*b )
print( a/b )
print( a%b )   # %  modulus  (to calculate the remainder)
print( 11%4 )
print( a//b )  #  // floor_Division/Truncation (divide and remove decimal part from answer)
print( 5//2 )
print( 5**3 )  # ** Exponential (to calculate the power of a number 5**3 => 5*5*5)
print( 2**5 )


2- Relational/Conditional Operator
    > < >= <= == !=    (return boolean answer True/False)

a = 7
b = 5
print( a>b )  #  > is greater than
print( a<b )  #  < is less than
print( a>=b ) # >= is greater than or equal to
print( a<=b ) # <= is less than or equal to
print( a!=b ) # != is not equal to
print( a==b ) # == is equal to

3- Assignment Operator
    = , += , -= , *= etc

a = 10  # ( a is assign to 10 )
a += 1  # =>    a = a+1
a *= 2  # =>    a = a*2
print(a)


4- Membership Operator   (Check existance)
    in , not in          (Return Boolean Answer True/False)

a = "aman"
b = "amankumar"
print( a in b )
print( "ankum" in b )
print( "ka" in b )
print( "ka" not in b )


5- Identity Operator (check exact match)
    is , is not  ( return boolean answer True/False )

a = "aman"
b = "amankumar"
c = "aman"
print( a is b )
print( a is c )
print( a is not b )


6- Logical Operator
    and , or , not
and : if both conditions are True , Result is True
otherwise False

print( 10>5 and 10>50 )   # False
print( 10>5 and 10>7 )    # True
print( 10>70 and 10>50 )  # False

or : if both conditions are False , Result is False
otherwise True

print( 10>5 or 10>50 )   # True
print( 10>5 or 10>7 )    # True
print( 10>70 or 10>50 )  # False

not : works with only one and one condition/input
not : it is also called inverter gate
not : it convert True to False and vice-versa

print( not 10>5 )
print( not False )
print( not True )


# True =>   1
# False =>  0

print( True+True )
print( True+False )
print( True*False )

"""
