"""
list = []
tuple = ()
set = set() or {ele1,ele2,..}

SET:- Set is also a collection of unique hetreogenous elements
Syntax:-
set_name = {ele1,ele2,ele3,..}
s = {23,78,54,57,25}
print(s)

in set order is not Preserved
and remove the duplicate data
s = {2,7,4,2,45,7,9,7,5,3,4}
print(s)

SET has no INDEX (do not work on INDEX)
SET can not be SLICED because of NO INDEX
SET can not be REPLICATE
SET can be TRAVERSE/ITTERATE

s = {23,456,78,76,54,321,76,33}
for x in s:
    print(x)

Built-in Functions
    sum , max , min , len

s = {23,75,86,24,64,13,87}
print(s)
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
print(sum(s)/len(s))


SET's Method
     add , pop , remove , discard , clear

s = {21,43,56,78,35}
print(s)
s.add(99)   # it can be add anywhere mostly in 1st place (order is not oreserved)
print(s)
s.pop()     # it can be remove a element from anywhere (mostly 1st place)
print(s)   
s.remove(56)
print(s)
# s.remove(101)  it will raise an error because 101 is not in the list
s.discard(43)
print(s)
s.discard(101)
print(s)
s.clear()
print(s)


SET's Operations

a = {1,2,3,4,5,6}
b = {3,4,5,6,7,8}
# union      (All unique elements from both sets)
print( a|b )
print( a.union(b) )
# intersection (common)
print( a&b )
print( a.intersection(b) )
# difference
print( a-b )
print( a.difference(b) )
# Symmetric Difference
print( a^b )
print( a.symmetric_difference(b) )


"""
