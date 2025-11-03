"""
File Handling
File (Two Types)
1- Text File
2- Binary File
=> TEXT FILE
Syntax:-
file_handler = open('file_name.extension' , 'mode')
mode:-  r,w,a,r+,w+,a+
Example:-
file = open('student.txt','w')
file.close()

# WAP to write data in a text file.

file = open('student.txt','w')
filee("Rahul Kumar\n")
file.write("Suman Singh\n")
file.write("Siya Kumari")
file.close()


# IN APPEND MODE
file = open('student.txt','a')
file.write("Rahul Kumar\n")
file.write("Diya Singh\n")
file.write("Ravi Kumar")
file.close()

# WAP TO READ A FILE
file = open('student.txt','r')
data = file.read()
print(data)
file.close()


# read() , read(value) , readline , readlines
file = open('student.txt','r')
data = file.read(30)
print(data)
file.close()

file = open('student.txt','r')
data = file.readline()
print(data)
data = file.readline()
print(data)
file.close()

file = open('student.txt','r')
data = file.readlines()
for x in data:
    print(x)
file.close()

# tell , seek
file = open('student.txt','r')
print(file.tell())
data = file.read(10)
print(data)
print(file.tell())
file.close()

file = open('student.txt','r')
print(file.tell())
data = file.read(10)
print(data)
print(file.tell())
file.seek(20)
print(file.tell())
print(file.read(5))
print(file.tell())
file.close()


file = open('student.txt','w+')
file.write('Raman Singh')
file.seek(0)
print( file.read() )
print( file.tell() )
file.close()


# BINARY FILE
import pickle
load  (read)/dump  (write)

file_handler = open('file_name.extension','mode')
mode :=   rb,wb,ab,rb+,wb+,ab+
Example:-
file = open('employee.bin','wb')
file.close()

# WAP to write in a binary file.
import pickle
file = open('employee.bin','ab')
pickle.dump('Simran Sharma',file)
file.close()


# WAP to read a binary file
import pickle
file = open('employee.bin','rb')
data = pickle.load(file)
print(data)
file.close()

# Read A File With Loop
import pickle
file = open('employee.bin','rb')
try:
    while True:
        data = pickle.load(file)
        print(data)
except:
    print("\nRead Successfully!")
file.close()


"""
import pickle
file = open('employee.bin','rb')
try:
    while True:
        data = pickle.load(file)
        print(data)
except:
    print("\nRead Successfully!")
file.close()



