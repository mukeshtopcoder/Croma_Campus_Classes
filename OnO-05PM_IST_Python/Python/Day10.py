"""
# WAP to add digits of a number
HINT:   234  => 2+3+4   => 9\

num = int(input("Enter A Number : "))
add  = 0
while num>0:
    rem = num%10
    add = add + rem  
    num = num//10   

print(add)


# WAP to reverse a Number
Number 123  =>  321 (Reverse)

num = int(input("Enter A Number : "))
add  = 0
while num>0:
    rem = num%10
    add = add*10 + rem   
    num = num//10

print('Reverse Number :',add)


# Factorial of a number
HINT :-    5 => 5*4*3*2*1  => 120
"""

num = int(input("Enter A Number : "))
add = 1
a = 1
while a<=num:
    add = add*a
    a = a+1
    
print(add)


