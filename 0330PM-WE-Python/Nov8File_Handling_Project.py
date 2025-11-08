"""
Inventory Management System
customers (cid,cname,cadd,cmob)
products  (pid,pname,price)
orders    (oid,cid,pid,qty)

1. Add Customer
2. View All Customers
3. View A Customer By CID
4. Add Product
5. View All Products
6. Delete A Product
7. Place An Order
8. View All Orders
0. Exit

"""
# IMPORTING REQUIRED LIBRARIES
import pickle
import os

# A METHOD TO ADD CUSTOMER
def addCustomer():
    cid = input("\n\t  Enter New Customer ID : ")
    cname = input("\t  Enter Customer Name : ")
    cadd = input("\t  Enter Customer Address : ")
    cmob = input("\t  Enter Customer Mobile : ")
    file = open("customer.bin",'ab')
    pickle.dump(cid,file)
    pickle.dump(cname,file)
    pickle.dump(cadd,file)
    pickle.dump(cmob,file)
    file.close()
    print("\n\t  Customer Added Successfully!")
    input("\n\t  Press Enter To Continue...")

# A METHOD TO VIEW ALL CUSTOMERS INFORMATION
def viewAllCustomer():
    file = open('customer.bin','rb')
    try:
        while True:
            print("\n\t  Customer ID :",pickle.load(file))
            print("\t  Customer Name :",pickle.load(file))
            print("\t  Customer Address :",pickle.load(file))
            print("\t  Customer Mobile :",pickle.load(file))
            print("\t  ----------------------------")
    except:
        pass
    file.close()
    input("\n\t  Here is all information about customer\n\t  Press Enter To Continue...")

# A METHOD TO ADD PRODUCT INTO DATABASE/FILE
def addProduct():
    pid = input("\n\t  Enter Product ID : ")
    pname = input("\t  Enter Product Name : ")
    price = input("\t  Enter Product Price : ")
    file = open('product.bin','ab')
    pickle.dump(pid,file)
    pickle.dump(pname,file)
    pickle.dump(price,file)
    file.close()
    print("\n\t  Product Added Successfully!")
    input("\n\t  Press Enter To Continue...")

# A METHOD TO VIEW ALL PRODUCT'S INFORMATION
def viewAllProduct():
    file = open('product.bin','rb')
    try:
        print("\t   PID\t   P_NAME\t   PRICE")
        while True:
            print("\t  ",pickle.load(file),end="")
            print("\t  ",pickle.load(file),end="")
            print("\t  ",pickle.load(file))
    except:
        pass
    file.close()
    input("\n\t  Here is all information about Product\n\t  Press Enter To Continue...")

# A METHOD TO DELETE A PRODUCT
def deleteProduct():
    flag = 0
    file1 = open('product.bin','rb')
    file2 = open('temp.bin','wb')
    pid = input("\n\t  Enter PID To Delete Product : ")
    try:
        while True:
            data = pickle.load(file1)
            if data==pid:
                pickle.load(file1)
                pickle.load(file1)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\n\t  Product Deleted Successfully!")
        else:
            print("\n\t  Product Not Found!")
    file1.close()
    file2.close()
    os.remove('product.bin')
    os.rename('temp.bin','product.bin')
    input("\n\t  Press Enter To Continue...")

# DASHBOARD
while True:
    print("\n\t  WELCOME TO OUR SUPER STORE")
    print("""
    \t  1. Add Customer
    \t  2. View All Customers
    \t  3. View A Customer By CID
    \t  4. Add Product
    \t  5. View All Products
    \t  6. Delete A Product
    \t  7. Place An Order
    \t  8. View All Orders
    \t  0. Exit
    """)
    print("\t  Enter Your Choice : ",end="")
    ch = int(input())
    if ch==0:
        print("\n\t  THANK YOU FOR USING OUR SOFTWARE!")
        break
    elif ch==1:
        addCustomer()
    elif ch==2:
        viewAllCustomer()
    elif ch==3:
        pass #viewCustomer()
    elif ch==4:
        addProduct()
    elif ch==5:
        viewAllProduct()
    elif ch==6:
        deleteProduct()
    
