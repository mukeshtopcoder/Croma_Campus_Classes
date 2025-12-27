"""
Tuple :- It is also a collection of hetreogenous elements
(different data type)
Syntax:- tuple = (34,54,67,78,45)

t = (34,4,56,7,9)
t = (34,567.34,'A',True,'Aman',4+8j)
t = ()
t = tuple()
t = tuple([32,45,67,89,23])
print(t)

Tuple works on INDEX
forward (0,1,2,3..) and backward indexing(-1,-2,-3...)

t = (34,56,78,89)
print(t)
print(t[1])
print(t[-2])


SLICING
tuple_name[start:stop:step]

t = (34,56,67,8,90,34)
print(t)
print(t[3])
print(t[2:5])
print(t[2:5:2])

REPLICATION

t = (34,5,678,56)
print(t)
print(t*3)

TRAVERSING / ITERATION

t = (34,56,7,9,0,987,65,43,23)
print(t)
for x in t:
    print(x)


Built-in Funtions
sum , max , min , len

t = (34,56,67,89)
print(t)
print(sum(t))
print(max(t))
print(min(t))
print(len(t))
print(sum(t)/len(t))

Methods
    count , index

t = (34,45,34,88,57)
print(t)
print( t.count(34) )
print( t.index(88) )


Tuple is immuteable (You can not delete or add elements)
or you can not make any change in the tuple

Difference between List and Tuple
List is ordered
List is muteable (changeable)
List Syntax []
Slower than Tuple (because of its mutablity)
List use more memory

Tuple is ordered
Tuple is immuetable
Tuple Syntax ()
Tuple is Fast than list (cause of its immutablity)
Tuple use less memory


Programming Questions
# WAP to remove duplicate values from a list.

li = [3,5,7,8,7,6,5,3,2,3,4,5,6,5,4,3,4,6,7,8,9]
print(li)

li2 = []
for i in li:
    if i not in li2:  
        li2.append(i)

print(li2)

# WAP to sort a list in ascending or descending order

li = [23,56,90,67,32,78,45,89,56,36,54]
print(li)
li2 = []
for i in range(len(li)):
    li2.append(max(li))
    li.remove(max(li))

print(li2)

# WAP to split a list into even and odd number's list

li = [43,90,67,34,78,93,56,34,23,56,67,89,97]
print(li)
even = []
odd = []
for x in li:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print(even)
print(odd)

# WAP to find common elements from two list

li1 = [23,34,56,78,89,34,45,56,78,62]
li2 = [34,45,56,67,67,78,90,78,63,56]
common = []
for i in li1:
    if i in li2:
        common.append(i)
        li2.remove(i)
print(common)

# WAP to count positive, negative and zeros in a list

positive = []
negative = []
zero = []
li = [23,45,0,45,-67,78,0,56,34,-34,-56,-67,46]
for x in li:
    if x>0:
        positive.append(x)
    elif x<0:
        negative.append(x)
    else:
        zero.append(x)

print(positive)
print(negative)
print(zero)

print("Positive :", len(positive) )
print("Negative :", len(negative) )
print("Zero :", len(zero) )

"""
