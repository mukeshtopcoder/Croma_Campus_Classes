'''
Sequence Data Type
Tuple:- Tuple is same as list, it is also a collection of
hetreogenous elements. (Different Data Type)
work on index
- forward   (0,1,2,3,4..)
- backward  (-1,-2,-3...)

Tuple Creation

t = ()
t = (2,54,56,67,78,89)
t = (34, 45.73 , 'A' , "Aman" , 3+8j , True)
t = tuple()
t = tuple([34,56,78,89,35,65])
print(t)
print(type(t))

Tuple can work on index
tuple_name[index]

t = (2,54,56,67,78,89)
print(t)
print(t[2])
print(t[-3])


Tuple can be sliced
tuple_name[start_index:stop_index:step]

t = (2,54,56,67,78,89)
print(t)
print(t[2:5:1])
print(t[2:5])
print(t[2:5:2])
print(t[-4:-1])
print(t[-1:-4:-1])


Tuple can be replicate  (Replication)
t = (2,54,56,67,78,89)
print(t*3)


Tuple can be traversed
t = (2,54,56,67,78,89)
for x in t:
    print(x)

built-in functions
sum  , max , min , len

t = (2,54,56,67,78,89)
print(t)
print(sum(t))
print(max(t))
print(min(t))
print(len(t))

Tuple's Method
count , index

t = (2,54,56,67,54,89)
print(t)
print(t.count(54))
print(t.index(89))

Tuple is immuteable.
List is muteable.

----------------------------------------------------
Nested List /Tuple

li = [ 23,4,67,89,45 ]

li = [ 23,4,67,[23,45,45,78],45 ]

print(li)
print(li[3])
print(li[3][1])



li = ( 23,4,67,89,45 )

li = ( 23,4,67,(23,45,45,78),45 )

print(li)
print(li[3])
print(li[3][1])


List of tuples
Tuple of list
li = [(1,2,3),(4,5,6),(6,7,8),(4,5,7)]
print(li)
print(li[1])
print(li[1][2])


'''
t = (32,54,63,[1,2,3],34,56)
t[3].append(99)
print(t)







