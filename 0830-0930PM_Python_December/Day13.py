"""
Collection (List , Tuple , Set , Dictionary , String)
LIST:- list is a collection of hetreogenous data type elements
a = 10    Variable
li = [23,56,87,56,32,89]    # List

Ways to create a list
li = [23,45,78,90,45]
li = [23,45.56,True,'A',3+8j,'Aman']
li = []
li = list()
li = list([23,34,56,78,94])
li = list((23,34,56,78,94))
print(li)

List works on INDEX (backward forward)
list_name[index]
forward =>  0,1,2,3,4...
backward=>  -1,-2,-3....

li = [23,45,78,90,45]
print(li)
print( li[2] )
print( li[-4] )

LIST supports SLICING
list_name[start:stop:step]

li = [23,45,78,90,45]
print(li)
print( li[1:4:1] )
print( li[1:4] )
print( li[1:4:2] )
print( li[-4:-1] )
print( li[-1:-4:-1] )

LIST supports REPLICATION
li = [1,2,3,4]
print(li)
print(li*4)

LIST supports TRAVERSING/ITTERATION

li = [23,45,56,7,65,43,21]
for x in li:
    print(x)


Built-in Functions
    sum , max , min , len
li = [23,34,556,786,543,32]
print( li )
print( sum(li) )  # add all the elements
print( max(li) )  # print max element
print( min(li) )  # print min element
print( len(li) )  # count the elements

List's METHODS
    append , insert , extend

li = [23,34,45,67,56]
print(li)
li.append(99)
print( li )
li.insert(2,88)
print(li)
li2 = [22,33,44,55]
li.extend(li2)
print(li)

    remove , pop , del (keyword) , clear

li = [23,34,4,56,7,8]
print(li)
li.pop(2)   # delete by index
print(li)
li.pop()   # by default last value will be deleted
print(li)
li.remove(34)   #  delete by value
print(li) 
del li[1]
print(li)
li.clear()
print(li)


    count , index

li = [23,5,67,12,23,45,23,45,23,43,34]
print(li)
print( li.count(23) )
print( li.index(45) )
print( li.index(45,6,10) )  # index(ele,start,stop)


    sort , reverse

li = [23,34,45,567,89,45,54,34]
print(li)
li.reverse()
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)


# TUPLE
Tuple is also a collection like a list of hetreogenous elements
tuple_name = ( 23,43,45,56,67,23,34,45 )

Ways to create a tuple
t = (23,3,3445,5,56,67)
t = (23,34.56,3+8j,True,'Aman')
t = ()
t = tuple()
t = tuple([23,43,45,56,67])
t = tuple((23,43,45,56,67))
print(t)

TUPLE works on INDEX
backward -1,-2,-3,.. and forward 0,1,2,3,...

t = (23,3,3445,5,56,67)
print(t)
print(t[1])
print(t[-2])


Tuple Support SLICING
t = (23,3,3445,5,56,67)
print(t)
print(t[3:5])


Tuple supports REPLICATION
t = (1,3,3,4,6)
print(t)
print(t*3)


Tuple supports TRAVERSING/ITTERATION
t = (23,45,67,89,34)
for x in t:
    print(x)


Built-in Functions
    sum , max , min , len

t = (23,4,45,56,66,77,78,23)
print(t)
print(sum(t))
print(max(t))
print(min(t))
print(len(t))


Tuple's METHODS
        index , count

t = (23,34,54,23,43,56,23,4,56,23)
print(t)
print(t.count(23))
print( t.index(4) )


Tuple is immuteable (You can not change anything in the tuple)
List is muteable (You can make any change in the list)
Tuple is faster than the list because of its immuteablity

# WAP to find all the even numbers of a list/tuple
li = [23,4,67,78,65,45,32,45,56]
for x in li:
    if x%2==0:
        print(x)

li = (23,4,67,78,65,45,32,45,56)
for x in li:
    if x%2==0:
        print(x)


# WAP to find cube of every element of a list/tuple
li = [1,2,3,4,5,6,7,8,9,10]
for x in li:
    print(x*x*x)


# WAP to add all elements of a list without sum function

li = [2,34,4,45,56,63,68]
s = 0
for x in li:
    s = s+x
print(s)
print( sum(li) )

"""

