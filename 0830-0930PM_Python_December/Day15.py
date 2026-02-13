"""
Dictionary:- Dictionary is a collection of items
(key : value) pair.

s = { 1:23,2:56,5:36,'aman':14 }
print( s )

dict_name[key]


s = { 1:23,2:56,5:36,'aman':14 }
print( s )
print( type(s) )
print( s[5] )
print( s['aman'] )
# print( s[56] )   # it will raise an error because key not found


# Dictionary supports duplicate values
# Dictionary can not hold a duplicate key

d = {1:23,2:34,3:56,4:78,5:34, 3:99}
print( d )

# Dictionary can not be sliced
# Dictionary can not be Replicated

# Dictionary can be Traversed

It will traverse only keys
dic = { 1:34,2:45,3:57,4:68 }
for k in dic:
    print(k)



dictionary's Methods
keys() , values() , items()

# Traverse only keys
dic = { 1:34,2:45,3:57,4:68 }
for k in dic.keys():
    print(k)


Traverse only values
dic = { 1:34,2:45,3:57,4:68 }
for k in dic.values():
    print(k)


# Traverse both key:value pair in tuples
dic = { 1:34,2:45,3:57,4:68 }
for k in dic.items():
    print(k)


# Traverse both key:value pair in tuples
dic = { 1:34,2:45,3:57,4:68 }
for k,v in dic.items():
    print(k , v)


Built-in functions
    sum , max , min , len

# Works with keys only
dic = { 1:34,2:45,3:57,4:68 }
print( len(dic) )
print( sum(dic) )
print( max(dic) )
print( min(dic) )

# Works with values only
dic = { 1:34,2:45,3:57,4:68 }
print( len(dic.values()) )
print( sum(dic.values()) )
print( max(dic.values()) )
print( min(dic.values()) )

dictionary's Method
    update

dic1 = {1:24,2:345,3:567,4:68}
dic2 = {5:455,6:222,3:999}
dic1.update(dic2)
print(dic1)



Q17:-

li = [1,1,2,2,3,3,4,4,2,2,2,6,4,4,3,2,3,4,3,2,3]
target = 2

while target in li:
    li.remove(target)

print(li)


Q18:-

li = [1,2,3,2,1]
if li==li[::-1]:
    print("List is Palindrome")
else:
    print("List is not Palindrome")


Q19:-

li = [23,34,45,65,67,78,89,90]
target = 90
print(li,'\nTarget :',target)
if target in li:
    print("On Position :",li.index(target)+1)
else:
    print("Target is not in the list")

"""

