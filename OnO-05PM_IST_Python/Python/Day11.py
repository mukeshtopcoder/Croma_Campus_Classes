"""
Collection:- store more than one element in one entity
a = 10
List:- List a collection of hetreogenous values.
a = [34,56,78,90,45]   # List

Ways to create a list

a = [34,56,78,90,46,23]
a = [24,'A',26.82,'Aman',True,3+8j]
a = []
a = list()
a = list([34,67,43,67,89])
print(a)


List supports INDEX
forward index    (0,1,2,3...)
backward index   (-1,-2,-3..)
list_name[index]

a = [34,45,78,35,76,54,34]
print( a )
print( a[2] )
print( a[5] )
print( a[-2] )
print( a[-4] )


LIST supports SLICING
slicing
list_name[start:stop:step]

a = [34,54,56,7,78,89,76,56,4,3]
print( a )
print( a[3:8] )
print( a[2:8:2] )

List Supports REPLICATION

li = [34,45,54,56,67]
print(li)
print(li*2)

Built-in Functions
    sum , max , min , len

li = [34,45,56,67,65]
print(li)
print( sum(li) )
print( max(li) )
print( min(li) )
print( len(li) )

List supports Traversing/Itteration

li = [34,89,74,72,56]
for x in li:
    print(x)


li = [34,89,74,72,57]
for x in li:
    if x%2==0:
        print(x)


# WAP to find max value from a list using for loop
li = [34,89,74,72,57]
m = 0
for x in li:
    if m<x:
        m=x
print(m)


LIST's Method
    append, extend , pop , remove , clear

li = [23,45,67,78,89,90]
print( li )
li.append(99)
print(li)
li2 = [11,22,33]
li.extend(li2)
print(li)
li.pop(2)     # li.pop(index)
print(li)
li.remove(90)    # li.remove(value)
print(li)
li.clear()
print(li)

sort , reverse

li = [57,90,23,56,89,73]
print( li )
li.reverse()
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)

"""

