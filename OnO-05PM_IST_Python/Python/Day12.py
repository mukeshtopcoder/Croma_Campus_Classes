"""
Tuple is also a collection like a list
li = [2,54,56,677]
tu = (34,76,78,89,90,34)

list is muteable (changeable)
tuple is immuteable (unchangeable)

Ways to create a tuple

t = (23,54,56,78,89)
t = (234,67.34,'A',True,3+9j,'Aman')
t = ()
t = tuple([34,4,56,67])
t = tuple((34,4,56,67))
t = tuple()
print( t )

Tuple is also use to works INDEX
backward  (-1,-2,-3...)
forward   (0,1,2,3,...)

t = (45,56,67,78,89)
print(t)
print( t[3] )
print( t[-3] )


Tuple also support SLICING
t = (45,56,67,78,89)
print(t)
print( t[1:4] )


Tuple supports Replication
t = (45,56,67,78,89)
print(t)
print( t*3 )


Tuple Support Traversing/Itteration
t = (45,56,67,78,89)
print(t)
for x in t:
    print(x)


Tuple suppor Built-in Functions
    sum , max , min , len

t = (23,5,67,89)
print(t)
print(sum(t))
print(max(t))
print(min(t))
print(len(t))
print( sum(t)/len(t) )

tuple's Method
    index , count

t = (23,47,67,23,46)
print(t)
print( t.count(23) )
print( t.index(47) )


t = (34,54,56,67,23,34,54,53)
l = list(t)
l.sort()
print(l)


"""
