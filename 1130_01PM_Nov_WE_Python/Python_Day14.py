"""
SET:- SET is a collection of unique keys(elements) Hetreogenous
Order is not preserved

Syntax:-
set_name = {34,56,67,78,45}
Example:- s = {2,34,455,67,78,89,90,69}
print(s)

SET will remove duplicate elements automatically
s = {2,5,89,8,6,4,2,4,6,8,96}
print( s )
OUTPUT:- {96, 2, 4, 5, 6, 8, 89}

s = {23,46.75,'A',True,'Aman',3+8j}
s = set()
s = set([23,45,56,78,35,23])
s = {34,45,677,63,90}
print(s)

s = {75,56,67,87,25}
print( type(s) )

SET do not work on INDEX (SET has no index)
SET can not be sliced
SET can not be replicate

SET can be traversed/iterate
s = {23,45,56,67,86,56}
for x in s:
    print(x)

Built-in Functions
sum , max , min , len

s = {23,56,78,90,89,67,54,23,45,78,90}
print(s)
print( sum(s) )
print( max(s) )
print( min(s) )
print( len(s) )
print( sum(s)/len(s) )


s = set(["Hello","Python"])
print(s)
OUTPUT:- {'Hello', 'Python'}

s = set("PYTHONPROGRAMMING")
print(s)
OUTPUT:- {'A', 'N', 'I', 'O', 'M', 'P', 'G', 'T', 'Y', 'R', 'H'}

s = set("AMANKUMAR")
print(s)
OUTPUT:- {'U', 'R', 'A', 'K', 'M', 'N'}

SET's METHOD
add , remove , discard , clear

s = {2,45,67,78,90}
print(s)
s.add(99)
print(s)
s.remove(78)
print(s)
# s.remove(101)  it will raise an error because 101 is not in SET
s.discard(67)
print(s)
s.discard(101)  # it will not raise any error cause of 101 
print(s)
s.clear()
print(s)


SET OPERATIONS
Union            |
Intersection     &
Differnce        -
Symmetri Diff    ^

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print(s1)
print(s2)
print( s1 | s2 )  #  Union (remove duplicates and show both sets value)
print( s1 & s2 )  #  Intersection (common values)
print( s1 - s2 )  #  Difference (Show 1st set element and remove common)
print( s1 ^ s2 )  #  Symmetric Difference (Show both set elements remove common)


CHECK MEMBERSHIP ( in , not in )
s = {23,45,56,36,68}
print( s )
print( 45 in s )  
print( 99 not in s )
print( 36 not in s )


SET's METHOD
pop , issubset , union , intersect , difference , symmetric_difference

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print( s1.union(s2) )
print( s1.intersection(s2) )
print( s1.difference(s2) ) 
print( s1.symmetric_difference(s2) )

s1 = {1,2,3,4,5,6,7,8,9}
s2 = {1,2,3}
print(s2.issubset(s1))
print( s1.pop() )   # It will remove randomly any value
print( s1 )



# POP will remove a value from a set (randomly) (mostly 1st value)
s1 = {12,45,5,67,78,89,90,34,78,7,45,34}
print(s1)
s1.pop()
print(s1)

"""
