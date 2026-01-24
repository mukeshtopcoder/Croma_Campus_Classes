"""

Exception Handling
a = 10
b = 0
try:
    print(a/b)
except:
    print("Divide not possible")



File Handling
TEXT file and BINARY file

TEXT file
file_handler = open( 'file_name.extension' , 'mode' )
mode:-  r , w , a , r+ , w+ , a+
Example:-
# WAP to write data in a file
file = open('student.txt','w')
file.write("Yogesh Saini")
file.close()

file = open('student.txt','a')
file.write("\nSimran Khurana")
file.close()

# WAP to read data from a file
file = open('student.txt','r')
print( file.read() )
file.close()

BINARY FILE
import pickle
pickle.load   =>   read file
pickle.dump   =>   write file

file_handler = open( 'file_name.extension' , 'mode' )
mode:-  rb , wb , ab , rb+ , wb+ , ab+
Extension:- .dat , .bin etc

Example:-
# WAP to write data in a binary file

import pickle
file = open('employee.bin','wb')
pickle.dump("Rahul Singh",file)
file.close()


import pickle
file = open('employee.bin','ab')
pickle.dump("Simran Khurana",file)
file.close()


# WAP to read data from a file
import pickle
file = open( 'employee.bin','rb' )

print( pickle.load(file) )

file.close()



import pickle
file = open( 'employee.bin','rb' )
for i in range(1,5):
    data = pickle.load(file)
    print( data )

file.close()

import pickle
file = open( 'employee.bin','rb' )
try:
    while True:
        data = pickle.load(file)
        print( data )
except:
    print("Read Complete")
file.close()


# WAP to insert employees details in a binary file
employee_details(eid,ename,edesg,esal)

import pickle
file = open("emp_detail.bin",'ab')
eid = input("Enter Employee ID : ")
ename = input("Enter Employee Name : ")
edesg = input("Enter Employee Designation : ")
esal = input("Enter Employee Salary : ")
pickle.dump(eid,file)
pickle.dump(ename,file)
pickle.dump(edesg,file)
pickle.dump(esal,file)
print("Detail Inserted Successfully!")
file.close()


# WAP to read employee's detail from a file
employee(eid,ename,edesg,esal)

import pickle
file = open('emp_detail.bin','rb')
try:
    while True:
        print("Employee ID :",pickle.load(file))
        print("Employee Name :",pickle.load(file))
        print("Employee Designation :",pickle.load(file))
        print("Employee Salary :",pickle.load(file))
        print("*********************")
except:
    print("File Read Complete!")
file.close()


"""




