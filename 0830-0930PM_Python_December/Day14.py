"""
list_name = [23,34,456,34,89]  # muteable
tuple_name = (23,4,67,89,32)   # immuteable
Tuple is faster than the list cause of its immuteabity

li = [23,45,678,23,234]
print(li)
print(type(li))
t = (23,45,67,78,82,45)
print(t)
print(type(t))

SET
s = {23,42,56,67,87}
this is a set
it is a collection of unique elements

order is not preserved
SET can not work on index
SET can not be replicate
SET can no be sliced

SET can be traversed

s = {2,3,4,6,7,9,3,5,6,3,2,4,6,7,4,2}
print(s)
print( type(s) )


s = {23,6,78,78,76,55,32,45,67,65,42}
print(s)
for m in s:
    print(m)

Built-in functions
    sum , max , min , len

s = {2,4,5,7,9,7,6,4,2}
print(s)
print( sum(s) )
print( max(s) )
print( min(s) )
print( len(s) )


Set's Method
add , pop , remove , discard , clear
"""
s = {23,45,65,78,89}
print(s)
s.add(99)
print( s )
s.pop()
print(s)
s.remove(78)
print(s)
# s.remove(101)  it will through an error because 101 is not available in set
s.discard(45)
print(s)
s.discard(101)
print(s)
s.clear()
print(s)

