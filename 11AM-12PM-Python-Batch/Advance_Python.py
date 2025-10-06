'''

# WAF to find cube of a number.

def cube(num):
    return num**3

print(cube(4))


lambda expression

variable_name/lambda_function_name = lambda var : definition

# WAF to find cube of a number.

cube = lambda num : num**3

print(cube(4))


# WAF to find cube of a number.

cube = lambda num : num**3
li = [1,2,3,4,5,6,7,8]
for x in li:
    print(cube(x))


# WAP to find all even numbers of a list using lambda functions.

even = lambda val : val%2==0
li = [23,45,56,46,78,89,90,90,98,87,76,54,43]
for num in li:
    if even(num):
        print(num) 

even = lambda val : val%2==0
# li = [*range(1,101)]
li = [x for x in range(1,101)]
for num in li:
    if even(num):
        print(num)

# WAF to add all numbers
add = lambda a,b : a+b
li = [2,3,4,4,5,6,7,8,8,9,0]
count = 0
for val in li:
    count = add(count,val)
print(count)


'''
# WAF TO ADD SQUARES OF ALL NUMBERS OF A LIST USING LAMBDA.

add = lambda a,b : a+b**2
li = [2,3,4,4,5,6,7,8,8,9,0]
count = 0
for val in li:
    count = add(count,val)
print(count)







