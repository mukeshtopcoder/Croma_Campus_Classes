"""
List
List's Methods

append , extend , insert

li = [23,78,36,75,26]
print(li)
li.append(99)
print(li)
li2 = [11,22,33]
li.extend(li2)
print(li)
li.insert(1,55)   # insert(index , value)
print(li)


pop , remove , clear

li = [23,56,78,89,76,45,34]
print(li)
li.pop()
print(li)
li.pop(3)   # pop(index)
print(li)
li.remove(76)   # remove(value)
print(li)
li.clear()
print(li)


count , index

li = [34,56,67,56,89,25]
print(li)
print( li.count(56) )
print( li.index(89) )

reverse , sort

li = [23,45,67,6754,23,56]
print(li)
li.reverse()
print(li)
li.sort()   # by default asc
print(li)
li.sort(reverse=True)   # desc
print(li)


    copy
a = [23,45,78,73,25]
b = a.copy()
print(b)
b[2] = 99
print(b)
print(a)



TUPLE
Tuple is also a collection of hetregenous element like LIST 
List is muteaable (changeable) You can make changes
Tuple is immuteable (unchangeable) you can not make any change

Syntax:-
tuple_name = ( ele1,ele2,ele3.. )

t = (34,26,66,73,83)
t = (24,5.46,'A',True,'Aman',4+8j)
t = ()
t = tuple([2,4,6,789,45])
t = tuple((2,4,6,789,45))
t = tuple()
print( t )
print( type(t) )


Tuple works on INDEX
backward and forward
backward =>  -1,-2,-3...
forward  =>  0,1,2,3,4..

tuple[index]

t = (34,56,67,78,35)
print(t)
print( t[2] )
print( t[-4] )


Tuple can SLICED
tuple_name[start_index : stop_index , step]

t = (34,56,78,89,26,56)
print(t)
print( t[2:5:1] )
print( t[2:5] )
print( t[2:5:2] )
print( t[-4:-1] )  
print( t[-1:-4:-1] )

Tuple supports Replication

t = (1,3,4,5)
print(t)
print( t*3 )


Tuple support Traversing/Itteration
t = (34,57,6,5,475,68,72)
print( t )
for x in t:
    print(x)


t = (34,57,6,5,475,68,72)
print( t )
for x in t:
    if x%2==0:
        print(x)


Built-in Functions
    sum , max , min , len

t = (34,67,8978,56,5,35)
print(t)
print(sum(t))
print(max(t))
print(min(t))
print(len(t))
print(sum(t)/len(t))


Tuple's Method
        index , count

t = (234,56,78,8,89,67,78)
print(t)
print( t.count(78) )
print( t.index(8) )


t = (34,45,[23,45,67],67)
print( t )
print( t[2] )
t[2].append(99)
print(t)
t[2].clear()
print(t)


t1 = (1,2,3)   # 
t2 = (1,2,3)
print( t1 is t2 )  # is do not check data , check memory
print( t1 in t2 )

a = (1,2,3)
b = (1,2,3)
print( a is b ) # True

"""
