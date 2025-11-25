r"""
File Handling
1- Text File
    (notepad, word , excel etc)
2- Binary File
    (Encoded files , .vcd , .dat , .bin etc)

TEXT FILES
file_handler = open('file_name.ext' , 'mode')
mode => r,w,a,r+,w+,a+


file = open('temp.txt','w')
file.close()

file = open(r"c:\users\Croma Campus\Desktop\temp.txt",'w')
file.close()

# Method:- write , writelines

file = open("temp.txt",'a')
file.write("\nShiva Yadav")
file.close()

file = open("temp.txt",'a')
file.writelines("\nRahul Singh")
file.close()

file = open("temp.txt",'a')
li = ['\nSonu Singh','\nRaja']
file.writelines(li)
file.close()

Methods:-  read , readline , readlines

file = open("temp.txt",'r')
data = file.read()
print(data)
file.close()


file = open("temp.txt",'r')
data = file.read(20)    # it will read 20 characters
print(data)
file.close()

file = open("temp.txt",'r')
data = file.readline()  
print(data)
file.close()


file = open("temp.txt",'r')
data = file.readline()  
print(data)
data = file.readline()  
print(data)
file.close()


file = open("temp.txt",'r')
data = file.readline(10)     # it will read 10 characters  
print(data)
file.close()


file = open("temp.txt",'r')
data = file.readlines()  
print(data)  # print a list of all lines
file.close()


file = open("temp.txt",'r')
data = file.readlines()  
for line in data:
    print(line,end='')
file.close()



file = open("temp.txt",'r')
for i in range(20):
    data = file.readline()  
    print(data)
file.close()



file = open("temp.txt",'r')
while True:
    data = file.readline()
    if len(data)==0:
        break
    print(data,end='')
file.close()


BINARY FILE
pickle module/library
dump , load  (dump => write , load => read)

file_handler = open('file_name.bin','mode')
mode =>   wb,ab,rb,wb+,ab+,rb+


file = open('student.bin' , 'wb')
file.close()


Write in a binary file
import pickle
file = open('student.bin' , 'ab')
pickle.dump('Vikas Kumar',file)
file.close()

Read a binary file

import pickle
file = open('student.bin' , 'rb')
data = pickle.load(file)
print(data)
file.close()


import pickle
file = open('student.bin' , 'rb')
for i in range(3):
    data = pickle.load(file)
    print(data)
file.close()


import pickle
file = open('student.bin' , 'rb')
try:
    while True:
        data = pickle.load(file)
        print(data)
except:
    print("\nRead Successfully!")
file.close()

"""

