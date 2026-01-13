"""
while loop
Syntax:-

initilization
while condition:
    statements
    inc/dec

Example:-

a = 1
while a<5:
    print("Hello")
    a = a+1

a = 1
while a<=5:
    print("Hello")
    a = a+1


a = 1
while a<=5:
    print(a)
    a = a+1


a = 1
while a<=10:
    print(a)
    a = a+1


# WAP to print table of a number

num = int(input("Enter A Number : "))
a = 1
while a<=10:
    print(a*num)
    a = a+1


# WAP to print all factors of a number

num = int(input("Enter A Number : "))
a = 1
while a<=num:
    if num%a==0:
        print(a)
    a = a+1

# break , continue , pass

a = 1
while a<=5:
    print(a)
    if a==3:
        break
    a = a+1

# continue
a = 1
while a<=5:
    print(a)
    if a==3:
        continue
    a = a+1

#  pass

a = 1
while a<=5:
    print(a)
    if a==3:
        pass
    a = a+1

# WAP to add all digits of a number
# 123  =>  1+2+3  => 6
# 752  =>  7+5+2  => 14

num = int(input("Enter A Number : "))
add = 0
while num>0:
    rem = num%10
    add = add+rem  
    num = num//10
print("Addition of Digits :",add)


# WAP to reverse a number.
# num => 123   --->   321  (reverse)

num = int(input("Enter A Number : ")) 
add = 0
while num>0:
    rem = num%10   
    add = add*10+rem  
    num = num//10
print("Reverse :",add)


# WAP to check a number is palindrome
# 123 => reverse 321 (Not Palindrome)
# 121 => reverse 121 (Palindrome)

num = int(input("Enter A Number : "))
copy = num
add = 0
while num>0:
    rem = num%10   
    add = add*10+rem  
    num = num//10 
print("Reverse :",add)
if copy==add:
    print("Palindrome")
else:
    print("Not Palindrome")


"""
