"""
STUDENT MANAGEMENT SYSTEM FILE_HANDLING_PROJECT

student (sid,sname,sadd,scourse)

1- Add Student
2- View All Students
3- View A Student By SID
4- Delete A Student
5- Update Info Of A Student
0- Exit

"""
# IMPORTING REQUIRED LIBRARIES
import pickle

# A METHOD TO ADD A STUDENT
def addStudent():
    file = open('student.bin','ab')
    sid = input("\n\tEnter New Student ID : ")
    sname = input("\tEnter Student Name : ")
    sadd = input("\tEnter Student Address : ")
    scourse = input("\tEnter Course Name : ")
    pickle.dump(sid,file)
    pickle.dump(sname,file)
    pickle.dump(sadd,file)
    pickle.dump(scourse,file)
    file.close()
    print("\n\tStudent Added Successfully!")
    input("\tPress Enter To Continue...")

# A METHOD TO PRINT INFORMATION OF ALL STUDENTS
def viewAllStudents():
    file = open('student.bin','rb')
    try:
        print("\nSID\tSNAME\tSADD\tSCOURSE\n")
        while True:
            for i in range(4):
                data = pickle.load(file)
                print(data,end="\t")
            print()
    except:
        pass
    file.close()
    print("\n\tHere is Your All Student's Info")
    input("\tPress Enter To Continue...")

# A METHOD TO VIEW A STUDENT INFO BY SID
def viewStudent():
    sid = input("\n\tEnter Student ID : ")
    file = open('student.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==sid:
                print("\n\tStudent ID :",data)
                print("\tStudent Name :",pickle.load(file))
                print("\tStudent Address :",pickle.load(file))
                print("\tStudent Course :",pickle.load(file))
                break
    except:
        print("\n\tStudent Not Found!")
    file.close()
    print("\n\tHere The Student's Information")
    input("\tPress Enter To Continue...")

    
# DASHBOARD (MAIN MENU)
while True:
    print("\n     ***** STUDENT MANAGEMENT SYSTEM *****")
    print('''
            1- Add Student
            2- View All Students
            3- View A Student By SID
            4- Delete A Student
            5- Update Info Of A Student
            0- Exit
    ''')
    ch = int(input("\t    Enter Your Choice : "))
    if ch==0:
        print("\n\t\tBye-Bye Admin!")
        break
    elif ch==1:
        addStudent()
    elif ch==2:
        viewAllStudents()
    elif ch==3:
        viewStudent()
