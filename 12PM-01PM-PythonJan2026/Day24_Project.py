"""
Store Management System

customer (cid , cname , cadd , cmob)
product  (pid , pname , price , pdesc)
orders   ( cid , pid , qty )


1- Add Customer
2- View All Customers
3- Delete Customer
4- Add Product
5- View All Products
6- Update Product
7- Place An Order
8- View All Orders
9- View Orders of A Customer

"""
# REQUIRED LIBRARIES
import pickle
import os

# A METHOD TO ADD A CUSTOMER
def addCustomer():
    file = open('customer.bin','ab')
    cid = input("\n\tEnter New Customer ID : ")
    cname = input("\tEnter Customer Name : ")
    cadd = input("\tEnter Customer Address : ")
    cmob = input("\tEnter Customer Mobile : ")
    pickle.dump(cid,file)
    pickle.dump(cname,file)
    pickle.dump(cadd,file)
    pickle.dump(cmob,file)
    file.close()
    print("\n\tCUSTOMER ADDED SUCCESSFULLY!")
    input("\tPRESS ENTER TO CONTINUE...")

# A METHOD TO VIEW ALL CUSTOMERS
def viewCustomer():
    file = open('customer.bin','rb')
    try:
        print("CID\tCNAME\tCADD\tCMOB")
        while True:
            for i in range(4):
                data = pickle.load(file)
                print(data,end="\t")
            print()
    except:
        pass
    file.close()
    print("\n\tHERE IS YOUR ALL CUSTMERS")
    input("\tPRESS ENTER TO CONTINUE...")

# A METHOD TO DELETE A CUSTOMER
def deleteCustomer():
    file1 = open('customer.bin','rb')
    file2 = open('temp.bin','ab')
    cid = input("\n\tEnter Customer ID To Delete : ")
    try:
        while True:
            data = pickle.load(file1)
            if data==cid:
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
            else:
                pickle.dump(data,file2)
    except:
        pass
    file1.close()
    file2.close()
    os.remove('customer.bin')
    os.rename('temp.bin','customer.bin')
    print("\n\tCUSTOMER DELETED SUCCESSFULLY!")
    input("\tPRESS ENTER TO CONTINUE...")

# DASHBOARD
print("\n\t  STORE MANAGEMENT SYSTEM")
while True:
    print("\t---------------------------")
    print("""    1- Add Customer
    2- View All Customers
    3- Delete Customer
    4- Add Product
    5- View All Products
    6- Update Product
    7- Place An Order
    8- View All Orders
    9- View Orders of A Customer
    0- Exit\n""")
    ch = int(input("Enter Your Choice : "))
    if ch==0:
        print("\n\t THANK YOU!")
        break
    if ch==1:
        addCustomer()
    if ch==2:
        viewCustomer()
    if ch==3:
        deleteCustomer()

