"""
File Handling:- File handling is related to that how we
can interact with files.

Files
Text File
Binary File

Text File:- .txt , .docx , .xlsx  , .csv etc

file_object = open( 'file_name.extention' , 'mode' )
mode:-  r , w , a (append) , r+ (rw) , w+ (wr) , a+ (ar)
file_object.close()
Example:-

file = open( 'student.txt' , 'w' )

file.close()


# WAP to write something in the file

file = open( 'student.txt' , 'w' )
file.write("Shiva Yadav ")
file.close()



file = open( 'student.txt' , 'a' )
file.write("Ravi Kumar\n")
file.close()


# WAP to read a file

file = open( 'student.txt' , 'r' )
print( file.read() )
file.close()


"""
