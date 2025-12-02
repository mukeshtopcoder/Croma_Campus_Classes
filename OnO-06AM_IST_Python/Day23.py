"""
execute SQL Queries using python
"""
import mysql.connector
conn = mysql.connector.connect(
host='127.0.0.1',
port='3306',
user='root',
password='553655',
database='flipkart'
    )
cur = conn.cursor()

"""
sql = "show tables"
cur.execute(sql)
print(cur.fetchall())



sql = 'select * from employee'
cur.execute(sql)
data = cur.fetchall()
for emp in data:
    print(emp[0],'\t',emp[1],'\t',emp[2],'\t',emp[3])


name = input('Enter Employee Name : ')
desg = input('Enter Employee Designation : ')
sal = input('Enter Employee Salary : ')
add = input('Enter Employee Address : ')
age = input('Enter Employee Age : ')
sql = 'insert into employee(ename,edesg,esal,eadd,eage) value(%s,%s,%s,%s,%s)'
data = (name,desg,sal,add,age)
cur.execute(sql,data)
conn.commit()
if cur.rowcount>0:
    print("Employee Inserted!")
else:
    print("Failed To Add Employee!")



sql = "delete from employee where eid=210"
cur.execute(sql)
conn.commit()
print( cur.rowcount )


"""

