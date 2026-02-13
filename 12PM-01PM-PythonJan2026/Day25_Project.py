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
    print("\n\tHERE IS YOUR ALL CUSTOMERS")
    input("\tPRESS ENTER TO CONTINUE...")

# A METHOD TO DELETE A CUSTOMER
def deleteCustomer():
    file1 = open('customer.bin','rb')
    file2 = open('temp.bin','ab')
    flag = 0
    cid = input("\n\tEnter Customer ID To Delete : ")
    try:
        while True:
            data = pickle.load(file1)
            if data==cid:
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        pass
    file1.close()
    file2.close()
    os.remove('customer.bin')
    os.rename('temp.bin','customer.bin')
    if flag ==1:
        print("\n\tCUSTOMER DELETED SUCCESSFULLY!")
    else:
        print("\n\tCUSTOMER NOT FOUND!")
    input("\tPRESS ENTER TO CONTINUE...")

# A METHOD TO ADD PRODUCT
def addProduct():
    file = open("product.bin",'ab')
    pid = input("\n\tEnter New Product ID : ")
    pname = input("\tEnter Product Name : ")
    price = input("\tEnter New Product Price : ")
    pdesc = input("\tAbout The Product : ")
    pickle.dump(pid,file)
    pickle.dump(pname,file)
    pickle.dump(price,file)
    pickle.dump(pdesc,file)
    print("\n\tProduct Added Successfully!")
    file.close()
    input("\tPRESS ENTER TO CONTINUE...")


# A METHOD TO VIEW ALL PRODUCTS
def viewProduct():
    file = open('product.bin','rb')
    try:
        print("PID\tPNAME\tPRICE\tDESCRIPTION")
        while True:
            for i in range(4):
                data = pickle.load(file)
                print(data,end="\t")
            print()
    except:
        pass
    file.close()
    print("\n\tHERE IS YOUR ALL PRODUCTS")
    input("\tPRESS ENTER TO CONTINUE...")


# A METHOD TO UPDATE PRICE OF A PRODUCT
def updateProduct():
    file1 = open('product.bin','rb')
    file2 = open('temp.bin','ab')
    flag = 0
    pid = input("\n\tEnter Product ID To Update Price : ")
    try:
        while True:
            data = pickle.load(file1)
            if pid==data:
                pickle.dump(data,file2)
                name = pickle.load(file1)
                print("\n\tName :",name)
                pickle.dump(name,file2)
                print("\tPrice :",pickle.load(file1))
                price = input("\n\tEnter New Price : ")
                pickle.dump(price,file2)
                pickle.dump(pickle.load(file1),file2)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        pass
    file1.close()
    file2.close()
    os.remove('product.bin')
    os.rename('temp.bin','product.bin')
    if flag == 1:
        print("\n\tPrice Updated Successfully!")
    else:
        print("\n\tPRODUCT NOT FOUND!")
    input("\tPRESS ENTER TO CONTINUE...")


# A METHOD TO GET CUSTOMER DETAIL
def getCustomer(cid):
    cus = []
    file = open('customer.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data == cid:
                cus.append(data)
                for i in range(3):
                    cus.append(pickle.load(file))
    except:
        pass
    file.close()
    return cus


# A METHOD TO GET PRODUCT DETAIL
def getProduct(pid):
    pro = []
    file = open('product.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data == pid:
                pro.append(data)
                for i in range(3):
                    pro.append(pickle.load(file))
    except:
        pass
    file.close()
    return pro


# A METHOD TO PLACE AN ORDER
def placeOrder():
    cid = input("\n\tEnter Customer ID : ")
    cus = getCustomer(cid)
    if len(cus)!=0:
        print("\n\tCustomer Name :",cus[1])
        print("\tCustomer Address :",cus[2])
        pid = input("\n\tEnter Product ID : ")
        pro = getProduct(pid)
        if len(pro)!=0:
            print("\n\tProduct Name :",pro[1])
            print("\tProduct Price :",pro[2])
            print("\tProduct Description :",pro[3])
            qty = input("\n\tEnter Quantity : ")
            print("\n\tTotal Bill :",float(qty)*float(pro[2]))
            
        else:
            print("\n\tPRODUCT NOT FOUND!")
    else:
        print("\n\tCUSTOMER NOT FOUND!")
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
    elif ch==2:
        viewCustomer()
    elif ch==3:
        deleteCustomer()
    elif ch==4:
        addProduct()
    elif ch==5:
        viewProduct()
    elif ch==6:
        updateProduct()
    elif ch==7:
        placeOrder()
