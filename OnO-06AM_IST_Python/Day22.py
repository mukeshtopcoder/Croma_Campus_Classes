"""
Database Interaction
MySQL (host , port , user , password)


# pip install mysql.connector
# pip install mysql.connector.python


import mysql.connector
conn = mysql.connector.connect(
host = '127.0.0.1',           # localhost
port = '3306', 
user = 'root',
password = '553655'
    )
cur = conn.cursor()
sql = "show databases"
cur.execute(sql)
print( cur.fetchall() )

"""
