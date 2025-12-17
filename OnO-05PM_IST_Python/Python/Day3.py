"""
3- Relational Operator (Boolean Answer True/False)
    > < >= <= == !=

a = 7
b = 5

print( a>b )
print( a<b )
print( a>=b )
print( a<=b )
print( a==b )   # == is equal to 
print( a!=b )   # != is not equal to


4- Membership Operator (check existance)
    in , not in     (boolean Answer True/False)

a = "aman"
b = "amankumar"
print( a in b )
print( a not in b )
print( b not in a )
print( "ankum" in b )
print( "k" in b )
print( "ka" in b )
print( "amar" in b )

5- Identity Operator  (Exact Match)
    is , is not  (Boolean Answer True/False)

a = "amankumar"
b = "aman"
c = "aman"
print( a is b )
print( b is a )
print( b is c)
print( a is not b )

a = [23,56,89]
c = [23,56,89]
b = [23,56,[23,56,89],89]
print( a in c )  
print( a in b )


num = 34
st = "aman"
num2 = 34
a = [23,56,89]
c = [23,56,89]
b = [23,56,[23,56,89],89]
print( a is c )


6- Logical Operator
    and or not
and => if both/all conditions are True , Output is True
Otherwise False
and => if both/all conditions are False , Output is False
Otherwise True
not => work on only one condition/input(also called inverter gate)
it reverse the output

a = 7
b = 5
print( a>5 and b>3 )
print( a>5 and b>7 )
print( a>5 or b>7 )
print( a>10 or b>7 )
print( not a>10 )

a = 7
b = 5
print( int( False ) )  
print( int( True ) )  
print( bool(0) )
print( bool(1) )
print( bool(35678) )
print( bool(-35678) )
print( bool("aman") )


a = 7
b = 5
print( a and b )
print( b and a )

a = 7
b = 0
print( a and b )
print( b and a )

a = 7
b = 5
print( a or b )
print( b or a )

a = 7
b = 0
print( a or b )
print( b or a )


Always answer in boolean

a = 0
print( not a )
print( not 1 )


"""


