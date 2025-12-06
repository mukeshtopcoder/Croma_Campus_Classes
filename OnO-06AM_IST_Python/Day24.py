"""
STUDENT MANAGEMENT SYSTEM
student (sid,sname,sadd,cid)
Course (cid,cname,cfee,cdesc)

1. Add Student
2. View All Student
3. Remove A Student
4. Update Student Infomation
5. Add Course
6. View All Courses
7. Remove A Course
0. Exit
"""

# Importing Required Libaries
import mysql.connector

# Creating Connection with MySQL Server
conn = mysql.connector.connect(
host='127.0.0.1',
user='root',
password='553655',
database='school'
    )

# Creating Cursor For Query Execution
cur = conn.cursor()

# A Method to Add A Student
def addStudent():
    sname = input("\n\tEnter Student Name : ")
    sadd = input("\tEnter Student Address : ")
    cid = input("\tEnter Student Course ID : ")
    data = (sname,sadd,cid)
    sql = "call addStudent(%s,%s,%s)"
    try:
        cur.execute(sql,data)
        conn.commit()
        if cur.rowcount>0:
            print("\n\tStudent Addedd Successfully")
        else:
            print("\n\tFailed To Add Student")
    except Exception as e:
        print("\n\tFailed To Add Student")
        print("\tError :",e)
    input("\n\tPress Enter To Continue...")


# A Method to Add A Course
def addCourse():
    cname = input("\n\tEnter Course Name : ")
    cfee = input("\tEnter Course Fee : ")
    cdesc = input("\tEnter Course Content : ")
    data = (cname,cfee,cdesc)
    sql = "call addCourse(%s,%s,%s)"
    try:
        cur.execute(sql,data)
        conn.commit()
        if cur.rowcount>0:
            print("\n\tCourse Addedd Successfully")
        else:
            print("\n\tFailed To Add Course")
    except Exception as e:
        print("\n\tFailed To Add Course")
        print("\tError :",e)
    input("\n\tPress Enter To Continue...")



# DASHBOARD
print("\n\tSTUDENT MANAGEMENT SYSTEM")
while True:
    print("""
    \n\t1. Add Student
    \t2. View All Student
    \t3. Remove A Student
    \t4. Update Student Infomation
    \t5. Add Course
    \t6. View All Courses
    \t7. Remove A Course
    \t0. Exit
    """)
    ch = int(input("\n\tEnter Your Choice : "))
    if ch==0:
        print("\n\t\tTHANK YOU!")
        break
    elif ch==1:
        addStudent()
    elif ch==5:
        addCourse()
