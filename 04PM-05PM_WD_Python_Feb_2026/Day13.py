"""
WHILE LOOP

a = 1
while a<=5:
    print(a)
    a = a+1


# break
a = 1
while a<=5:
    print(a)
    a = a+1
    if a==3:
        break

    

# break
a = 1
while a<=5:
    if a==3:
        break
    print(a)
    a = a+1


# break
a = 1
while a<=5:
    print(a)
    if a==3:
        break
    a = a+1



# continue
a = 1
while a<=5:
    if a==3:
        continue  # it will stuct because 'a' can not increase
    print(a)
    a = a+1



# continue
a = 1
while a<=5:
    a = a+1
    if a==3:
        continue  # it will stuct because 'a' can not increase
    print(a)
    



# continue
a = 1
while a<=5:
    a = a+1
    if a==3:
        continue  # it will stuct because 'a' can not increase
    print(a)  # 2 4 5 6



# continue
a = 1
while a<=5:
    a = a+1
    print(a)
    if a==3:
        continue


# pass
a = 1
while a<=5:
    if a==3:
        pass
    print(a)
    a = a+1


# else
a = 1
while a<=5:
    if a==3:
        pass
    print(a)
    a = a+1
else:
    print(0)


# else
a = 1
while a<=5:
    if a==3:
        break
    print(a)
    a = a+1
else:
    print(0)




a = 1
while a<=5:
    print(a)
    a=a+1
    if 0b1001%a==0:    
        break




a = 2
while a<=10:
    print(a)
    a=a+2
    if a%3==0:
        break


a = 1
while a<=5:
    print(a)
    a+=1
    a+=1


NESTED WHILE LOOP

*****
*****
*****
*****
*****
a = 1
while a<=5:
    b = 1
    while b<=5:
        print("*",end="")
        b=b+1
    print()
    a=a+1




*
**
***
****
*****


a = 1
while a<=5:
    b = 1
    while b<=a:
        print("*",end="")
        b=b+1
    print()
    a=a+1


"""




