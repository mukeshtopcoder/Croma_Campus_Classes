"""
Database Connectivity

pip install mysql.connector
pip install mysql.connector.python

local_ip_address = 127.0.0.1   ,   localhost
port = 3306
user = 'root'
password = 'your_password'
database = 'database_name'


import mysql.connector
conn = mysql.connector.connect(
host = '127.0.0.1',
port = '3306',
user = 'root',
password = '553655'
    )
cur = conn.cursor()





import mysql.connector
conn = mysql.connector.connect(
host = '127.0.0.1',
port = '3306',
user = 'root',
password = '553655',
database = 'store'
    )
cur = conn.cursor()
# ====================================================
sql = ''' create table product(
pid INT primary key auto_increment,
pname VARCHAR(100) NOT NULL ,
price DECIMAL(8,2) DEFAULT 0.0
) '''
try:
    cur.execute(sql)
    print("Table Created Successfully!")
except Exception as e:
    print("Found Error :",e)


    
name = input("Enter Product Name : ")
price = input("Enter Product Price : ")
data = (name,price)
sql = 'insert into product(pname,price) value(%s,%s)'
try:
    cur.execute(sql,data)
    conn.commit()
    print("Data Inserted Successfully!")
except Exception as e:
    print("Found Error :",e)


sql = 'select * from product'
cur.execute(sql)
data = cur.fetchall()
print("PID \t PNAME \t\t PRICE\n")
for pro in data:
    print(pro[0],'\t',pro[1],'\t',pro[2])



name = input("Enter Customer Name : ")
add = input("Enter Customer Address : ")
data = (name,add)
sql = 'insert into customer(cname,cadd) value(%s,%s)'
try:
    cur.execute(sql,data)
    conn.commit()
    print("Data Inserted Successfully!")
except Exception as e:
    print("Found Error :",e)


sql = 'select * from customer'
cur.execute(sql)
data = cur.fetchall()
print("CID \t CNAME \t\t CADD\n")
for pro in data:
    print(pro[0],'\t',pro[1],'\t',pro[2])




"""
import mysql.connector
conn = mysql.connector.connect(
host = '127.0.0.1',
port = '3306',
user = 'root',
password = '553655',
database = 'store'
    )
cur = conn.cursor()
# ====================================================

# STORE MANAGEMENT SYSTEM

# A METHOD TO ADD A PRODUCT DETAIL
def addProduct():
    name = input("\n\t\tEnter Product Name : ")
    price = input("\t\tEnter Product Price : ")
    data = (name,price)
    sql = 'insert into product(pname,price) value(%s,%s)'
    try:
        cur.execute(sql,data)
        conn.commit()
        print("\n\t\tProduct Added Successfully!")
    except Exception as e:
        print("Found Error :",e)
    input("\n\t\tPress Enter To Continue...")


# A METHOD TO GET PRODUCT DETAIL
def getProduct(pid):
    sql = 'select * from product where pid='+str(pid)
    cur.execute(sql)
    data = cur.fetchall()
    if len(data)!=0:
        return data[0]
    else:
        return []

# A METHOD TO GET CUSTOMER DETAIL
def getCustomer(cid):
    sql = 'select * from customer where cid='+str(cid)
    cur.execute(sql)
    data = cur.fetchall()
    if len(data)!=0:
        return data[0]
    else:
        return []


# A METHOD TO DELETE PRODUCT
def deleteProduct():
    pid = input("\n\t\tEnter Product ID : ")
    pro = getProduct(pid)
    if len(pro)!=0:
        sql = 'delete from product where pid='+pid
        cur.execute(sql)
        conn.commit()
        print("\n\t\tProduct Deleted!")
    else:
        print("\n\t\tProduct Not Found!")
    input("\n\t\tPress Enter To Continue...")

# A METHOD TO PLACE AN ORDER
def placeAnOrder():
    cid = input("\n\t\tEnter Customer ID : ")
    cus = getCustomer(cid)
    if len(cus)!=0:
        print("\n\t\tCustomer Name :",cus[1])
        pid = input("\n\t\tEnter Product ID : ")
        pro = getProduct(pid)
        if len(pro)!=0:
            print("\n\t\tProduct Name :",pro[1])
            qty = input("\n\t\tEnter Quantity : ")
            sql = 'insert into orders(cid,pid,qty) value(%s,%s,%s)'
            cur.execute(sql,(cid,pid,qty))
            conn.commit()
            print("\n\t\tOrder Placed Successfully")
            print("\t\tTotal Amount :",int(pro[2])*int(qty))
        else:
            print("\n\t\tProduct Not Found!")
    else:
        print("\n\t\tCustomer Not Found On This ID")
    input("\n\t\tPress Enter To Continue...")

# DASHBOARD
while True:
    print("\n\t\tSTORE MANAGEMENT SYSTEM\n")
    print("\t\t1. Add Product")
    print("\t\t2. Delete Product")
    print("\t\t3. Add Customer")
    print("\t\t4. View All Products")
    print("\t\t5. View All Customers")
    print("\t\t6. Place An Order")
    print("\t\t7. View All Orders")
    print("\t\t0. Exit")
    print("\n\t\tEnter Your Choice : ",end="")
    ch = int(input())
    if ch==0:
        print("\n\t\tBye-Bye Admin!")
        break
    elif ch==1:
        addProduct()
    elif ch==2:
        deleteProduct()
    elif ch==6:
        placeAnOrder()

