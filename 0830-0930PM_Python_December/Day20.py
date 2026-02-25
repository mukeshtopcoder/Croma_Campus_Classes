"""

File Handling
Binary File ( .dat , .bin etc )


file_pointer = open('file_name.extension' , 'mode')
mode :->  rb , wb , ab , wb+ , rb+ , ab+


import pickle
pickle.dump(data , file_pointer)
pickle.load(file_pointer)


# WAP to open a binary file


file = open( 'employee.bin' , 'wb' )
file.close()


# WAP to write in a binary file


import pickle
file = open( 'employee.bin' , 'ab' )
pickle.dump('Akash Singh' , file)
file.close()


# WAP to read a binary file


import pickle
file = open( 'employee.bin' , 'rb' )
for i in range(3):
    data = pickle.load(file)
    print(data)
file.close()



import pickle
file = open( 'employee.bin' , 'rb' )
try:
    while True:
cid = input("Enter Customer ID : ")
        data = pickle.load(file)
        print(data)
except:
    print('File Read Successfully!')
file.close()


# WAP to add customer details in a file

import pickle
cid = input("Enter Customer ID : ")
cname = input("Enter Customer Name : ")
cadd = input("Enter Customer Address : ")
cmob = input("Enter Customer Mobile : ")

file = open('customer.bin','ab')
pickle.dump(cid,file)
pickle.dump(cname,file)
pickle.dump(cadd,file)
pickle.dump(cmob,file)
file.close()
print("\nCutomer Added Succesfully!")


# WAP to view All Customer Details

import pickle
file = open('customer.bin' , 'rb')
try:
    print("\nCID\tCName\tCAdd\tCMob\n")
    while True:
        for i in range(4):
            data = pickle.load(file)
            print(f'{data}\t',end='')
        print()
except:
    print("\nHere is your all customer")
file.close()


"""
