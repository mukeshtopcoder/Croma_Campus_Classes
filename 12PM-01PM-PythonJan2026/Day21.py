"""
# WAF to calculate the cube of a number

def cube(num):
    return num**3

print(cube(4))


Advance Python
lambda expression
lambda keyword is use to write small function definition

function_name = lambda parameter : definition

# WAF to calculate the cube of a number

cube = lambda num : num**3

print(cube(3))


# WAF to add two numbers

add = lambda a,b : a+b

print( add(20,48) )


# WAF to check a number is even or odd

even = lambda num : "Even" if num%2==0 else "Odd"

print( even(13) )
print( even(18) )



# WAF to calculate the cube of a number

cube = lambda val:val**3
li = [x for x in range(1,11)]
print(li)

for m in li:
    print(cube(m))





# WAF to calculate the cube of a number

cube = lambda val:val**3
li = [x for x in range(1,11)]
print(li)
cu = []
for m in li:
    cu.append(cube(m))

print(cu)




map
map is a keyword which is use to aplly a function/method
on a collection

# WAF to calculate the cube of a number

cube = lambda val:val**3
li = [x for x in range(1,11)]
print(li)

cu = list( map(cube , li) )
print(cu)



filter

# WAP to find all even numbers from a list

checkEven = lambda num : True if num%2==0 else False
li = [23,45,7,89,78,56,54,23,65]

even = list( filter( checkEven , li ) )
print(even)



# WAP to find all even numbers from a list

checkEven = lambda num : num%2==0
li = [23,45,7,89,78,56,54,23,65]

even = list( filter( checkEven , li ) )
print(even)


# WAP to find all even numbers from a list

checkEven = lambda num : num%2==0
li = [23,45,7,89,78,56,54,23,65]

even = list( filter( checkEven , li ) )
print(even)



# WAP to find all prime numbers form a list
def checkPrime(num):
    if num>1:
        for x in range(2,num//2+1):
            if num%x==0:
                return False
        return True
    else:
        return False

li = [23,56,78,90,78,17,35,24,5,789,35]
prime = tuple( filter(checkPrime , li) )
print(prime)


reduce

from functools import reduce
add = lambda a,b : a+b
li = [1,2,3,4,5,6,7,8,9,10]

s = reduce( add , li )
print(s)


# Anonymous Function

li = [12,23,45,56,67,89,90,89]

even = list( filter( lambda num:num%2==0 , li ) )
print(even)


# find cubes

print( list( map(lambda x:x**3 , [1,2,3,4,5,6,7]) ) )



# WAP to find sum of the square of all even numbers
of a list

from functools import reduce
li = [1,2,3,4,5,6,7,8,9,10]
checkEven = lambda num:num%2==0
even = filter( checkEven , li )
sq = map( lambda val:val**2 , even )
s = reduce(lambda a,b:a+b , sq)
print(s)

from functools import reduce
li = [1,2,3,4,5,6,7,8,9,10]
checkEven = lambda num:num%2==0
even = list(filter( checkEven , li ))
print(even)
sq = list(map( lambda val:val**2 , even ))
print(sq)
s = reduce(lambda a,b:a+b , sq)
print(s)


from functools import reduce
li = [1,2,3,4,5,6,7,8,9,10]
print( reduce(lambda a,b:a+b ,map(lambda a:a*a,filter(lambda x:x%2==0 ,li))) )


"""
