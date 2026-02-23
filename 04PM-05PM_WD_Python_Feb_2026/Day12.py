"""
Q20. Pyramid Pattern
Print:
    *
   ***
  *****
 *******
*********

m = 5
for i in range(1,10,2):
    print(" "*m+"*"*i)
    m=m-1



Q21. Inverted Pyramid
Print:
*********
 *******
  *****
   ***
    *


m = 0
for i in range(9,0,-2):
    print(" "*m+"*"*i)
    m=m+1


    *
   ***
  *****
 *******
*********

for i in range(1,6):
    for k in range(i,5):
        print(" ",end="")
    for j in range(0,i*2-1):
        print("*",end="")
    print()



for i in range(1000):
    print("*"*i)
    if i==4:
        break


"""
