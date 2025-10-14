# DDL : Data Definition Language
# CREATE ALTER DROP
CREATE DATABASE school;
USE school;
CREATE TABLE student(
sid INT ,
sname TEXT , 
semail TEXT
);
ALTER TABLE student ADD COLUMN sadd TEXT;
ALTER TABLE student DROP COLUMN semail;

# DML :- Data Manipulation Language
# INSERT , DELETE , SELECT , UPDATE
INSERT INTO student VALUE(101,'Ravi Kumar','Noida');
SELECT sid,sname,sadd FROM student;
SELECT sid,sname FROM student;
SELECT * FROM student;

INSERT INTO student VALUES
(102,'Rohan','Delhi'),
(103,'Riya','GZB');

SELECT * FROM student;
INSERT INTO student(sid,sname) VALUE(104,'Ravi Kumar');
INSERT INTO student(sadd,sname) VALUE('Noida','Ravi Kumar');
# Remove Safe Mode
SET sql_safe_updates = 0;
UPDATE student SET sadd='Amroha' WHERE sid=104;
SELECT * FROM student;

DELETE FROM student WHERE sname='ravi kumar';
SELECT * FROM student;

# INSERT , SELECT , DELETE , UPDATE
# CURD ->  Create , Update , Read , Delete Operations

# DML
DROP TABLE student;
# PRIMARY KEY => UNIQUE + NOT NULL 
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT ,
ename VARCHAR(40) NOT NULL ,
mobile VARCHAR(15) NOT NULL , 
email VARCHAR(40) UNIQUE 
);

# INT 4bytes => 4*8=> 32bit =>  2^31 => 214Cr+   5,6,7,8,9
# BIGINT 8bytes => 8*8 => 64bit => 2^63 => 92KCrCr