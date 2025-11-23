"""
Python is dynamic programming language

sid INT static
a = 10/10.7/'aman'  Dynamic

a = 10
print(a)
print( type(a) )
b = 19.6
print(b)
print(type(b))
a = 'red'
b = 'car'
print(a , b)
print(type(a))


input always return str/text value.
a = int( input("Write Something : ") )
print(a)
print(type(a))


WAP to calculate the area and circumference of a circle
Area:-   pie*radius*radius
ciru:-   2*pie*radius


radius = float( input("Enter Raidus : ") )
area = 3.14*radius*radius
circ = 2*3.14*radius
print("Area :",area)
print("Circumference :",circ)


Python Operators
1- Arithmetic Operator
    + - * / // % **

a = 7
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)     # 1.4
print(a//b)    # // truncation/floor division (it divide and remove point value)
print(11/4)
print(11//4)
print(a%b)     # % modulus (use to calculate the remainder)
print( 11%4 )
print( 5**3 )  # 5**3 => 5 to the power 3 (it calculate power)
print( 2**5 )  # 2**5 => 2*2*2*2*2


2- Assignment Operator
    = , += , -= , *= etc

a = 10    # (a is assign to 10)
print(a)
a += 1    #  a = a+1
print(a)


3- Relational / Conditional Operator
    > , < , >= , <= , == , !+
    it return boolean answer (True/False)

a = 7
b = 5
print( a > b )
print( a < b )
print( a >= b )
print( a <= b )
print( a != b )  # !=  is not equal to
print( a == b )  # ==  is equal to

4- Membership Operator  (check existance)
    in , not in
            They return boolean value (True/False)
a = 'aman'
b = 'amankumar'
print( a in b )
print( 'bablu' in b )  
print( 'ankum' in b )
print( 'k' in b )
print( 'z' not in b )
print( 'aman' not in b )


a = [1,2,3]
b = [1,2,3]
print( a in b )

5- Identity Operator   (check exact match  (works like ==))
    is , is not
        it also return boolean value (True/False)

a = 'aman'
b = 'amankumar'
c = 'aman'
d = 'Aman'
print( a is b )
print( a is c )
print( a is d )
# Python is a case sensitive language ( a != A )
print( a is not d )


a = [1,2,3]
b = [1,2,3]
print( a is b )

6- Logical Operator
    and or not    (it also return boolean (True/False) on conditions)

and => if both conditions are True , than True otherwise False
or => if both conditions are False , than False otherwise True
not => takes only one condition and revert the output
not is also called inverter

a = 7
b = 5
print( a>b , a<b )
print( a>b and a<b )
print( a>b and a<10 )
print( a>b or a<b )
print( not a>b )


print( int(True) )
print( int(False) )
print( bool(0) )
print( bool(1) )
print( bool(35) )
print( bool(-2376) )
# Every value is true besides 0


a = 7
b = 5
print( a and b )
print( b and a )
# last value is the answer if there is no 0


a = 7
b = 5
print( a or b )
print( b or a )
# first value is the answer if there is no 0

"""
