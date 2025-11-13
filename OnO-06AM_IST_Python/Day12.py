"""
collection (list,tuple,set,dictionary,string,range)
tuple (tuple is also a collection like list)
t = ()

t = ()
t = (23,56,78,89)
t = (34,67.3,'A','Aman',True,3+7j)
print(t)
t = tuple()
t = tuple([34,67,90])
t = tuple((34,67,90))
print(t)


indexing same as list
backward and forward both index
t = (23,56,89,56,23,67)
print(t)
print(t[3])

Slicing
t = (23,56,89,56,23,67)
print(t)
print(t[2:5])

Traversing
t = (23,56,89,56,23,67)
print(t)
for x in t:
    print(x)

Replication
t = (23,56,89,56,23,67)
print(t*2)

Built-in functions
sum , max , min , len

t = (23,56,89,56,23,67)
print(t)
print(sum(t))
print(max(t))
print(min(t))
print(len(t))
print(sum(t)/len(t))


Tuple's Methods
count , index

t = (23,56,89,56,23,67)
print(t)
print(t.count(23))
print(t.index(56))


Tuple is immuteable (can not be change)
A tuple can not be edit or modify (immuteablity)
List is muteable
Tuple is faster than the list (immuteablity)

Programming Questions

li = [4,34,56,36,77,89,90,56,67]
print(li)
li2 = []
for i in range(len(li)-1 , -1 , -1):
    li2.append(li[i])

print(li2)
li = li2.copy()
print(li)

li = [23,67,9,67,54,23,23,56,23,78,90,23,67]
print(li.count(23))


li = [23,67,9,67,54,23,23,56,23,78,90,23,67]
target = 23
count = 0
for x in li:
    if x==target:
        count+=1
print(count)


li1 = [3,56,89,45]
li2 = [34,67,90,57]
li1.extend(li2)
print(li1)

SET/DICTIONARY
"""
