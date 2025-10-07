"""
lambda :- Lambda is use to write a small definition's
function.

# WAP function to find cubes of all numbers of list.

def cube(num):
    return num**3

li = [1,2,3,4,5,6]
for x in li:
    print(cube(x))


# Using lambda
# WAP function to find cubes of all numbers of list.

cube = lambda num : num**3

li = [1,2,3,4,5,6]
for x in li:
    print(cube(x))


# MAP , FILTER , REDUCE
map

cube = lambda num:num**3

li = [1,2,3,4,5,6,7,8,9]

result = list(map(cube , li))

print(result)



cube = lambda num:num**3

li = [1,2,3,4,5,6,7,8,9]

print( list(map(cube , li)) )



cube = lambda num:num**3

print( list(map(cube , [1,2,3,4,5,6,7,8,9])) )


# Anonymous Functions / lambda expression
print( list(map(lambda num:num**3 , [1,2,3,4,5,6,7,8,9])) )


def even(num):
    return num%2==0

li = [32,54,67,9,98,67,54,23,56,89,45]

for x in li:
    if even(x):
        print(x)



even = lambda num : num%2==0

li = [32,54,67,9,98,67,54,23,56,89,45]

for x in li:
    if even(x):
        print(x)


    
# Filter

even = lambda num : num%2==0

li = [32,54,67,9,98,67,54,23,56,89,45]

result = list( filter(even , li) )

print(result)



even = lambda num : num%2==0

li = [32,54,67,9,98,67,54,23,56,89,45]

print(list( filter(even , li) ))


even = lambda num : num%2==0

print(list( filter(even,[32,54,67,9,98,67,54,23,56,89,45])))



print(list( filter(lambda num : num%2==0,[32,54,67,9,98,67,54,23,56,89,45])))



reduce

from functools import reduce

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

add = lambda a,b : a+b

result = reduce(add , li)
print(result)


# map , reduce , filter , lambda

# WAF to find the sum of all even number's square from a list

from functools import reduce
li = [12,4,67,89,23,87,56,34]
print(li)
even_num = list(filter(lambda num : num%2==0, li))
print(even_num)
sq_num = list(map(lambda val : val**2 , even_num))
print(sq_num)
result = reduce(lambda a,b:a+b , sq_num)
print(result)


from functools import reduce
li = [12,4,67,89,23,87,56,34]
even_num = list(filter(lambda num : num%2==0, li))
sq_num = map(lambda val : val**2 , even_num)
result = reduce(lambda a,b:a+b , sq_num)
print(result)


from functools import reduce
li = [12,4,67,89,23,87,56,34]
print(reduce(lambda x,y:x+y , map(lambda x:x**2 ,filter(lambda x:x%2==0 , li))))


"""

