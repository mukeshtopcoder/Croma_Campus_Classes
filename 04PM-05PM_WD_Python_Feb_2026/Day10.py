"""
PATTERN
*****
*****
*****
*****
*****

print("*****\n"*5)

*
**
***
****
*****

for i in range(1,6):
    print("*"*i)

1
22
333
4444
55555

for i in range(1,6):
    print(str(i)*i)

1
12
123
1234
12345

st = ""
for i in range(1,6):
    st = st+str(i)
    print(st)

    *
   **
  ***
 ****
*****

for i in range(1,6):
    print(" "*(5-i),"*"*i)

    *
   * *
  * * *
 * * * *
* * * * *

for i in range(1,6):
    print(" "*(5-i)+"* "*i)


A
AB
ABC
ABCD
ABCDE

ASCII Values
A => 65,B>66,C>67--Z>90 , a=> 97

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()


A
BB
CCC
DDDD
EEEEE

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()


A
BC
DEF
GHIJ
KLMNO

k = 65
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(k),end="")
        k=k+1
    print()


A
AB
ABC
ABCD
ABCDE


st = ""
for i in range(65,70):
    st = st+chr(i)
    print(st)

A
BB
CCC
DDDD
EEEEE

for i in range(65,70):
    print(chr(i)*(i-64))


12344321
123**321
12****21
1******1

for i in range(4,0,-1):
    for j in range(1,5):
        if i>=j:
            print(j,end="")
        else:
            print("*",end="")
    for j in range(4,0,-1):
        if i>=j:
            print(j,end="")
        else:
            print("*",end="")
    print()

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

"""
st = "0"
for i in range(10,0,-1):
    if i!=10:
        st = str(i) + st + str(i)
    print(st)
