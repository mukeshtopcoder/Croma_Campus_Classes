"""
Conditional Statements
Looping:-   for , while
Loop:- Loop is use to perform a same task again and again

print( *range(1,5,1) )
print( *range(1,11,1) )

FOR
Syntax:-

    for variable_name in range(start,stop,step):
        statements
Example:-
for a in range(1,5,1):
    print("Hello India")

for a in range(1,7,2):  
    print("Hello India")

for a in range(1,11,1):
    print( a )

for a in range(2,21,2): 
    print( a )

#  by default step value = 1
for a in range(1,6): 
    print( a )

#  by default step value = 1
for a in range(5,9): 
    print( a )

#  by default step value = 1 , start value = 0
for a in range(5):  
    print( a )

for i in range(1,11):
    print(i)
    if i==5:
        print("Hello India")

# break exit from the current loop
for i in range(1,11): # 1 2 3 4 5
    print(i)
    if i==5:
        break

# break exit from the current loop
for i in range(1,11):
    if i==5:
        break
    print(i)


# continue skip the upcoming task or go to the next iteration
for i in range(1,11):
    if i==5:
        continue
    print(i)


# continue skip the upcoming task or go to the next iteration
for i in range(1,11): 
    print(i)
    if i==5:
        continue

# pass , do nothing  (it pass code forward)
for i in range(1,5):
    if i==3:
        pass
    print(i)


if 10>5:
    pass
print("Hello")


else

for i in range(1,5):  
    print(i)
else:
    print(0)

else will work with loop, Output:-  1 2 3 4 0



for i in range(1,7):  
    print(i)
    if i==4:
        break
else:
    print(0)

# else will work only when a loop will run completly
# else will work only when a loop will not break

# WAP to print counting from 1 to N (user input)

n = int( input("Enter Range From 1 to : ") )
for i in range(1,n+1):
    print(i)

# WAP to print table of a number.
num = int(input("Enter Number To Print Table : "))
for i in range(1,11):
    print(i*num)

#   5 * 1 = 5
#   5 * 2 = 10

num = int(input("Enter Number To Print Table : "))
for i in range(1,11):
    print(num,"*",i,"=",i*num)

# WAP to print all even numbers from 1 to 20

for i in range(1,21):
    if i%2==0:
        print(i)
        
"""
