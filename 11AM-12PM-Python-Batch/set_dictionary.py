'''
SET_DICTIONARY
SET :- Set is a collection of unique hetregenous elements.
s = {12,34,56,67,89}

s = {34,45,56,67,89,34}
s = {2,3,5,7,7,8,6,5,4,3,2,3,2}
s = {'A','Aman',34,True,25.57,3+8j}
s = set()
s = set([23,34,45,67,78,46])
print(type(s))
print(s)

SET has no index.
SET can not be sliced.
SET can not be Replicate.
But Set can be traversed.
SET has no order (it is unordered).

s = {34,45,6,8,9}
for i in s:
    print(i)    

s = {2,4,5,6,8,7,6,5,4,3,3,4}
for i in s:
    print(i)

Built-in Methods
sum , max , min , len
s = {90,25,47,79,45,90}
print(s)
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

SET's Method
add , remove , discard , clear , pop , update

s = {90,25,47,79,45,90}
print(s)
s.add(99)
print(s)
s.remove(25)
print(s)
s.pop()
print(s)
s.pop()
print(s)
# s.remove(88)  it will raise an error because element is not present
s.discard(88)
s.discard(45)
print(s)
s1 = {33,44}
s.update(s1)
print(s)
s.clear()
print(s)


{key:value} => item's collection => Dictionary
Dictionary :- Dic is a collection of items. An item is a
pair of key and value . {key:value}
Dictionary can have duplicate values.
Dictionary can not have duplicate keys.
s = {1:345,2:67,5:89,9:574,1:99,1:77 , 10:66}
print(s)

s = {1:345,2:67,5:89,9:574}
print(type(s))
print(s)
print(s[5])

s = {1:3,7:56,'A':78,'Aman':8,3.5:900}
print(s)


d = {}
d = dict()
d = dict({12:567})
d = {2:45,6:35}
print(type(d))
print(d)

Dic has no index it works on keys.
Dic can not be sliced.
Dic can not be replicate.
But Dic can be traversed.


d = {2:45,6:35,3:67,8:25}
for i in d:
    print(i)

    
dic's Method
keys , values , items , update , get

d = {2:45,6:35,3:67,8:25}
for i in d.keys():
    print(i)
print(d.keys())


d = {2:45,6:35,3:67,8:25}
for i in d.values():
    print(i)
print(d.values())



d = {2:45,6:35,3:67,8:25}
for i in d.items():
    print(i)
print(d.items())


d = {2:45,6:35,3:67,8:25}
for i in d.items():
    print(i[1])
print(d.items())


d = {2:45,6:35,3:67,8:25}
for k,v in d.items():
    print(k,' = > ',v)
print(d.items())


d = {2:45,6:35,3:67,8:25}
d2 = {4:99,5:77,6:11}
d.update(d2)
print(d)


d = {2:45,6:35,3:67,8:25}
print(d[3])
# print(d[25]) it will raise an error cause of no key found
print( d.get(8,'Not Found') ) 
print( d.get(88,'Not Found') )


d = {2:45,6:35,3:67,8:25}
for k in d.items():
    if k[0]==6:
        print(k)


  student = {
    'roll no' : 101,
    'name' : 'Raman',
    'course' : 'Python Full Stack',
    'fee' : 28350
    }
for d,v in student.items():
    print(d, ':' ,v)




student = {
'roll no' : [101,102,103,104],
'name':['Ram','Anu','Shanu','Ravi'],
'course':['DS','DA','DSA','Java']
    }
print(student)

roll no
name
course
..
.
.
.
Write a Python program to swap
two variables without using a temporary variable.? 

a = 10
b = 20

a = a+b
b = a-b
a = a-b

print(a)
print(b)



a = 10
b = 20

a = a*b
b = a//b
a = a//b

print(a)
print(b)


a = 10
b = 20

a = a^b
b = a^b
a = a^b

print(a)
print(b)



a = 10
b = 20

a , b = b , a

print(a)
print(b)
'''

