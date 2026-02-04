"""
Doubt Session
WAP to find the longest increasing sub sequence in a list
li = [23,56,89,78,6,4,23,4,56,67,78,89,90,23,56,34]

li = [23,56,89,78,6,4,23,4,56,67,78,89,90,23,56,34]
print(li)
lss = []
i = 0
while i<len(li)-1:
    temp = []
    for j in range(i+1,len(li)):
        if li[i]<li[j]:
            temp.append(li[i])
            i=i+1
        else:
            temp.append(li[i])
            i=i+1
            break
    if len(temp)>len(lss):
        lss = temp.copy()
print(lss)


# WAP to group elements based on frequency
li = [2,4,6,8,3,6,5,3,4,6,7,9,6,4,3,5,6,7,9,0,7,5,3]

li = [2,4,6,8,3,6,5,3,4,6,7,9,6,4,3,5,6,7,9,0,7,5,3]
gli = []
temp = []
for x in li:
    if x not in temp:
        temp.append(x)
        gli.extend([x]*li.count(x))

print(gli)


li = [2,4,6,8,3,6,5,3,4,6,7,9,6,4,3,5,6,7,9,0,7,5,3]
gli = []
temp = []
for x in li:
    if x not in temp:
        temp.append(x)
        gli.append([x]*li.count(x))

print(gli)

WAP TO find the element with maximum frequency in a tuple

t = (2,4,6,8,3,6,5,3,4,6,7,9,6,4,6,6,6,7,9,0,7,5,3)
temp = []
maxx = 0
val = 0
for x in t:
    if x not in temp:
        temp.append(x)
        if t.count(x)>maxx:
            maxx = t.count(x)
            val = x

print("Element ",val,"Frequency ",maxx)




WAP to check a number is Prime using UDF

def checkPrime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True


if checkPrime(17):
    print("Prime")
else:
    print("Not Prime")

    
"""
# WAP to find all prime numbers from 1 to 100
def checkPrime(num):
    for i in range(2,num//2+1):
        if num%i==0 or num==1:
            return False
    return True

for i in range(1,101):
    if checkPrime(i):
        if i>1:
            print(i)

