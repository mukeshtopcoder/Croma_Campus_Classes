"""
CURD :- Create , Update , Read , Delete

Store Management System
customer (cid,cname,cadd,cmobile)
product (pid , pname , price)
orders (oid , cid , pid , qty)


1. Add Customer
2. Show All Customers
3. View A Customer By CID
4. Add Product
5. View All Products
6. Update A Product
7. Place An Order
8. View All Orders
0. Exit

"""

# Required Libraries
import pickle
import os

# A Method to Add a customer
def addCustomer():
    file = open('customer.bin','ab')
    cid = input("\n\tEnter New Customer ID : ")
    cname = input("\tEnter New Customer Name : ")
    cadd = input("\tEnter New Customer Address : ")
    cmobile = input("\tEnter New Customer Mobile : ")
    pickle.dump(cid,file)
    pickle.dump(cname,file)
    pickle.dump(cadd,file)
    pickle.dump(cmobile,file)
    print("\n\t\tCustomer Added Successfully!")
    file.close()
    input("\n\t\tPress Enter To Continue...")

# A Method to view All Customers
def showAllCustomer():
    file = open('customer.bin','rb')
    try:
        print('\n\t CID\t C_Name\t C_Add\t C_Mobile\n')
        while True:
            for i in range(4):
                print('\t',pickle.load(file),end='')
            print()
    except:
        print("\n\tHere are all the customers")
    file.close()
    input("\n\t\tPress Enter To Continue...")

# A Method to Add Products
def addProduct():
    file = open('product.bin','ab')
    pid = input("\n\tEnter New Product ID : ")
    pname = input("\tEnter New Product Name : ")
    price = input("\tEnter New Product Price : ")
    pickle.dump(pid,file)
    pickle.dump(pname,file)
    pickle.dump(price,file)
    print("\n\t\tProduct Added Successfully!")
    file.close()
    input("\n\t\tPress Enter To Continue...")

# A Method To View All Products
def viewAllProducts():
    file = open('product.bin','rb')
    try:
        print('\n\t PID\t P_Name\t\t P_Price\n')
        while True:
            for i in range(3):
                print('\t',pickle.load(file),end='')
            print()
    except:
        print("\n\tHere are all the products")
    file.close()
    input("\n\t\tPress Enter To Continue...")
# DASHBOARD
while True:
    print("\n\t\tStore Management System")
    print("""
    \t\t1. Add Customer
    \t\t2. Show All Customers
    \t\t3. View A Customer By CID
    \t\t4. Add Product
    \t\t5. View All Products
    \t\t6. Update A Product
    \t\t7. Place An Order
    \t\t8. View All Orders
    \t\t0. Exit
    """)
    ch = int(input("\t\tEnter Your Choice : "))
    if ch==0:
        print("\n\t\tBye-Bye Admin!")
        break
    elif ch==1:
        addCustomer()
    elif ch==2:
        showAllCustomer()
    elif ch==3:
        pass
    elif ch==4:
        addProduct()
    elif ch==5:
        viewAllProducts()
