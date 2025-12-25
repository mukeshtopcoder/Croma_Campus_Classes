"""
5- Identity Operator (Check Exact Match)
    is , is not   (Return Boolean Value True/False)

a = "aman"
b = "amankumar"
c = "aman"
print( a is b )
print( a is c )
print( a is not c )
print( a is not b )

# Membership
a = [1,2,3]
b = [1,2,[1,2,3],3]
c = [1,2,3]
print( a in b )
print( a in c )

#  Identity operator works on memory
a = "aman"
b = "amankumar"
c = "aman"
print( a is b )
print( a is c )

#  Identity operator works on memory
a = [1,2,3]
b = [1,2,3]
print( a is b )

6- Logical Operator
    and, or , not
and:- if both conditions are TRUE , Result is TRUE
otherwise FALSE

print( 10>5 and 50>10 )
print( 10>5 and 5>10 )
print( 10<5 and 30<10 )

or:- if both conditions are FALSE , Result is FALSE
otherwise TRUE


print( 10>5 or 10<5 )
print( 10<5 or 10<5 )
print( 10>5 or 15>5 )

not:- NOT is also called inverter gate
it reverse the output
print( not 10>5 ) 
print( not 10<5 ) 


print( int(True) )
print( int(False) )

print( bool(0) )
print( bool(1) )
print( bool(27) )
print( bool(273873) )
print( bool(-2653) )
print( bool('aman') )

a = 7
b = 5
  
print( a and b )
print( b and a )
print( 0 and a )
print( b and 0 )

a = 7
b = 5

print( a or b )
print( b or a )
print( a or 0 )
print( 0 or a )
print( 0 or 0 )

a = 7
print( not a )
print( not 0 )

7- Bitwise Operator

"""


