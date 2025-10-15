CREATE DATABASE oracle;
USE oracle;
# Primary key => UNIQUE + NOT NULL
# DECIMAL(8,2)  =>  999999.99

/*
1 Byte => 8 bit -> 1bit reserve (+-) , 7bit -> 2^7
TINYINT     1 Byte  -128 to 127  
SMALLINT    2 Byte  -32,768 to 32,767     2^15
MEDIUMINT   3 Byte  -83,88,608  to 83,88,607   2^23
INT         4 Byte  -214Cr to 214Cr    2^31
BIGINT      8 Byte  2^63
*/

# INT 4bytes => 4*8=> 32bit =>  2^31 => 214Cr+   5,6,7,8,9
# BIGINT 8bytes => 8*8 => 64bit => 2^63 => 92KCrCr

CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT ,
ename VARCHAR(40) NOT NULL , 
mobile VARCHAR(15) NOT NULL , 
email VARCHAR(40) UNIQUE NOT NULL ,
joining_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
esal DECIMAL(8,2) NOT NULL ,
estatus BOOL DEFAULT TRUE
);
INSERT INTO employee(eid,ename , mobile , email , esal ) 
VALUE(5,'Suman','+91987345734','suman@gmail.com',34468.46);
SELECT * FROM employee;
INSERT INTO employee(ename , mobile , email , esal ,eage) 
VALUE('Rohan','+91857369734','rohan@gmail.com',83468.46 , 26);
SELECT * FROM employee;

ALTER TABLE employee ADD COLUMN eage INT CHECK (eage>17);

# WHERE 
SELECT * FROM employee;
SELECT * FROM employee WHERE esal<=50000;

# AND , OR
SELECT * FROM employee WHERE esal>50000 AND esal<70000;
# BETWEEN
SELECT * FROM employee WHERE esal BETWEEN 50000 AND 70000;
# OR
SELECT * FROM employee WHERE esal<40000 OR eage>18;

DROP TABLE employee;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT ,
ename VARCHAR(40) NOT NULL , 
esal DECIMAL(8,2) NOT NULL , 
edesg VARCHAR(20) NOT NULL , 
eadd VARCHAR(20) NOT NULL
);
INSERT INTO employee VALUE (101,'Rahul',34786.56,'IT','Noida');
INSERT INTO employee(ename,esal,edesg,eadd) VALUES
('Raman',43254.45,'HR','Delhi'),
('Baman',67433.45,'HR','Noida'),
('Suman',34765.66,'IT','Noida'),
('Riya',47555.43,'IT','Delhi');

SELECT * FROM employee;
# SUM , MAX , MIN , AVG , count 
SELECT sum(esal) FROM employee;
SELECT max(esal) FROM employee;
SELECT min(esal) FROM employee;
SELECT avg(esal) FROM employee;
SELECT count(esal) FROM employee;

# ORDER BY
SELECT * FROM employee;
SELECT * FROM employee ORDER BY esal ASC;
SELECT * FROM employee ORDER BY esal DESC;

