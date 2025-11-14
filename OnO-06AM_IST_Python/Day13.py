"""
SET:- Set is also a collection
Unordered
Mutable (can add/delete elements)
Does NOT allow duplicates
Stores unique items/elements only

a = {23,56,76,9,56}
print(a)
print(type(a))


a = {23,56,76,9,56}
a = {23,567.34,True,'A','AMAN',3+8j}
a = set([34,56,78,90])
a = set()
print(a)

SET's Method
add , update , remove , discard

a = {1,2,3,6,4,5}
print(a)
a.add(99)
print(a)
a.add(56)
print(a)
b = {34,56,46,89}
a.update(b)
print(a)
a.remove(99)
print(a)
# a.remove(199)
a.discard(199)
print(a)
a.discard(89)
print(a)
a.pop()
print(a)
a.clear()
print(a)


SET's Method / Operations
UNION , INTERSECTION , DIFFERENCE , 

a = {1,2,3,4}
b = {3,4,5,6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))  # {1,2}
print(a.symmetric_difference(b))  # {1,2,5,6}

print( a&b )  # intersection
print( a-b )  # difference

s1 = set([1,2,3,4])
s2 = frozenset([1,2,3,4])
s1.add(99)
# s2.add(99)   in frozenset we can not add or remove
print(s1)
print(s2)


Built-in Functions
sum , len , max , min

a = {1,2,3,3,3,4,4,5,6}
print(a)
print(sum(a))
print(max(a))
print(min(a))
print(len(a))
print(sum(a)/len(a))

SET has no index
a = {1,2,3,4,5,6,6,6,5,3}
print(a)
# print(a[3])    Set do not work in index
# SET can not be sliced
# SET can not be replicate
# BUT SET can be traverse

a = {1,2,3,4,5,6,6,6,5,3}
for x in a:
    print(x)


Dictionary:-
A dic in python is used to store data in key:value pair
dic = {key:value}
key can not be duplicate (always unique)
value can be duplicate

a = {1:34,2:34,5:34,'A':39,9:67,8:34}
print(a)
print(a[5])
print(type(a))

a = {1:34,2:34,5:34,'A':39,9:67,8:34}
a = {'name':'Ramesh Singh','Address':'Noida Sec 16'}
a = {}
a = dict()
a = dict({2:98,5:87})
print(a)


a = {5:34,9:67,8:34}

print(a[8])
# print(a[6])  #  it will raise an error because key is not available
print(a.get(8,'Not Available'))
print(a.get(6,'Not Available'))



a = {5:34,9:67,8:34}

print(a[8])
# print(a[6])  #  it will raise an error because key is not available
print(a.get(8,'Not Available'))
print(a.get(6,'Not Available'))
a = {}
a = dict()
print(type(a))
a['name']='Rahul'
print(a)
a['age']=28
b = {'address':'Noida','age':31}
a.update(b)
print(a)


Dictionary's Method
GET , UPDATE , pop , del (keyword) , popitem() , clear()

a = {5:34,9:67,8:34,1:35,3:45}
print(a)
a.pop(5)
print(a)
del a[9]
print(a)
a.popitem()
print(a)
a.clear()
print(a)

Traversing
METHODS:-  keys , values, items

a = {1:23,2:45,3:567,4:657,5:67}
for x in a:   # it will traverse keys (by default)
    print(x)

for x in a.keys():
    print(x)

for x in a.values():
    print(x)

for x in a.items():
    print(x)

for k,v in a.items():
    print(k,

# Create a dictionary by list of tuples
li = [(1,34),(2,45),(3,56),(4,78)]
d = dict(li)
print(d)


keys = ['name','age','address']
values = ['Rahul Singh',24,'noida']
d = dict(zip(keys,values))

print(d)

sq = {x:x*x for x in range(1,11)}
print(sq)


WAYS to make collections
li = []
li = list()
t = ()
t = tuple()
s = set()
dic = {}
dic = dict()

# Sort the rows by the marks
students = {
's1':{'name':'Amit','marks':87},
's2':{'name':'Rahul','marks':76},
's3':{'name':'Samar','marks':81}
    }
for stu,det in students.items():
    print(stu, det)

# Find intersection of two list

li1 = [1,2,3,4,5]
li2 = [7,6,3,4,8,9]
li3 = []
for i in li1:
    if i in li2:
        li3.append(i)
print(li3)
"""
