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

# A Method to delete a Customer
def deleteCustomer():
    file1 = open('customer.bin','rb')
    file2 = open('temp.bin','ab')
    cid = input("\n\t\tEnter CID To Delete : ")
    flag = 0
    try:
        while True:
            data = pickle.load(file1)
            if data == cid:
                for i in range(3):
                    pickle.load(file1)
                    flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag == 1:
            print("\n\t\tCustomer Deleted Successfully!")
        else:
            print("\n\t\tCustomer Not Found!")
    file1.close()
    file2.close()
    os.remove('customer.bin')
    os.rename('temp.bin','customer.bin')
    input("\n\t\tPress Enter To Continue...")
    
# A Method to update price of a product
def updateProduct():
    file1 = open('product.bin','rb')
    file2 = open('temp.bin','ab')
    pid = input("\n\t\tEnter PID To Update Price : ")
    flag = 0
    try:
        while True:
            data = pickle.load(file1)
            if data == pid:
                pickle.dump(data,file2)
                name = pickle.load(file1)
                pickle.dump(name,file2)
                print("\t\tProduct Name : ",name)
                print("\t\tProduct Old Price : ",pickle.load(file1))
                pr = input("\n\t\tEnter New Price : ")
                pickle.dump(pr,file2)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag == 1:
            print("\n\t\tProduct Updated Successfully!")
        else:
            print("\n\t\tProduct Not Found!")
    file1.close()
    file2.close()
    os.remove('product.bin')
    os.rename('temp.bin','product.bin')
    input("\n\t\tPress Enter To Continue...")

# A Method to find a customer in the file
def getCustomer(cid):
    file = open('customer.bin','rb')
    cus = []
    try:
        while True:
            data = pickle.load(file)
            if data == cid:
                cus.append(data)
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
    except:
        pass
    file.close()
    return cus

# A Method to find a Product in the file
def getProduct(pid):
    file = open('product.bin','rb')
    pro = []
    try:
        while True:
            data = pickle.load(file)
            if data == pid:
                pro.append(data)
                pro.append(pickle.load(file))
                pro.append(pickle.load(file))
    except:
        pass
    file.close()
    return pro

# A Method to place an order
def placeAnOrder():
    file = open('order.bin','ab')
    cid = input("\n\t\tEnter Customer ID : ")
    cus = getCustomer(cid)
    if len(cus)>0:
        print("\t\tCustomer Name :",cus[1])
        print("\t\tCustomer Address :",cus[2])
        print("\t\tCustomer Mobile :",cus[3])
        pid = input("\n\t\tEnter Product ID : ")
        pro = getProduct(pid)
        if len(pro)>0:
            print("\t\tProduct Name :",pro[1])
            print("\t\tProduct Price :",pro[2])
            qty = input("\n\t\tEnter Quantity : ")
            pickle.dump(cid,file)
            pickle.dump(pid,file)
            pickle.dump(qty,file)
            print("\n\t\tOrder Placed Successfully")
            print("\t\tof Amount : ",int(pro[2])*int(qty))
        else:
            print("\n\t\tProduct Not Found!")
    else:
        print("\n\t\tCustomer Not Found!")
    file.close()
    input("\n\t\tPress Enter To Continue...")

# A Method to view Orders
def viewOrders():
    file = open('order.bin','rb')
    try:
        print("\t CID \t PID \t QTY")
        while True:
            for i in range(3):
                print("\t",pickle.load(file),end='')
            print()
    except:
        print("\n\t\tHere Are All Orders")
    file.close()
    input("\n\t\tPress Enter To Continue...")

# A Method To View A Customer information 
def viewCustomerByID():
    cid = input("\n\t\tEnter Customer ID : ")
    cus = getCustomer(cid)
    if len(cus)>0:
        print("\t\tCustomer Name :",cus[1])
        print("\t\tCustomer Address :",cus[2])
        print("\t\tCustomer Mobile :",cus[3])
        print("\n\t\tOrders")
        file = open('order.bin','rb')
        try:
            while True:
                data = pickle.load(file)
                if data==cid:
                    pro = getProduct(pickle.load(file))
                    qty = pickle.load(file)
                    print("\n\t\tProduct Name :",pro[1])
                    print("\t\tProduct Price :",pro[2])
                    print("\t\tOrdered Qty :",qty)
                    print("\t\tTotal Amount : ",int(pro[2])*int(qty))                    
        except:
            pass
        file.close()
    else:
        print("\n\t\tCustomer Not Found!")
    input("\n\t\tPress Enter To Continue...")
    
# DASHBOARD
while True:
    print("\n\t\tStore Management System")
    print("""
    \t\t1. Add Customer
    \t\t2. Show All Customers
    \t\t3. View A Customer By CID
    \t\t4. Delete A Customer
    \t\t5. Add Product
    \t\t6. View All Products
    \t\t7. Update A Product
    \t\t8. Place An Order
    \t\t9. View All Orders
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
        viewCustomerByID()
    elif ch==4:
        deleteCustomer()
    elif ch==5:
        addProduct()
    elif ch==6:
        viewAllProducts()
    elif ch==7:
        updateProduct()
    elif ch==8:
        placeAnOrder()
    elif ch==9:
        viewOrders()
