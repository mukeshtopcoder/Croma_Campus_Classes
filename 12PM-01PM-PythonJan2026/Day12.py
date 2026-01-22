"""
Collection / Sequence Data Type (LIST/TUPLE)
List:- List is a collection of hetreogenous(different)
data elements
Syntax:-
list_name = [ele1, ele2 ,...]

Example
Ways to create a list
li = [23,45,67,78,45]
li = [234 , 34.67 , True , 'A', 'Aman', 3+9j]
li = []
li = list()
li = list([34,566,7,89,567])
print( li )


INDEX
List works on index
forward index    ( 0,1,2,3,4,.. )
backward index   (-1,-2,-3,-4...)
list_name[index]

li = [23,45,67,78,45]
print( li )
print( li[2] )
print( li[-4] )

SLICING
List supports slicing
list_name[ start:stop:step ]

li = [23,45,67,78,45,57,13,47]
print( li )
print( li )
print( li[3:6:1] )
print( li[3:6] )
print( li[ :3 ] )
print( li[ 4: ] )
print( li[2:7:2] )
print( li[-1:-4] )  # it will not work because step is 1
print( li[-1:-4:-1] ) # -1:-4:-1  (-1-1)
print( li[-5:-2] )  # -5:-2  (-5+1)
print( li[ : : -1 ] )


TRAVERSING / ITTERATION

li = [23,45,67,78,45,57,13,47]
for a in li:
    print( a )

REPLICATION
li = [2,5,7,9,0]
print(li*3)  #  it will repeat the list for 3 times

Built-in Functions
    sum , max , min , len

li = [2,5,7,9,0]
print( li )
print( sum(li) )
print( max(li) )
print( min(li) )
print( len(li) )   # count elements in a list
print( sum(li)/len(li) )

TRAVERSING / ITTERATION

li = [23,45,56,78,90]
print(li)
for x in range(len(li)):
    print(li[x])

List's Method/Function
    append , extend , insert
li = [23,56,67,89,35]
print(li)
li.append(99)
print(li)
li.insert(2,88)
print(li)
li2 = [11,22,33]
li.extend(li2)
print(li)
li3 = [44,55,66]
li = li+li3
print(li)


remove , pop , del(keyword) , clear

li = [23,45,56,78,58,35]
print( li )
li.pop(2)   # pop(index)
print(li)
li.pop()   #  pop()  -> remove last elements
print(li)
li.remove(45)   #  remove(value/element)
print(li)
del li[2]
print(li)
li.clear()  # remove all the elements
print(li)

    count , index

li = [23,67,90,23,56,78,23,56,67]
print(li)
print( li.count(23) )  # count frequency of 23 in list
print( li.index(56) )  # return index of element (error if not found #ValueError)

    sort , reverse

li = [23,456,78,90,87,65,32,45,678]
print( li )
li.reverse()
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)

"""

