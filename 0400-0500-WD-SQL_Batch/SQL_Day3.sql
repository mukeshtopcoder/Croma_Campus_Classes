/*
# DDL :-  Data Definition Language
- CREATE , DROP , ALTER
*/
DROP DATABASE school;
CREATE DATABASE college;
USE college;

CREATE TABLE student(
sid INT , 
sname TEXT , 
course TEXT 
);
ALTER TABLE student ADD COLUMN email TEXT;
ALTER TABLE student DROP COLUMN course;

# DML :- Data Manipulation Language
# INSERT , DELETE , UPDATE , SELECT
INSERT INTO student(sid,sname) VALUE(102,'Mohan');
SELECT * FROM student;

# NEW DATABASE
CREATE DATABASE amazon;
USE amazon;
# PRIMARY KEY => UNIQUE + NOT NULL
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT ,
ename VARCHAR(40) NOT NULL ,
email VARCHAR(100) UNIQUE NOT NULL ,
esal DECIMAL(8,2) NOT NULL ,   # 999999.99
mobile VARCHAR(15) NOT NULL ,
roles VARCHAR(20) DEFAULT "Admin Staff" ,
time_ TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO employee(ename,email,esal,mobile)  VALUE
('Raman Singh','raman@gmail.com',63544.83,'+91897348754');
INSERT INTO employee(ename,email,esal,mobile)  VALUE
('Suresh Sharma','suresh@gmail.com',38754.74,'+9138748744453');

SELECT * FROM employee;

# INT => 4 byte => 8*4 => 32bit => 2^31 => 214Cr+