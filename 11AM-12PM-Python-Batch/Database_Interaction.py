"""
Database Interaction with Python
import mysql.connector

pip => Python Installer Package
run these two instructions in command prompt
pip install mysql.connector
pip install mysql.connector.python

import mysql.connector

conn = mysql.connector.connect(
host = '127.0.0.1',
port = '3306',
user = 'root',
password = '553655',
database = 'oracle'
    )
cur = conn.cursor()

query = '''INSERT INTO employee(ename,emobile,esal,eage)
VALUE('Mohan Singh','+919999999999',45453.45,24)'''
cur.execute(query)
conn.commit()

import mysql.connector

conn = mysql.connector.connect(
host = '127.0.0.1',
port = '3306',
user = 'root',
password = '553655',
database = 'oracle'
    )
cur = conn.cursor()
query = 'SELECT * FROM employee;'
cur.execute(query)
data = cur.fetchall()
for emp in data:
    print('Employee ID :',emp[0])
    print('Employee Name :',emp[1])
    print('Employee Mobile :',emp[2])
    print('Employee Salary :',emp[3])
    print('---------------------')


"""

    
