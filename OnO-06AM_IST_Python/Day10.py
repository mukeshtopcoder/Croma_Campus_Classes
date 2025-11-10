"""
Pattern Programming

12344321
123**321
12****21
1******1

for i in range(4,0,-1):
    for j in range(1,5):
        if j<=i:
            print(j,end="")
        else:
            print("*",end="")
    for j in range(4,0,-1):
        if j<=i:
            print(j,end="")
        else:
            print("*",end="")
    print()

   *
  ***
 *****
*******
 *****
  ***
   *
counter = 1
m = 2
n = 1
z = 1
for i in range(1,8):
    for k in range(z,4):
        print(end=" ")
    z=z+n
    for j in range(0,counter):
        print("*",end="")
    print()
    counter+=m
    if counter==7:
        m=-2
        n=-1


*****
*****
*****
*****
*****
print("*****\n"*5)

for i in range(5):
    print("*"*5)

*
**
***
****
*****
for i in range(1,6):
    print("*"*i)

    *
   **
  ***
 ****
*****

for i in range(1,6):
    print(" "*(5-i),"*"*i)

1
12
123
1234
12345

st = ""
for i in range(1,6):
    st = st+str(i)  
    print(st)


A
AB
ABC
ABCD
ABCDE
st = ""
for i in range(65,70):
    st = st+chr(i)  
    print(st)


12344321
123**321
12****21
1******1

st = "1234"
for i in range(4,0,-1):  
    print(st,end="")
    print(st[::-1])
    st = st.replace(str(i),"*")

0
909
89098
7890987
678909876
56789098765
4567890987654
345678909876543
23456789098765432
1234567890987654321


st = '0'
for i in range(10,0,-1):
    if i!=10:
        st = str(i)+st+str(i)
    print(st)

*******
*     *
*     *
*     *
*     *
*     *
*******

for i in range(1,8):
    if i == 1 or i == 7:
        for j in range(1,8):
            print("*",end="")
        print()
    else:
        print("*"," "*3,"*")

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

m = 1
n = 1
for i in range(1,10):   
    for j in range(1,11):   
        if j<=m or (11-m)<=j:
            print("*",end="")
        else:
            print(end=" ")
    m=m+n
    if m==5:
        n=-1
    print()

"""
