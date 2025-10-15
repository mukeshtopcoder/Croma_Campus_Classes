CREATE DATABASE oracle;
USE oracle;
/*
# PRIMARY KEY => UNIQUE + NOT NULL
# TEXT => 255 BIT (255 chracters) ANU - 252BIT Blocked
# Varchar(40) => 40 BIT (40 chracters) ANU - 37BIT Blocked

TINYINT 1Byte => 8bit - 1bit reserved(+-) 2^7 => -128 to 127
SMALLINT 2Byte => 16bit => 2^15 => -32,768 to 32,767
MEDIUMINT 3Byte => 24bit => 2^23 => -83L to 83L+
INT or INTEGER => 4Byte => 32Bit => 2^31 => -214Cr to 214Cr
BIGINT => 8Byte => 64Bit => 2^63 => 92KCRCR

DECIMAL(8,2)   =>  999999.99
*/
CREATE TABLE employee(
eid SMALLINT PRIMARY KEY AUTO_INCREMENT ,
ename VARCHAR(40) NOT NULL ,
emobile VARCHAR(15) NOT NULL , 
esal DECIMAL(8,2) NOT NULL , 
eage TINYINT CHECK (eage>17) NOT NULL ,
joining_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
estatus BOOL DEFAULT TRUE
);
INSERT INTO employee(ename,emobile,esal,eage) VALUE
('Rihan','+9128638344',98268.56,26);
SELECT * FROM employee;
INSERT INTO employee(eid,ename,emobile,esal,eage)
VALUE(5,'Rohan','+9134638344',37455.45,26);
SELECT * FROM employee;

# DELETE , UPDATE
DELETE FROM employee;
# WHERE Clause
DELETE FROM employee WHERE eid=4;
SELECT * FROM employee;
DELETE FROM employee WHERE eid<5;

SET SQL_SAFE_UPDATES=0;

UPDATE employee SET esal=77000 WHERE eid=102;
SELECT * FROM employee;