"""
Collections
range , list , tuple , set , dictionary , string , array(Numpy)

LIST:- List is a collection of hetregenous elements
(Different Data Types collection)
Syntax:-
list_name =  [ ele1, ele2, ele3... ]

li = [34,56,67,78,890,34]

WAYS TO CREATE A LIST

li = [25,75,86,89,74,24]
li = [54,35.75,'A',True,3+8j,'Aman']
li = []
li = list([35,78,6,23,7])
li = list((35,78,6,23,7))
li = list()
print(li)
print( type(li) )


LIST works on INDEX
backward    -1,-2,-3,..
forward     0,1,2,3,...
list_name[index_number]



li = [243,67,89,89,76,54,243]
print(li)
print(li[1])
print( li[-3] )


LIST support SLICING
list_name[start_index:stop_index:step_index]

li = [23,57,89,76,56,26,47,68]
print(li)
print(li[3:6:1])
print(li[3:6])
print(li[3:6:2])
print( li[-1:-4: -1] )
print( li[-4:-1] )



LIST support REPLICATION

li = [1,2,3,4,5]
print(li)
print(li*3)  # it will repeat elements for 3 time in the same list


LIST supports Traversing/Itteration

li = [23,56,78,90,76,34,45]
print(li)
for x in li:
    print(x)


li = [23,56,78,91,76,34,45]
print(li)
for x in li:
    if x%2==0:
        print(x)

# Built-in Functions
    sum , max , min , len

li = [34,56,78,89]
print(li)
print(sum(li))
print(max(li))
print(min(li))
print(len(li))
print( sum(li)/len(li) )


"""
