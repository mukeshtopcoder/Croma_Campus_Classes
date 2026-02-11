"""
File Handling:-

Types of files
1- Text File  (.txt , .docx , .xlsx etc)
2- Binary File (.bin , .dat etc)


TEXT FILE
file_pointer = open( 'file_name.extension'  ,  'mode' )
mode =>  r , w , a , r+ , w+ , a+

# CLOSE FILE
file_pointer.close()


file = open( 'data.txt' , 'w' )

file.close()


# WAP to write something in the file

file = open( 'data.txt' , 'a' )

# file.write("Raman Kumar")
# file.writelines("Siya Singh")
# write , writelines both are same use to write data in file
file.close()


file = open( 'data.txt' , 'a' )
file.write("\nVikas Kumar")
file.close()


# WAP to read data from a file

file = open( 'data.txt' , 'r' )
print( file.read() )   # read all data from file
file.close()



file = open( 'data.txt' , 'r' )
print( file.read(10) )  # read 10 characters of a file
file.close()



file = open( 'data.txt' , 'r' )
print( file.readline() ) # read first line  
print( file.readline() ) # read second line
file.close()



file = open( 'data.txt' , 'r' )
for i in range(4):
    print( file.readline() )
file.close()




file = open( 'data.txt' , 'r' )

while True:
    data = file.readline()
    if data == "":
        break
    print(data)
    
file.close()




file = open( 'data.txt' , 'r' )
print( file.readline(2) )  # read only two characters
file.close()



file = open( 'data.txt' , 'r' )

print( file.readlines() )  # read all lines and append in a list
    
file.close()




file = open( 'data.txt' , 'r' )

data = file.readlines()
for line in data:
    print(line)

file.close()





file = open( 'data.txt' , 'r' )

print( file.tell() )  # tells cursor position in a file
print( file.read(10) )
print( file.tell() )

file.close()






file = open( 'data.txt' , 'r' )

print( file.tell() )  # tells cursor position in a file
print( file.readline() )
print( file.tell() )

file.close()






file = open( 'data.txt' , 'r' )

file.seek(10)   # it will take cursor to the next 10 charcters
# it will skip 10 characters
print( file.read(10) )

file.close()




file = open( 'data.txt' , 'r' )

print( file.tell() )
print( file.read(10) )
print( file.tell() )

file.close()





# Q9 String Exercise
Check if two strings are ANAGRAM

    LISTEN , SILENT


st1 = "LISTEN"
st2 = "SILENT"
if len(st1)==len(st2):
    for ch in st1:
        if st1.count(ch)!=st2.count(ch):
            print("Strings Are Not Anagram")
            break
    else:
        print("Strings Are Anagram")
else:
    print("Strings Are Not Anagram")

    
"""

