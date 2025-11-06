"""
SEQUENCE DATA TYPES :- LIST , TUPLE
List:- A list is a collection different type of data.

li = [23,5,78,90,76,43,33]

li = [23,5,78,90,76,43,33]
li = [43,'A','Aman',34.67,True,3+8j,0b1001,0x2FA]
li = []
li = list([23,56,89,34,21])
li = list()
print(li)


li = [23,45,67,78,845,32,23]
print(li)


list works on index:-
forward index   (0,1,2,3..)
backward index  (-1,-2,-3,-4...)

list_name[index]

li = [23,45,67,78,845,32]
print(li)
print(li[2])


print(li[4])


li = [23,45,67,78,845,32]
print(li)
print(li[4])
print(li[-2])


Slicing
list_name[start_index,stop_index,step]

li = [23,45,67,78,845,32]
print(li)
print(li[2:5:1])
print(li[2:5:2])
print(li[2:5])
print(li[:5])  # default start value = 0
print(li[3:])  # default len of list will be stop

# Traversing
li = [23,45,67,78,845,32]
print(li)
for x in li:
    print(x)

# WAP TO PRINT ONLY ODD NUMBERS OF LIST

li = [23,45,67,78,845,32]
print(li)
for x in li:
    if x%2!=0:
        print(x)

# REPLICATION

li = [1,2,3,4,5]
print(li)
print(li*3)


# BUILT_IN FUNCTIONS
sum , max , min , len

li = [23,78,54,12,78,34]
print(li)
print(sum(li))
print(len(li))
print(min(li))
print(max(li))
print(sum(li)/len(li))

# TRAVERSING
li = [12,67,98,53,24,67]
print(li)
for i in range(0,len(li)):
    print(li[i])

# METHODS
append , extend , insert

li = [23,66,24,26,67]
print(li)
li.append(88)
print(li)
li.insert(1,99)
print(li)
li.insert(19,77)   # element will insert in the last
print(li)
li2 = [11,22,99,22]
li.extend(li2)
print(li)

for i in range(3):
    x = input('Enter A NUmber : ')
    li.append(x)
print(li)


pop , remove , del(keyword)

li = [23,66,24,26,23,67]
print(li)
li.pop()
print(li)
li.pop(2)    # index
print(li)
li.remove(26)   # value
print(li)


count , index
li = [23,66,24,26,23,67]
print(li)
print( li.count(23) )
print( li.index(26) )
print( li.index(99) )

reverse
li = [23,66,24,26,23,67]
print(li)
li.reverse()
print(li)

# SORT

li = [23,66,24,26,23,67]
print(li)
li.sort()
print(li)


li = [23,66,24,26,23,67]
print(li)
li.sort(reverse=True)
print(li)


li = [23,66,24,26,23,67]
print(li)
print(li.index(23,1))


# sum ,  max , min , len

SUM
li = [2,34,5,67,89,32]
add = 0
for x in li:
    add+=x
print(add)

MAX

li = [2,34,5,67,89,32]
maxx = li[0]
for x in li:
    if maxx<x:
        maxx=x
print(maxx)


MIN
li = [2,34,5,67,89,32]
maxx = li[0]
for x in li:
    if maxx>x:
        maxx=x
print(maxx)


COUNT
li = [2,34,5,67,89,32]
count = 0
for x in li:
    count+=1
print(count)

"""

