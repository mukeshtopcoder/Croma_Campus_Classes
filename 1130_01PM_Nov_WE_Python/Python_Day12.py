"""
Sequence Data Types
    LIST , TUPLE

a = 12
a = [23,78,5,23]      # List
a = (23,78,5,23)      # Tuple

LIST
List is a collection of Heterogeneous Elements (Different Data Type)

a = 12
a = [23,56,89,35,84]
a = [24,'A',236.45,'Aman',True,3+7j]
a = []
a = list()
a = list([32,55,89,43,78])
print(a)
print( type(a) )

List works on index
    forward index (0,1,2,3...) ,
    backward index (-1,-2,-3,-4...)
    li = [2424,67557,79797]
    li[index]
Example:-

li = [23,56,89,85,36]
print(li)
print(li[2])        # 89
print(li[-2])       # 85

SLICING
li = [12,45,56,78,89,90]
    li[start:stop:step]

li = [23,56,89,85,36]
print(li)
print(li[2:4:1])
print(li[2:4])

li = [23,56,89,34,56,67,78,38,90,90,54,85,36]
print(li)
print(li[3:6])
print(li[2:8:2])
print(li[1:10:3])


li = [23,56,89,34,56,67]
print(li)
print(li[-4:-1])
print(li[-2:-5])
print(li[-2:-5:-1])

REPLICATION

a = [2,4,6,7]
print( a )
print( a*3 )

TRAVERSING

for val in list_name:
    statement

li = [34,67,68,35,24,68]
for x in li:
    print(x)

li = [34,67,6]
for a in li:
    print(a*1000)

# Built-in Functions
    sum , max , min , len

li = [23,67,90,78,45,12,64,56,89]
print( sum(li))
print( max(li))
print( min(li))
print( len(li))
print( sum(li)/len(li))

Methods
    append , insert , extend
    remove , pop , clear , del keyword
    count

li = [23,45,23]
print(li)
li.append(99)
print(li)
li.insert(2,88)
print(li)
li2 = [77,66]
li.extend(li2)
print(li)
li.remove(88)
print(li)
li.pop()
print(li)
li.pop(3)
print(li)
del li[3]
print(li)
print(li.count(23))
li.clear()
print(li)

# sort
li = [23,67,90,47,35]
li.sort()
print(li)

# sort
li = [23,67,90,47,35]
li.sort(reverse=True)
print(li)


# reverse
li = [23,67,90,47,35]
print(li)
li.reverse()
print(li)

"""
