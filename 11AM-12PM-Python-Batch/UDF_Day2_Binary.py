"""
Binary Files
import pickle
dump : is use to write data into a file
load : is use to read a file

import pickle
pickle.dump('content',file)
pickle.load(file)

file_handler = open('file_name.extension' , 'mode')
extension :-    .vcd , .dat , .bin etc
mode :-    rb , ab , wb , rb+ , ab+ , wb+

file = open('employee.bin','wb')

file.close()

# WAP to write data into a binary file
import pickle
file = open('employee.bin','ab')
pickle.dump('Vikas Saini',file)
file.close()

# WAP to read data from a binary file
import pickle
file = open('employee.bin','rb')
print( pickle.load(file) )
print( pickle.load(file) )
file.close()


import pickle
file = open('employee.bin','rb')
for i in range(4):
    print( pickle.load(file) )
file.close()

import pickle
file = open('employee.bin','rb')
try:
    while True:
        data = pickle.load(file)
        print(data)
except:
    print("File Read Successfully!")
file.close()


# WAP to store employee Details in a file.
empid , empname , empadd , empsal

import pickle
file = open('employee.bin','ab')
eid = input("Enter Employee ID : ")
ename = input("Enter Employee Name : ")
eadd = input("Enter Employee Address : ")
esal = input("Enter Employee Salary : ")
pickle.dump(eid,file)
pickle.dump(ename,file)
pickle.dump(eadd,file)
pickle.dump(esal,file)
print("\nEmployee Added Successfully!")
file.close()


# WAP to read all employee's detail from a file

import pickle
file = open('employee.bin','rb')
try:
    while True:
        print("Employee ID :",pickle.load(file))
        print("Employee Name :",pickle.load(file))
        print("Employee Address :",pickle.load(file))
        print("Employee Salary :",pickle.load(file))
        print("----------------------")
except:
    print("Here is all the employee's details")
file.close()



# WAP to delete detail of an employee from a file.

import pickle
import os
file1 = open('employee.bin','rb')
file2 = open('temp.bin','wb')
eid = input("Enter Employee ID To Delete : ")
try:
    while True:
        data = pickle.load(file1)
        if data==eid:
            pickle.load(file1)
            pickle.load(file1)
            pickle.load(file1)
        else:
            pickle.dump(data,file2)
except:
    print("\nEmployee Delete Successfully! (if available)")
file1.close()
file2.close()
os.remove('employee.bin')
os.rename('temp.bin','employee.bin')

"""
