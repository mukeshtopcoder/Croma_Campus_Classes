"""
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


    *
   **
  ***
 ****
*****

for i in range(1,6):
    print(" "*(5-i)+"*"*i)


    *
   * *
  * * *
 * * * *
* * * * *

for i in range(1,6):
    print(" "*(5-i)+"* "*i)

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

A
BB
CCC
DDDD
EEEEE
# A => ASCII 65

for i in range(1,6):
    print( chr(i+64)*i )

A
AB
ABC
ABCD
ABCDE

st = ""
for i in range(1,6):
    st = st+chr(i+64)  
    print( st )

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

st = "0"
for i in range(10,0,-1):
    if i!=10:
        st = str(i) + st + str(i) 
    print(st)
  
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

st = "0"
for i in range(10,0,-1):
    if i!=10:
        st = str(i) + st + str(i)
    print(" "*(i-1),end="")
    print(st)

"""
