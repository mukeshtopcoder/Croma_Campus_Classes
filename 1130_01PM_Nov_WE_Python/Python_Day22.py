"""
Employee Management System
EMPLOYEE ( eid,ename,edesg,esal,eadd )

1- Add An Employee
2- View All Employees
3- View An Employee By EID
4- Delete An Employee
5- Update An Employee
0- EXIT

"""
# IMPORTING REQUIRED LIBRARIES
import pickle
import os

# A METHOD TO ADD AN EMPLOYEE
def addEmployee():
    file = open("employee.bin",'ab')
    eid = input("\n\t   Enter Employee ID : ")
    ename = input("\t   Enter Employee Name : ")
    edesg = input("\t   Enter Employee Designation : ")
    esal = input("\t   Enter Employee Salary : ")
    eadd = input("\t   Enter Employee Address : ")
    pickle.dump(eid,file)
    pickle.dump(ename,file)
    pickle.dump(edesg,file)
    pickle.dump(esal,file)
    pickle.dump(eadd,file)
    file.close()
    print("\n\t   Employee Added Successfully!")
    input("\t   Press Enter To Continue...")

# A METHOD TO VIEW ALL EMPLOYEES DETAILS
def viewAllEmployee():
    file = open('employee.bin','rb')
    try:
        i = 0
        while True:
            i+=1
            data = pickle.load(file)
            print(data,end="\t")
            if i%5==0:
                print()
    except:
        print("\n\t   Data Read Successfully!")
    file.close()
    input("\t   Press Enter To Continue...")

# A METHOD TO VIEW AN EMPLOYEE BY HIS/HER EID
def viewEmployeeByID():
    file = open('employee.bin','rb')
    eid = input("\n\t   Enter Employee ID : ")
    flag = 0
    try:
        while True:
            data = pickle.load(file)
            if data==eid:
                print("\t   Employee ID :",data)
                print("\t   Employee Name :",pickle.load(file))
                print("\t   Employee Designation :",pickle.load(file))
                print("\t   Employee Salary :",pickle.load(file))
                print("\t   Employee Address :",pickle.load(file))
                flag = 1
    except:
        if flag==1:
            print("\n\n\t   Here is your Employee")
        else:
            print("\n\n\t   Employee Not Found On This ID")
    input("\t   Press Enter To Continue...")

# A METHOD TO DELETE AN EMPLOYEE
def deleteEmployee():
    eid = input("\n\t   Enter Employee ID : ")
    file1 = open('employee.bin','rb')
    file2 = open('temp.bin','ab')
    flag = 0
    try:
        while True:
            data = pickle.load(file1)
            if eid==data:
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\n\t   Employee Deleted Successfully!")
        else:
            print("\n\t   Employee Not Found On This ID!")
    file1.close()
    file2.close()
    os.remove('employee.bin')
    os.rename('temp.bin','employee.bin')
    input("\t   Press Enter To Continue...")

# A METHOD TO UPDATE THE INFORMATION OF AN EMPLOYEE
def updateEmployee():
    eid = input("\n\t   Enter Employee ID : ")
    file1 = open('employee.bin','rb')
    file2 = open('temp.bin','ab')
    flag = 0
    try:
        while True:
            data = pickle.load(file1)
            if eid==data:
                pickle.dump(data,file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.load(file1)
                pickle.load(file1)
                sal = input("\n\t   Enter New Salary : ")
                add = input("\t   Enter New Address : ")
                pickle.dump(sal,file2)
                pickle.dump(add,file2)
                flag = 1
            else:
                pickle.dump(data.file2)
    except:
        if flag==1:
            print("\n\t   Employee Updated Successfully!")
        else:
            print("\n\t   Employee Not Found On This ID!")
    file1.close()
    file2.close()
    os.remove('employee.bin')
    os.rename('temp.bin','employee.bin')
    input("\t   Press Enter To Continue...")
 
# DASHBOARD
while True:
    print("\n\t   EMPLOYEE MANAGEMENT SYSTEM")
    print('''
    \t   1- Add An Employee
    \t   2- View All Employees
    \t   3- View An Employee By EID
    \t   4- Delete An Employee
    \t   5- Update An Employee
    \t   0- EXIT''')
    ch = int(input("\n\t   Enter Your Choice : "))
    if ch==0:
        print("\n\t   Bye-Bye Admin!")
        break
    elif ch==1:
        addEmployee()
    elif ch==2:
        viewAllEmployee()
    elif ch==3:
        viewEmployeeByID()
    elif ch==4:
        deleteEmployee()
    elif ch==5:
        updateEmployee()
    else:
        input("\n\t   Wrong Entered!")
