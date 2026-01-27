"""
Dictionary
Dictionary is a collection of of key:value pair items
Where key can not be duplicate but value can be duplicate

s = {1:23,2:45,5:56,'A':78,'Aman':89}
{ key:value }  (item)

s = {1:34,4:34,7:57,8:356,0:678,4:43}
print(s)
print(s[4])
# print(s*2) Dictionary can not be replicate because keys can not be duplicate


Dictionary's Methods
get

d = {1:34,2:45,3:56,4:67}
print(d)
print(d[2])
# print(d[8]) it will show error because key 8 is not available
print(d.get(8,"Alternate Message"))
print(d.get(7,"Not Found"))
d[5] = 99
print(d)
d.pop(3)
print(d)
del d[2]
print(d)


items , values , keys
d = {1:33,2:45,5:67,7:56}
print(d)
print(d.keys())
print(d.values())
print(d.items())

d = {1:33,2:45,5:67,7:56}
for x in d:   # by default it traverse keys
    print(x)

d = {1:33,2:45,5:67,7:56}
for x in d.keys(): 
    print(x)

d = {1:33,2:45,5:67,7:56}
for x in d.values(): 
    print(x)

d = {1:33,2:45,5:67,7:56}
for x in d.items(): 
    print(x)


d = {1:33,2:45,5:67,7:56}
for k,v in d.items(): 
    print(k , v)

d1 = {1:34,2:465,3:56}
d2 = {5:56,6:78,2:99}
d1.update(d2)
print( d1 )

Dictionary Comprehension
d = {x:x*x  for x in range(1,11) }
print(d)

Built-in Functions
    sum , max , min , len

d = {1:23,2:35,3:56,4:78,5:78}
print(d)
print( len(d) )
print( sum(d) )  #  by default Sum of keys
print( sum(d.values()) )
print( max(d.values()) )
print( min(d.values()) )

"""
