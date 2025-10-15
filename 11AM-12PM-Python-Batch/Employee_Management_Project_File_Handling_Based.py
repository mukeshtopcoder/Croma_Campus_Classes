"""
Employee Management System
Entity:-  eid,ename,eadd,esal
Operations:-
1- Add New Employee
2- View All Employee
3- View Employee By ID
4- Delete An Employee
5- Update info About an Employee
6- Exit
"""

# IMPORTING REQUIRED LIBRARIES
import pickle
import os

# A Method to add a new employee
def addEmployee():
    file = open('employee.bin','ab')
    eid = input("\n\t  Enter New Employee ID : ")
    ename = input(f"\t  Enter Employee {eid} Name : ")
    eadd = input(f"\t  Enter {ename} Address : ")
    esal = input(f"\t  Enter {ename} Salary : ")
    pickle.dump(eid,file)
    pickle.dump(ename,file)
    pickle.dump(eadd,file)
    pickle.dump(esal,file)
    print("\n\t\tEmployee Added Succesfully!")
    file.close()
    input("\n\t\tPress Enter To Continue...")

# A Method to view all employee details
def viewAllEmp():
    file = open('employee.bin','rb')
    try:
        print("\n\t\t EID\tEMP_Name")
        while True:
            print("\t\t",pickle.load(file),end='')
            print("\t",pickle.load(file))   
            pickle.load(file)
            pickle.load(file)
    except:
        pass
    file.close()
    input("\n\t\tPress Enter To Continue...")

# A Method to view an Employee Detail by ID
def viewEmp():
    file = open('employee.bin','rb')
    try:
        eid = input("\n\t\tEnter Employee ID : ")
        while True:
            data = pickle.load(file)
            if data==eid:
                print("\n\t\tEmployee ID :",data)
                print("\t\tEmployee Name :",pickle.load(file))
                print("\t\tEmployee Address :",pickle.load(file))
                print("\t\tEmployee Salary :",pickle.load(file))
                break
    except:
        print("\n\t\tEmployee Not Found!")
    else:
        print("\n\t\tHere is your Employee")
    file.close()
    input("\n\t\tPress Enter To Continue...")

# A Method to delete an employee
def deleteEmp():
    file1 = open("employee.bin",'rb')
    file2 = open("temp.bin",'ab')
    flag = 0
    eid = input("\n\t   Enter Employee ID To Delete : ")
    try:
        while True:
            data = pickle.load(file1)
            if data == eid:
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag == 0:
            print("\n\t\tEmployee Not Found!")
        else:
            print("\n\t\tEmployee Deleted Successfully!")
    file1.close()
    file2.close()
    os.remove('employee.bin')
    os.rename('temp.bin','employee.bin')
    input("\n\t\tPress Enter To Continue...")

# A Method to update information about an employee
def updateEmp():
    file1 = open('employee.bin','rb')
    file2 = open('temp.bin','ab')
    flag = 0
    eid = input("\n\t   Enter EID To Update Info : ")
    try:
        while True:
            data = pickle.load(file1)
            if data == eid:
                pickle.dump(data,file2)
                name = pickle.load(file1)
                pickle.dump(name,file2)
                pickle.load(file1)
                pickle.load(file1)
                print("\t   Employee Name :",name)
                add = input("\n\t\tEnter New Address : ")
                sal = input("\t\tEnter New Salary : ")
                pickle.dump(add,file2)
                pickle.dump(sal,file2)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\n\t\tEmployee Updated Successfully!")
        else:
            print("\n\t\tEmployee Not Found!")
    file1.close()
    file2.close()
    os.remove('employee.bin')
    os.rename('temp.bin','employee.bin')
    input("\n\t\tPress Enter To Continue...")

# DASHBOARD
while True:
    print("\n\t    EMPLOYEE MANAGEMENT SYSTEM")
    print("\n\t\t1. Add New Employee")
    print("\t\t2. View All Employee")
    print("\t\t3. View An Employee By ID")
    print("\t\t4. Delete An Employee")
    print("\t\t5. Update An Employee")
    print("\t\t0. Exit")
    print("\n\t\tEnter Your Choice : ",end="")
    ch = int(input())
    if ch==0:
        print("\n\tThank you for using our software!")
        break
    elif ch==1:
        addEmployee()
    elif ch==2:
        viewAllEmp()
    elif ch==3:
        viewEmp()
    elif ch==4:
        deleteEmp()
    elif ch==5:
        updateEmp()
    else:
        input("\n\t\tWrong Entered!\n\t\tTry Again!")
