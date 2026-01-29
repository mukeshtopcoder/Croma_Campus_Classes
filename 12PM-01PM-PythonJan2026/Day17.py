"""
Q1:- Merge two list and remove duplicate
li1 = [1,2,3,4,5,6]
li2 = [4,5,6,7,8,9]

# li3 = list(set(li1+li2))
# print(li3)
for e in li2:
    if e not in li1:
        li1.append(e)
print(li1)


Q2:- Rotation of a list
# Right Rotation
li = [0,1,2,3,4,5,6,7,8,9]
print(li)
n = int(input("How Many Rotation : "))
for i in range(n):
    li.insert(0 , li[len(li)-1])
    li.pop(len(li)-1)
print(li)

# Left Rotation

li = [0,1,2,3,4,5,6,7,8,9]
print(li)
n = int(input("How Many Rotation : "))
for i in range(n):
    li.insert(len(li), li[0])
    li.pop(0)
print(li)

Q3:- WAP to convert a nested list into a flatten list
Nested List : [1,2,[3,4,5],6,[7,8,9]]
Flatten List: [1,2,3,4,5,6,7,8,9]

nli = [1,2,[3,4,5],6,[7,8,9]]
flat = []
for e in nli:
    if isinstance(e,list):
        flat.extend(e)
    else:
        flat.append(e)
print(flat)

Q4:- WAP to find largest value in a digit
num = 365
li = []
while num>0:
    rem = num%10
    li.append(rem)
    num = num//10
print("Largest Digit :",max(li))

num = 374
maxx = 0
while num>0:
    rem = num%10
    if maxx<rem:
        maxx=rem
    num = num//10
print("Largest Digit :",maxx)


# WAP to count the frequency of each charcter in a string
st = "AMANKUMAR"
dic = dict()
for ch in st:
    dic.update({ch:st.count(ch)})
print(dic)

# WAP to split a list into even or odd number
li = [23,34,45,667,8,90,89,876,43,45,45,67,8]
even = []
odd = []
for e in li:
    if e%2==0:
        even.append(e)
    else:
        odd.append(e)

print(even)
print(odd)


# WAP to unpack the tuple elements

t = (23,45,78)
a,b,c = t
print(a)
print(b)
print(c)

# WAP to remove an element from a tuple 

t = (23,34,56,67,84,99)
print(t)
t = list(t)
t.remove(84)
t = tuple(t)
print(t)

# WAP to create a nested tuple and access its element

t = (2,45,6,7,(54,56,67,78),99)
for e in t:
    if isinstance(e,tuple):
        for x in e:
            print(x)
    else:
        print(e)

"""
