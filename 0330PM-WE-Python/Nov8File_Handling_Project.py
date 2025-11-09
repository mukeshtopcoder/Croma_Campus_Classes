"""
# IDLE:- Integrated Development Learning Environment 

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

# A METHOD TO GET INFORMATION ABOUT CUSTOMER
def getCustomer(cid):
    file = open('customer.bin','rb')
    li = []
    try:
        while True:
            data = pickle.load(file)
            if data==cid:
                li.append(data)
                for i in range(3):
                    li.append(pickle.load(file))
    except:
        pass
    file.close()
    return li
    
# A METHOD TO GET INFORMATION ABOUT PRODUCT
def getProduct(pid):
    file = open('product.bin','rb')
    li = []
    try:
        while True:
            data = pickle.load(file)
            if data==pid:
                li.append(data)
                for i in range(2):
                    li.append(pickle.load(file))
    except:
        pass
    file.close()
    return li

# A METHOD TO PLACE AN ORDER
def placeOrder():
    cid = input("\n\t  Enter Customer ID : ")
    cus = getCustomer(cid)
    if len(cus)>0:
        print("\t  Customer Name :",cus[1])
        print("\t  Customer Address :",cus[2])
        pid = input("\n\t  Enter Product ID : ")
        pro = getProduct(pid)
        if len(pro)>0:
            print("\t  Product Name :",pro[1])
            print("\t  Product Price :",pro[2])
            qty = input("\t  Enter Quantity : ")
            file = open('orders.bin','ab')
            pickle.dump(cid,file)
            pickle.dump(pid,file)
            pickle.dump(qty,file)
            print("\n\t  Order Placed Successfully!")
            print("\n\t  Total Amount :",int(pro[2])*int(qty),"INR")
            file.close()
        else:
            print("\n\t  Product Not Available!")
    else:
        print("\n\t  Customer Not Available!")
    input("\n\t  Press Enter To Continue...")

# A METHOD TO VIEW ALL ORDERS INFORMATION
def viewAllOrders():
    file = open('orders.bin','rb')
    try:
        print("\n\t  OID \t CID \t PID \t QTY")
        i = 1
        while True:
            print("\t  ",i,"\t",pickle.load(file),"\t",pickle.load(file),"\t",pickle.load(file))
            i+=1
    except:
        pass
    file.close()
    input("\n\t  Press Enter To Continue...")

# A METHOD TO VIEW ALL CUSTOMER BY ID
def viewCustomer():
    cid = input("\n\t  Enter Customer ID : ")
    cus = getCustomer(cid)
    if len(cus)>0:
        print("\t  Customer Name :",cus[1])
        print("\t  Customer Address :",cus[2])
        print("\t  Customer Mobile :",cus[3])
        file = open('orders.bin','rb')
        order = []
        try:
            while True:
                li = []
                data = pickle.load(file)
                if data == cid:
                    li.append(data)
                    for i in range(2):
                        li.append(pickle.load(file))
                    order.append(li)
        except:
            print("\n\t  Orders Information!")
            if len(order)>0:
                i = 1
                for x in order:
                    print("Order No",i,":-")
                    pro = getProduct(x[1])
                    print("\t  Product Name :",pro[1])
                    print("\t  Product Price :",pro[2])
                    print("\t  Product Quantity :",x[2])
                    print("\t  Total Amount :",int(pro[2])*int(x[2]))
                    print('\t  =======================')
                    i+=1
            else:
                print("\n\t  No Orders Yet!")
        file.close()
    else:
        print("\n\t  Customer Not Available!")
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
        viewCustomer()
    elif ch==4:
        addProduct()
    elif ch==5:
        viewAllProduct()
    elif ch==6:
        deleteProduct()
    elif ch==7:
        placeOrder()
    elif ch==8:
        viewAllOrders()
    else:
        input("\n\t  Wrong Entered\n\t  Try Again!")
