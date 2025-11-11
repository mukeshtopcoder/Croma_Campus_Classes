# Single Line Comment
"""
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
for j in range(1,10):
    for i in range(1,11):
        if i<=m or i>=(11-m):
            print("*",end="")
        else:
            print(end=" ")
    print()
    m=m+n
    if m==5:
        n=-1

LIST:-
find all prime numbers from a list

li = [24,541,73,9,87,33,13,35,47,687]

for num in li:
    count = 0
    for i in range(2,num//2+1):
        if num%i==0:
            count+=1
            break
    if count==0:
        print(num)
        
"""
