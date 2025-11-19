/*
# DML :- Data Manipulation Language
We need to perform CURD operations on a database/table.
C - Create
U - Update
R - Read
D - Delete

SQL Commands:- INSERT , DELETE , UPDATE , SELECT
*/
CREATE DATABASE college;
USE college;
CREATE TABLE student(
sid INT , 
sname TEXT ,
semail TEXT , 
scourse TEXT 
);
# HOW TO insert data in this table
# INSERT INTO table_name VALUE(val1,val2,...);
INSERT INTO student 
VALUE(102,'Mohan','mohan@gmail.com','M.Tech');

# HOW TO READ DATA FROM A TABLE
SELECT * FROM student;

# ISNERT INTO table_name(col1,col2..) VALUE(val1,val2..);
INSERT INTO student(sid,sname,scourse)
VALUE(103,'Ravi','MCA');

INSERT INTO student VALUES
(104,'Riya','riya@gmail.com','BCA'),
(105,'Suman','suman@gmail.com','MSc'),
(106,'George','george123@gmail.com','BSc'),
(107,'Bob','bob123@gmail.com','BBA');

SELECT * FROM student;
SELECT sid,sname,scourse FROM student;

SELECT * FROM student;

SET SQL_SAFE_UPDATES = 0;
UPDATE student SET semail='ravi@gmail.com' WHERE sid=103;

SELECT * FROM student;
UPDATE student SET semail='riya123@gmail.com' WHERE sid=104;

DELETE FROM student WHERE sid>104;

DROP TABLE student;

# PRIMARY KEY => UNIQUE(No Duplicates) + NOT NULL
CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT ,
sname VARCHAR(40) NOT NULL ,
semail VARCHAR(40) UNIQUE NOT NULL , 
smobile VARCHAR(15) NOT NULL ,
sage INT NOT NULL CHECK (sage>9) ,
sfee DECIMAL(8,2) DEFAULT 0.0
); 
/*
DECIMAL(8,2)  =>  999999.99
DECIMAL(65,30)  =>  Maximum limits for decimal

# ERD => Entity Relationship Diagram
# DFD => Data Flow Diagram

TINYINT  -  -128 to 127        1byte
SMALLINT -  -32,768 to 32767   2 Byte
MEDIUMINT -  -8M to 8M         3Byte
INT    -     -2B to 2B         4Bytes
BIGINT -     -9 Quintillion    8Bytes

CHAR (10)     -- Upto 255 Characters
# ANU-> 3 characters - 7 characters's memory is going to block

VARCHAR (10)     -- Upto 65535 Characters
# ANU-> 3 characters - 7 characters's memory is not going to block

TINYTEXT - 255 Bytes
TEXT - 65KB
MEDIUMTEXT - 16MB
LONGTEXT - 4GB 
*/