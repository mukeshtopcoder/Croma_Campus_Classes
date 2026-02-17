"""
Database Interaction

pip install mysql-connector
pip install mysql-connector-python

"""
# Building a cursor and a connection with MySQL Server
import mysql.connector
conn = mysql.connector.connect(
    host='127.0.0.1',     # localhost
    port='3306',
    user='root',
    password='553655',
    database='college'
    )
cur = conn.cursor()


"""
# CRAETE A DATABASE IN MYSQL
sql = "CREATE DATABASE college"
cur.execute(sql)


# CREATE A TABLE IN A DATABASE

query = 'USE college'
cur.execute(query)
sql = '''CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT ,
sname VARCHAR(100) NOT NULL ,
sadd VARCHAR(100) NOT NULL
)'''
cur.execute(sql)


# INSERT A DATA INTO A TABLE

que = "USE college"
cur.execute(que)
query = '''
INSERT INTO student VALUE(101,'Mohit','Noida');
'''
cur.execute(query)
conn.commit()



# AFTER SET THE DEFAULT DATABASE NAME IN CONNECTION

query = '''
INSERT INTO student VALUE(102,'Rohan','Delhi');
'''
cur.execute(query)
conn.commit()


sql = "SELECT * FROM student"
cur.execute(sql)
data = cur.fetchall()
for stu in data:
    print(stu)



sql = "SELECT * FROM student"
cur.execute(sql)
data = cur.fetchall()
for sid,sname,sadd in data:
    print(sname,sadd)



# UPDATE A DATA IN A TABLE
sql = "UPDATE student SET sadd='GZB' WHERE sid=102"
cur.execute(sql)
conn.commit()


# DELETE DATA FROM A TABLE
sql = "DELETE FROM student WHERE sid=101"
cur.execute(sql)
conn.commit()


sql = "DELETE FROM student WHERE sid=101"
cur.execute(sql)
conn.commit()

sql = "SELECT * FROM student"
cur.execute(sql)
data = cur.fetchall()
for stu in data:
    print(stu)



# FIND GCD using lamdba
import math
gcd = lambda a,b : math.gcd(a,b)
print( gcd(12,18) )


# FIND GCD using lamdba

gcd = lambda a,b : a if b==0 else gcd(b,a%b)
print( gcd(12,18) )


# FIND GCD using lamdba
def gcd (a,b):
    gcd = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            gcd = i
    return gcd


print( gcd(12,18) )



"""

# -----------------------------------------------------

s = {1,2,3,4,6,8,9,10}  # 1 to N

for i in range(1,max(s)+1):
    if i not in s:
        print(i)

