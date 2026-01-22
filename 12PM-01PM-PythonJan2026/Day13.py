"""
Sequenctial Data Type
Tuple:- Tuple is also a collection of hetreogenous
data type elements like list
Syntax:-
tuple_name = ( ele1,ele2,... )

Ways to create a tuple
t = (23,34,5,67,789)
t = (34,67.34,True , 'A',3+8j , 'Aman')
t = ()
t = tuple()
t = tuple([23,34,56,678,90,45])
print( t )

Tuple works on INDEX (backward , forward)
t = (23,45,56,67,8,89,34)
print(t)
tuple_name[index]
print( t[2] )
print( t[-4] )

Tuple Can be SLICED
tuple_name[start:stop:step]
t = (23,45,56,67,8,89,34)
print(t)
print(t[2:5])
print(t[-5:-2])


Tuple Can be Replicate
t = (3,4,5,67,8,9)
print(t)
print(t*3)

Tuple can BE TRAVERSE/ITTERATION
t = (34,56,67,788,90)
print(t)
for x in t:
    print(x)

BUILT-IN Functions
    sum , max , min , len
Function:-  A function is a block of statements
that perform a specific task and return a value

t = (23,4,56,67,89)
print(t)
print( sum(t) )
print( max(t) )
print( min(t) )
print( len(t) )
print( sum(t)/len(t) )


Tuple's Methods
    count , index 


t = (34,78,56,34,56,87,34,67,89)
print(t)
print( t.count(34) )
print( t.index(87) )


Tuple is immuteable (You can not change anything in the tuple)
Tuple is faster than the list due to its immuteability


# LIST COMPREHENSION

li = [23,54,56,78,90]
li = [x for x in range(1,11)]
li = [ x for x in range(1,11) if x%2==0 ]
li = [x*x for x in range(1,11)]
li = [x*x*x for x in range(1,11)]
li = [ x*x for x in range(1,11) if x%2==0 ]
print(li)

"""
