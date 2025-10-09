"""
File Handling:-
Types of files:-
1) Text File (.TXT , .DOCS , .XLSS etc)
2) Binary File (.vcd , .bin , .dat etc)

1) TEXT Files
file_handler = open('file_name.extension' , 'mode')
file_handler =>  variable name
file_name.extension =>  any_name.txt
mode =>  r , w , a , r+ , w+ , a+

file = open('student.txt','w')
print(file)
file.close()

WAP to write data into the file
file = open('student.txt','w')
file.write("Hello Mumbai")
print("Data Write Successfully!")
file.close()



file = open('student.txt','a')
file.write("\nMahesh Kumar")
print("Data Write Successfully!")
file.close()




# WAP TO READ A TEXT FILE.


file = open('student.txt','r')
print(file)
# print(file.read())  # it will read all the data
# print(file.read(20))  # it will read only 20 characters
# print(file.readline()) # it will read only first line
# print(file.readlines()) # it will read all lines and append into a list
file.close()



file = open('student.txt','r')
for i in range(5):
    print(file.readline())
file.close()


file = open('student.txt','r')
while True:
    data = file.readline()
    if len(data)==0:
        break
    print(data)
file.close()


# tell , seek
tell -> print the position of the cursor

file = open('student.txt','r')
print(file.tell())
print(file.read(20))
print(file.tell())
file.close()

seek -> Skip the position of the cursor

file = open('student.txt','r')
print(file.tell())
file.seek(20)
print(file.read(20)) 
print(file.tell())
file.close()

"""

