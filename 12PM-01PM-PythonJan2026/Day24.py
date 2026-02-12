"""
File Handling
Binary File

import pickle
pickle.dump( data , file_pointer )   # to write data
pickle.load( file_pointer )          # to read data

file_pointer = open( 'file_name.extension' , 'mode' )

extension:-   .bin , .dat etc
mode:-   rb , wb , ab , rb+ , wb+ , ab+


# WAP to write data in a binary file
import pickle
file = open( 'student.bin' , 'ab' )
pickle.dump('Simran Khurana',file)
file.close()


# WAP to read data from binary file

import pickle
file = open( 'student.bin' , 'rb' )
for i in range(4):
    print( pickle.load(file) )
file.close()



import pickle
file = open( 'student.bin' , 'rb' )
try:
    while True:
        print( pickle.load(file) )
except:
    print("File Read Successfully!")
file.close()



import pickle
file = open( 'student.bin' , 'rb' )
try:
    while True:
        print( pickle.load(file) )
except:
    print("File Read Successfully!")
file.close()



"""









