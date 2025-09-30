CREATE DATABASE croma;
USE croma;
# PRIMARY KEY ->  Unique + NOT NULL (not blank)
CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT,
sname VARCHAR(30) NOT NULL , 
smobile VARCHAR(15) NOT NULL ,
semail VARCHAR(40) UNIQUE NOT NULL , 
sage TINYINT NOT NULL CHECK (sage>15) , 
sactive BOOL DEFAULT 1 ,
sfee DECIMAL(8 , 2) NOT NULL ,
addmission_date DATE, 
joining_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO student(sname , smobile , semail , sage ,sfee)
VALUE('Monu','+919623768332','monu@gmail.com',21,27233);
SELECT * FROM student;
/*
INT 4 Bytes - 4*8 => 32 Bits => 2^31 => 214Cr+

Data Type	Storage	Signed Range	
1 Byte  =   8 Bits  
TINYINT	    1 byte	-128 to 127
SMALLINT	2 bytes	-32,768 to 32,767	
MEDIUMINT	3 bytes	-8,388,608 to 8,388,607	
INT     	4 bytes	-2,147,483,648 to 2,147,483,647	
BIGINT	    8 bytes	-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807

DECIMAL(8,2)
value can be upto 8 digits (including points value)
max value =>   999999.99
*/

