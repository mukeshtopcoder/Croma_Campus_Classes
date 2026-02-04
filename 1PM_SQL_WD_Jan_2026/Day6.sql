/*
DDL:- Data Definition Language

TINYINT 1B(8 bits)  -128 to 127
	1 bit reserved for signed value (-,+)
	7 bit => 2^7 => 128
SMALLINT 2B (16 bits) -32768 to 32767
	1 bit reserved for signed value (-,+)
    15 bit => 2^15 => 32768
MEDIUMINT 3B (24 bits)
INT 4B (32 bits) -214Cr to 214Cr
BIGINT 8B (64 bits)  90KCrCr

FLOAT 4B
DOUBLE 8B
DECIMAL(limit_number , point_value)

TINYTEXT => 255 Chracters
TEXT => 65K characters 
MEDIUMTEXT 
LARGETEXT

CHAR(N) => 255 Charcters
VARCHAR(N) => 0-65K characters

DECIMAL(8,2)   A number of 8 digits and with 2 decimal value included in 8 digits
275372.72

BOOL/BOOLEAN     1Byte (TINYTINT(N)) 

*/

CREATE DATABASE amazon;
USE amazon;
CREATE TABLE employee(
eid INT ,
ename VARCHAR(25),
eadd VARCHAR(200) , 
eemail TINYTEXT , 
mobile VARCHAR(15) , 
esal DECIMAL(8,2),              
estatus BOOLEAN 
);

# PRIMARY KEY => can not store duplicate and blank/null values 
# (Primary key can be foreign key for another table) 
CREATE TABLE product(
pid INT PRIMARY KEY AUTO_INCREMENT ,
pname VARCHAR(30) NOT NULL ,
price DECIMAL(8,2) NOT NULL
);

# ONLY ONE PRIMARY KEY CAN BE POSSIBLE IN ONE TABLE
# UNIQUE can not store duplicate (duplicate not allowed)
# BUT Unique can store NULL
DROP TABLE employee;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT , 
ename VARCHAR(30)  NOT NULL , 
eemail VARCHAR(50) UNIQUE NOT NULL , 
eage TINYINT NOT NULL CHECK (eage>17) ,
esal DECIMAL(8,2) NOT NULL ,
ecountry VARCHAR(20) DEFAULT "INDIA",
estatus BOOLEAN DEFAULT 1
);
INSERT INTO employee(ename,eemail,eage,esal)
VALUE("Raman",'raman123@gmail.com',28,72437.34);
INSERT INTO employee(ename,eemail,eage,esal)
VALUE("Mohan",'mohan123@gmail.com',26,26237.34); 

INSERT INTO employee(ename,eemail,eage,esal)
VALUE("Raman Kumar",'raman12345@gmail.com',22,34763.34);

SELECT * FROM employee;

INSERT INTO employee(ename,eemail,eage,esal)
VALUE("Suman Kumar",'suman12345@gmail.com',22,34763.34);