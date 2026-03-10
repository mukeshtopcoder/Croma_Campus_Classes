"""
For connecting with MySQL Server
pip install mysql-connector
pip install mysql-connector-python


import mysql.connector
conn = mysql.connector.connect(
host='127.0.0.1',
port='3306',
user='root',
password='553655'
    )
print(conn)
cur = conn.cursor()
print(cur)


For Connecting with SQL Server
pip install pyodbc
pip install sqlalchemy


import pyodbc
conn = pyodbc.connect(
'DRIVER={ODBC Driver 17 for SQL Server};'
'SERVER=localhost;'
'DATABASE=testdb;'
'UID=root;'  # optional
'PWD=password_here'    # optional
    )
print(conn)
cur = conn.cursor()
print(cur)


"""

import mysql.connector
conn = mysql.connector.connect(
host='127.0.0.1',
port='3306',
user='root',
password='553655',
database='amazon'
    )
cur = conn.cursor()

query = "show tables"
cur.execute(query)
print( cur.fetchall() )
query = "select * from employee"
cur.execute(query)
for emp in cur.fetchall():
    print(emp[0],'\t',emp[1],'\t',emp[2])




