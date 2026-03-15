"""
Collections:- range() , list , tuple , set , dictionary ,
string , array(numpy)

List:- A list is a collection of hetregenous elements
li = [23,45,78,8,76,45]  # List


Ways to create a List

li = [23,45,56,78,89,54]
li = [25,46.75,'A',True,'Aman',3+8j]
li = []
li = list([23,45,67,89])
li = list((23,45,67,89))
li = list()
print( li )


List can work on INDEX
Backward    -1,-2,-3..
forward     0,1,2,3,..

list_name[index]
li = [34,99,67,7,8,67,56,34]
print(li)
print(li[4])
print(li[-2])

List can be Sliced
list_name[start : stop : step]

li = [34,99,67,7,8,67,56,34]
print(li)
print( li[3:6:1] )
print( li[3:6] )
print( li[3:6:2] )
print( li[-1:-4:-1] )
print( li[-5:-2] )


li = [34,99,67,7,8,67,56,34]
print(li)
print( li[5:] )
print( li[:4] )


List Supports the Replication
li = [1,2,3,4]
print(li)
print(li*3)


List supports the traversing/itteration
li = [34,56,78,89]
print(li)
for x in li:
    print(x)


li = [34,56,42,68,80,76,35,78,89]
print(li)
for x in li:
    if x%2!=0:
        print(x)


Built-in Functions
    sum , max , min , len

li = [34,56,42,68,80,76,35,78,89]
print(li)
print( sum(li) )
print( max(li) )
print( min(li) )
print( len(li) )
print( sum(li)/len(li) )


List's Method
    append , extend , insert

li = [34,67,89,54]
print(li)
li.append(99)
print(li)
li.insert(2,88)
print(li)
li2 = [11,22,33]
li.extend(li2)
print(li)


    pop , remove , clear , del(keyword)

li = [34,67,65,51,56]
print(li)
li.pop()
print(li)
li.pop(1)           # pop(index)
print(li)
li.remove(51)
print(li)
del li[0]
print(li)
li.clear()    # clear will remove all the elements
print(li)


    sort , reverse

li = [23,45,67,89,67,56,34,23,16]
print(li)
li.reverse()
print(li)
li.sort()
print(li)
li.sort( reverse=True)
print(li)


Tuple
Tuple is same as list,
it is also a collection of hetreogenous elements
but a tuple is immuteable and list is muteable
it means u can not change anything in the tuple
and tuple is faster than the list due to its immortality

Syntax:-
t = (43,56,7,90,36,76,54)
t = (34,25.46,'A',True,'Aman',3+8j)
t = ()
t = tuple([23,45,56,78,89])
t = tuple((23,45,56,78,89))
print( t )


Tuple Support the INDEX
backward
forward
t = (43,56,7,90,36,76,54)
print( t )
print( t[2] )
print( t[-2] )


Tuple Support Slicing

t = (43,56,7,90,36,76,54)
print( t )
print( t[2:6] )
print( t[-5:-1] )


You can perform traversing/itteration with tuple
t = (43,56,7,90,36,76,54)
print( t )
for x in t:
    print(x)


t = (43,56,7,90,36,76,54)
print( t )
for x in t:
    if x%2!=0:
        print(x)


Tuple also support Replication
t = (34,56,53)
print( t )
print(t*4)


Built-in Functions
    sum , max , min , len

t = (34,56,53,56,78,35)
print( t )
print( sum(t) )
print( max(t) )
print( min(t) )
print( len(t) )
print( sum(t)/len(t) )


Tuple's Method
    count , index
    
t = (34,67,87,56,67,73,67,14)
print( t )
print( t.count(67) )
print( t.index(87) )
print( t.index(67,2) )


# Tuple is immuteable but you can delete a tuple's object
t = (34,56)
print(t)
del t
print(t)
  
"""
