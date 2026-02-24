"""
File Handling

Type of files
1- Text File
2- Binary File (.bin , .dat etc) (Encoded Files)

Text File (.txt , .xlsx , .docx etc)


file_pointer = open( 'file_name.extension' , 'mode' )
mode =>  w , r , a , w+ , r+ , a+
after working in the file, you have to close the file

file_pointer.close()


file = open('student.txt' , 'w')
print("File open!")
file.close()


# WAP TO WRITE DATA IN A FILE

file = open('student.txt' , 'w')

file.write("Aman KUmar")

file.close()
print("File Close!")




file = open('student.txt' , 'a')

file.write("\nShiva Yadav")

file.close()
print("File Close!")



# WAP to read data from a file

file = open('student.txt','r')
data = file.read()      #  it will read all data atonce
print(data)
file.close()



file = open('student.txt','r')
data = file.readline()   # read a single line
print(data)
file.close()



file = open('student.txt','r')
for i in range(3):
    data = file.readline()   
    print(data)
file.close()



file = open('student.txt','r')
while True:
    data = file.readline()   
    print(data)
    if len(data) == 0:
        break
file.close()




file = open('student.txt','r')
data = file.readlines()  # it will convert all lines into a list
print(data)
file.close()



file = open('student.txt','r')
data = file.readlines()  # it will convert all lines into a list
for a in data:
    print(a)
file.close()


"""

