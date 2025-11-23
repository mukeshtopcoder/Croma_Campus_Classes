"""
Database Connectivity

pip install mysql.connector
pip install mysql.connector.python

create connection (connect mysql server and python)

import mysql.connector
conn = mysql.connector.connect(
host = '127.0.0.1',            # localhost
port = '3306',
user = 'root',
password = '553655'
    )
cur = conn.cursor()



sql = "show databases"
cur.execute(sql)
print(cur)
db = cur.fetchall()
for db_name in db:
    print(db_name[0])



sql = "use flipkart"
cur.execute(sql)
sql = 'select * from employee'
cur.execute(sql)
data = cur.fetchall()
for emp in data:
    print('EID :',emp[0])
    print('E_Name :',emp[1])
    print('E_Desg :',emp[2])
    print('E_Sal :',emp[3])
    print('\n-----------------')



import mysql.connector
conn = mysql.connector.connect(
host = '127.0.0.1',            # localhost
port = '3306',
user = 'root',
password = '553655',
database = 'flipkart'
    )
cur = conn.cursor()


sql = 'select * from employee'
cur.execute(sql)
data = cur.fetchall()
name = input("Enter Employee ID To Find Detail : ")
for emp in data:
    if emp[0]==int(name):
        print('EID :',emp[0])
        print('E_Name :',emp[1])
        print('E_Desg :',emp[2])
        print('E_Sal :',emp[3])
        print('\n-----------------')



ename = input("Enter Employee Name : ")
edesg = input("Enter Employee Designation : ")
esal = input("Enter Employee Salary : ")
eadd = input("Enter Employee Address : ")
eage = input("Enter Employee Age : ")
data = (ename,edesg,esal,eadd,eage)
sql = '''insert into employee(ename,edesg,esal,eadd,eage)
VALUE(%s,%s,%s,%s,%s)'''
cur.execute(sql,data)
conn.commit()
if cur.rowcount>0:
    print("Employee Added Successfully!")
else:
    print("Employee Addition Failed!")





data = (ename,edesg,esal,eadd,eage)
sql = '''insert into employee(ename,edesg,esal,eadd,eage)
VALUE(%s,%s,%s,%s,%s)'''
try:
    cur.execute(sql,data)
except Exception as e:
    print("Found Error :",e)
conn.commit()
if cur.rowcount>0:
    print("Employee Added Successfully!")
else:
    print("Employee Addition Failed!")


    
CURD:- CREATE , UPDATE , READ , DELETE (SE)
DBMS => SQL Queries
"""
import mysql.connector
conn = mysql.connector.connect(
host = '127.0.0.1',            # localhost
port = '3306',
user = 'root',
password = '553655'
    )
cur = conn.cursor()
# ======================================================

sql = '''CREATE DATABASE amazon'''
cur.execute(sql)
sql = 'USE amazon'
cur.execute(sql)
sql = '''
CREATE TABLE product(
pid INT PRIMARY KEY AUTO_INCREMENT ,
pname VARCHAR(100) NOT NULL ,
price DECIMAL(8,2) NOT NULL
)
'''
cur.execute(sql)
