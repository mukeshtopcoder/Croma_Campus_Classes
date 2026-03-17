"""
Set and Dictionary
SET :- Set is a collection of unique hetregenous elements
Syntax:
s = { 23,56,67,89,45 }

Ways to create a SET
s = {34,56,67,8,90}
s = {1,2,3,5,4,32,1,1,2,3,3,2,1,2,3,2}
s = {'A',True,23,23+8j,'Aman',34.67}
s = set([234,456,67,89,34])
s = set((234,456,67,89,34))
print(s)
print( type(s) )


SET has no INDEX
SET can not be sliced
SET can not be Replicate
l = {32,45,56}
print(l*3)

BUT
SET can be traverse/Itterate
s = {32,45,56}
for x in s:
    print(x)


Built-in Functions
s = {1,2,2,1,3,4,5}
print(s)
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

SET's Method
    add , remove , pop , discard , clear

s = {3,56,7,88,5,53}
print(s)
s.add(11)
print(s)
s.pop()
print(s)
s.remove(56)    #  remove => it will raise an error if element not found
print(s)
s.discard(7)  # it will do nothing if element not found
print(s)
s.discard(101)

SET's Methods
    union , intersection , difference , symmetric_difference

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print( s1.union(s2) )  # it will concatenate but do not repeat the element
print( s1.intersection(s2) ) # it will print common elements
print( s1.difference(s2) ) # subtract s2 from s1
print( s1.symmetric_difference(s2) ) # Concatenate but remove the common elements


SET's Operation

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print( s1&s2 )  # INTERSECTION
print( s1|s2 )  # UNION
print( s1-s2 )  # DIFFERENCE
print( s1^s2 )  # SYMMETRIC_DIFFERENCE


DICTIONARY is also a collection or key and value pairs
Syntax:
dic_name = { key:value , key:value }
d = { 1:343,2:565,5:674,6:386,9:786 }  # {key:value}
print(d)
print( type(d) )



Dictionary can not have Duplicate Key
Dictionary can have Duplicate Value
d = {1:234,2:234,3:674}
print(d)


Dictionary has no INDEX
Dictionary can not be sliced
Dictionary can not be Replicate
BUT
Dictionary can be traverse/itterate
d = {1:234,2:654,3:874}
print( d )
for x in d:
    print(x)


Dictionary's Method
    keys , values , items
d = {1:234,2:654,3:874}
print( d )
for x in d.keys():
    print(x)


d = {1:234,2:654,3:874}
print( d )
for x in d.values():
    print(x)


d = {1:234,2:654,3:874}
print( d )
for x in d.items():
    print(x)


d = {1:234,2:654,3:874}
print( d )
for k,v in d.items():
    print(k , v)


d = {1:234,2:654,3:874}
print( d )
print( d[3] )


d = {1:234,2:654,3:874}
print( d )
# print( d[5] )   it will raise an error
print( d.get(2,'Not Found') )




    pop , get , clear , del (keyword)

d = {1:234,2:654,3:874}
print( d )
del d[2]
print(d)

d = {1:234,2:654,3:874}
print( d )
d.pop(3)
print(d)


d = {1:234,2:654,3:874}
print( d )
d.clear()
print(d)



d = {1:234,2:654,3:874}
print( d )
d2 ={4:999,5:555,3:999}
d.update(d2)
print(d)


d = {1:222 , 3:4554 , 1:999}
print(d)

"""
