"""
SET :- Set is also a collection of hetreogenous and
unique elements

Syntax:-
s = {34,45,56,67,78,89}

s = {34,45,56,67,78,89}
print(s)
print(type(s))
s = {1,2,2,3,4,4,5,5,4,4,3,4,2,3}
print(s)
print(type(s))


1- SET can not hold a duplicate element
2- Insertion Order is Not Preserved
3- SET do not work on INDEX
4- SET can not be sliced
5- SET can not be Replicate
6- SET can be Traversed/Itteration

s = {23,890,67,34,67,89}
print( s )
for x in s:
    print(x)


Built-in Functions
    sum , max , min , len

s = {1,2,3,5,5,5,4,3,2,2,1,2,3}
print(s)
print( sum(s) )
print( max(s) )
print( min(s) )
print( len(s) )


SET's Method
    add , remove , pop , discard , clear

s = {23,56,46,78,56,67}
print(s)
s.add(99)
print(s)
s.pop()
print(s)
s.remove(46)
print(s)
# s.remove(101)
s.discard(23)
print(s)
s.discard(101)
print(s)
s.clear()
print(s)


s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print( s1.intersection(s2) ) # print only common elements
print( s1.union(s2) ) # Print all elements but do not repeat
print( s1.difference(s2) )
print( s1.symmetric_difference(s2) ) # print both set's element exclude the common


SET's Operations

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}

print( s1&s2 )  # Intersection
print( s1|s2 )  # Union
print( s1-s2 )  # difference
print( s1^s2 )  # Symmetric_difference


Dictionary:- It is also a collection of hetregenous data
of key:value pairs {key:value} => item

s = {1:23,2:56,5:78,'A':90,'Aman':35}
print(s)
print(type(s))
print( s[5] )

1- Dictionary supports duplicate elements
2- Dictionary can not hold duplicate KEY
3- Dict do not support INDEX
4- Dict can not be sliced
5- Dict can not be REPLICATE

s = {1:23,2:56,5:78,'A':90,'Aman':35,5:99 , 4:35}
print(s)
print(type(s))
print( s[5] )


Dictionary can be traversed/itterate
dic = {1:43,2:35,3:57,4:23,5:46}
print(dic)
for x in dic:
    print(x)



dictionary's Methods
keys
dic = {1:43,2:35,3:57,4:23,5:46}
print(dic)
for x in dic.keys():
    print(x)

values
dic = {1:43,2:35,3:57,4:23,5:46}
print(dic)
for x in dic.values():
    print(x)

items
dic = {1:43,2:35,3:57,4:23,5:46}
print(dic)
for x in dic.items():
    print(x)

dic = {1:43,2:35,3:57,4:23,5:46}
print(dic)
for k,v in dic.items():
    print(k , v)


update

dic = {1:43,2:35,3:57,4:23,5:46}
print(dic)
dic2 = {7:99,8:88,3:66}
dic.update(dic2)
print(dic)


pop

dic = {1:43,2:35,3:57,4:23,5:46}
dic.pop(2)
print(dic)


get
dic = {1:43,2:35,3:57,4:23,5:46}
print(dic.get(3))
print( dic.get(8) )
print( dic.get(8,'Key Not Found') )
print( dic.get(2,'key Not  FOund') )

"""
