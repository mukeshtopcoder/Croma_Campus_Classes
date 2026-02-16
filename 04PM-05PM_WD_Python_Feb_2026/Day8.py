"""
for loop

# break continue pass

for i in range(1,11):
    if i==5:
        break
    print(i)


for i in range(1,11):
    if i==5:
        continue
    print(i)


for i in range(1,11):
    if i==5:
        pass
    print(i)




#  else

for i in range(1,6):
    print(i)
else:
    print(0)


for i in range(1,6):
    if i==3:
        break
    print(i)
else:
    print(0)


for i in range(1,6):
    if i==3:
        continue
    print(i)
else:
    print(0)



for i in range(1,6):
    if i==3:
        pass 
    print(i)
else:
    print(0)


for i in range(1,6):
    print(i)
    if i==5:
        break
else:
    print(0)


Q51. Calculate INCOME TAX

sal = float( input("Enter Salary : ") )
if sal<500000:
    print("No Tax Liablity")
elif sal<700000:
    print("Tax :",sal*0.05)
elif sal<1000000:
    print("Tax :",sal*0.10)
else:
    print("Tax :",sal*0.15)


Q52. ATM withdrawl Program

balance = 32000
w = float(input("Enter Amount Withdrawl : "))
if w<=balance:
    print("Collect The Money")
    balance=balance-w
    print("Current Balance :",balance)
else:
    print("Insufficient Balance")
    print("Current Balance :",balance)


# WAP to find sum of all natural numbers.
    1 to N

n = int(input("Enter Range From 1 to : "))
add = 0
for i in range(1,n+1):
    add=add+i

print(add)


n = int(input("Enter Range From 1 to : "))

print( "Total :", n*(n+1)/2 )



Find Factorial
    !5  =>  5*4*3*2*1  => 120

add = 1
num = int(input("Enter A Number : "))
for i in range(1,num+1):
    add = add*i

print("factorial :",add)


"""

