"""
SET :- Set is a collection of hetregenous type
unique element

s = {23,56,89,67,34}

s = {23,56,89,67,34}
print(s)
print(type(s))


s = {1,2,2,2,1,1,12,3,4,4,5,5,4,4,2,3,3}
print(s)
print(type(s))

1- SET is a collection of unique elements
2- SET will remove duplicate elements automatically
3- SET do not support INDEX
4- SET can not be sliced
5- SET can not be Replicate
6- SET can be traversed/itterate

s = {23,67,90,89,5,34}
print(s)
for x in s:
    print(x)


Built-in Functions
    sum , max , min , len

s = {23,67,90,89,5,34}
print(s)
print( sum(s) )
print( max(s) )
print( min(s) )
print( len(s) )

SET's Method
    add , pop , remove, discard , clear

s = {23,56,67,8,90}
print(s)
s.add(99)
print(s)
s.pop()
print(s)
s.remove(8)
print(s)
s.discard(90)
print(s)
s.discard(101)
print(s)
s.clear()
print(s)


s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print( s1.intersection( s2 ) )
print( s1.union(s2) )
print( s1.difference(s2) )
print( s1.symmetric_difference(s2) )


Set's Operation
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print( s1&s2 )   # intersection
print( s1|s2 )   # union
print( s1-s2 )   # difference
print( s1^s2 )   # symmetric_difference

"""
