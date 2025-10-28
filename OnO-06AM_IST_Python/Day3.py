"""
Python Operators:-
1- Arithmetic Opertors
+ - * / // % **

a = 7
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)    # // truncation/floor division (remove decial part/point value)
print(a%b)     #  % modulus  (use to calculate the remainder)
print(5**3)    #  **  exponential (power) (5*5*5)

2. Assignment Operator
   =  , +=  , -=  , *=  , //= etc (with arithmetic operators)

a = 10  # (a is assign to 10)
a = a+1
a += 1    # => a+=1  , a=a+1  (both are same)
a*=2

3. Relational Operators
< , > , == , != , >= , <=
    (these operators return boolean value(True/False))

a = 7
b = 5
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)    # a is equal to
print(a!=b)    # a is not equal to

4. Membership Operators
    in   ,   not in  (check existance)
        return boolean answer

a = 'amankumar'
b = 'aman'
print(b in a)
print(a in b)
print('aman' in a)
print('ankum' in a)
print('ak' in a)
print('ak' not in a)


a = [1,2,3]
b = [1,2,3]
print(a in b)
it will return False
because [1,2,3] not matched with 1 or 2 or 3


a = [1,2,3]
b = [1,2,3,'A',[1,2,3],'aman']
print(a in b)
it will return True

5. Identity Operator
    is , is not   (check exact match (works on memory))
    return boolean value

a = 'aman'
b = 'amankumar'
c = 'aman'
print(a is c)
print(a is b)
print(a is not b)


a = [1,2,3]   # [] , () , {} etc (collection)
b = [1,2,3]
print(a is b)
it will return False because both objects have different memory


6. Logical Operator
    and , or , not
and :- if both values are True, result will be True otherwise False
or :- if both values are False, result will be False otherwise True

print( True and True )
print( True and False )
print( True or True )
print( True or False )
print( False or False )
print(10>5 and 10<5)
print(10>5 or 10<5)

# not ( it is also called inverter gate)
print( not 10>5 )

a = 7
b = 5
print(a>b and b>a)

print( int(True) )
print( int(False) )
print( bool(1) )
print( bool(0) )
print( bool(825) )
print( bool(-725) )


a = 7
b = 5
print(a and b)
print(b and a)
print(0 and b)
print(b and 0)


a = 7
b = 5
print(a or b)
print(b or a)
print(0 or b)
print(b or 0)
print(0 or 0)


print( not 6 )
print( not 0 )

# Bitwise Operators
"""

