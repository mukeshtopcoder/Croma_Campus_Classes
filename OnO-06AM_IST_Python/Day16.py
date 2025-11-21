"""
import copy
a = [1,2,3,[6,7,8],5]
b = copy.deepcopy(a)
b[1] = 9
b[3][1] = 99
print(a)
print(b)


[[1, 2], [1, 2], [1, 2]]

a = [[1,2]]
a = a*3
a[0][0] = 99
print(a)


list comprehension

a = [[1,2] for x in range(3)]
a[0][0] = 99
#print(a)


a = [1,2,3,4,5,6,7,8,9,10]
a = [x for x in range(1,11)]
a = [x for x in range(2,21,2)]
a = [[1,2] for x in range(3)]
a[0][0] = 99
print(a)


Built-in Libraries
math 

import library_name
library_name.method(argument)

import math
math.sqrt(9)

import math
print( math.sqrt(9) )
print( math.factorial(5) ) # 5!  => 5*4*3*2*1
print( math.pow(2,5) )
print( math.pi )
print( math.ceil(23.12) )
print( math.floor(23.99) )

import random

import random
print( random.random() )



import random as r
import math
print( r.random() )
print( r.random()*100 )
print( math.floor(r.random()*100) )



import random as r

print( r.randint(1,6) )
print( r.randint(1000,9999) )
print( r.randint(100000,999999) )


import random as r
li = ['Apple','Banana','Grapes','CHerry','Dates']
print( r.choice(li) )
print( r.choices(li,k=2) )  # both values can be same
print( r.sample(li,k=2) )   # both values can not be same


# UDF :- User Define Functions
"""
