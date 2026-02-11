"""
for loop practice

LOOPING
if we wants to execute a same task again and again

for loop

for variable_name in range(start , stop , step):
    statement/task


for a in range(1,5,1): 
    print("Hello")

for a in range(1,11,1): 
    print(a)


for a in range(1,11,2): 
    print(a)


for a in range(1,11,3): 
    print(a)


for a in range(2,21,2): 
    print(a)


# by default step = 1
for a in range(1,11): 
    print(a)


# by default step = 1
# by default start = 0
for a in range(5): 
    print(a)



num = int(input("Enter A Number : "))
for a in range(1,11): 
    print(a*num)



# break , continue , pass


#  break => it exit from current loop
for i in range(1,11):
    print(i)
    if i==5:
        break


#  break => it exit from current loop
for i in range(1,11):
    if i==5:
        break
    print(i)


#  continue => it take cursor to the next iteration
#   it skip the upcoming code
for i in range(1,11):
    if i==5:
        continue
    print(i)


#  continue => it take cursor to the next iteration
#   it skip the upcoming code
for i in range(1,11):
    if i%3==0:
        continue
    print(i)


#  pass => do nothing
for i in range(1,11):
    if i==5:
        pass
    print(i)


if 10>5:
    pass

print("Hello")


# WAP to find all even number from 1 to 20


for i in range(1,21):
    if i%2==0:
        print(i)


# WAP to find all factors of a number:-
Hint:-    12  =>   1, 2,3,4,6,12

num = 12
for i in range(1,num+1):
    if num%i==0:
        print(i)

"""
