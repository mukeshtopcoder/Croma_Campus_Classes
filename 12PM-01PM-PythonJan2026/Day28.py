"""
STUDENT MANAGEMENT SYSTEM

student ( sid,sname,sadd,scourse,sfee )

1- Add Student
2- View All Student
3- Update Student
4- Delete A Student
0- Exit

"""
# IMPORT REQUIRED LIBRARIES
import mysql.connector

# BUILD A CONNECTION WITH MySQL
conn = mysql.connector.connect(
host='127.0.0.1',
port='3306',
user='root',
password='553655',
database='college'
    )

# BUILD A CURSOR FOR EXECUTING THE QUERIES
cur = conn.cursor()

# A METHOD TO ADD A STUDENT
def addStudent():
    sname = input("\n\tEnter Student Name : ")
    sadd = input("\tEnter Student Address : ")
    scourse = input("\tEnter Student Course : ")
    sfee = input("\tEnter Course Fee : ")
    query = '''insert into student(sname,sadd,scourse,sfee)
value(%s,%s,%s,%s)'''
    data = (sname,sadd,scourse,sfee)
    cur.execute(query,data)
    if cur.rowcount>0:
        print("\n\tStudent Added Successfully!")
    else:
        print("\n\tQuery Failed!")
    conn.commit()
    input("\n\tPress Enter To Continue...")

# A METHOD TO VIEW ALL STUDENTS
def viewStudent():
    query = 'select * from student'
    cur.execute(query)
    data = cur.fetchall()
    print("\nSID\tSNAME\tSADD\tSCOURSE\tSFEE\n")
    for sid,sname,sadd,scourse,sfee in data:
        print(f'{sid}\t{sname}\t{sadd}\t{scourse}\t{sfee}')
    input("\n\tPress Enter To Continue...")

# A METHOD TO UPDATE INFO OF A STUDENT
def updateStudent():
    sid = input("\n\tEnter Student ID : ")
    query = 'select * from student where sid='+sid
    cur.execute(query)
    data = cur.fetchone()
    if data!=None:
        print("\n\tStudent Name :",data[1])
        sadd = input("\tEnter New Address : ")
        scourse = input("\tEnter New Course : ")
        sfee = input("\tEnter New Fee : ")
        query = '''update student set sadd=%s, scourse=%s,
sfee=%s where sid=%s'''
        data = (sadd,scourse,sfee,sid)
        cur.execute(query,data)
        if cur.rowcount>0:
            print("\n\tStudent Updated Successfully!")
        else:
            print("\n\tFailed To Update!")
        conn.commit()
    else:
        print("\n\tStudent is not available")
    input("\n\tPress Enter To Continue...")

# A METHOD TO DELETE A STUDENT
def deleteStudent():
    sid = input("\n\tEnter Student ID : ")
    query = 'select * from student where sid='+sid
    cur.execute(query)
    data = cur.fetchone()
    if data!=None:
        print("\n\tStudent Name :",data[1])
        print("\tStudent Course :",data[3])
        sql = 'delete from student where sid='+sid
        cur.execute(sql)
        if cur.rowcount>0:
            print("\n\tStudent Deleted Successfully!")
        else:
            print("\n\tFailed To Delete!")
    else:
        print("\n\tStudent Not Found!")
    conn.commit()
    input("\n\tPress Enter To Continue...")
    
# DASHBOARD
while True:
    print("\n\t    STUDENT MANAGEMENT SYSTEM")
    print('''
                1- Add Student
                2- View All Student
                3- Update Student
                4- Delete A Student
                0- Exit
    ''')
    ch = int(input("\t\tEnter Your Choice : "))
    if ch==0:
        print("\n\t\tBye-Bye")
        break
    elif ch==1:
        addStudent()
    elif ch==2:
        viewStudent()
    elif ch==3:
        updateStudent()
    elif ch==4:
        deleteStudent()
    else:
        input("\n\tWrong Entered!\n\tTry Again!")

