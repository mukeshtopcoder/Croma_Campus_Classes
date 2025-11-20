CREATE DATABASE college;
USE college;
CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT ,
sname VARCHAR(40) NOT NULL ,
semail VARCHAR(40) UNIQUE NOT NULL , 
smobile VARCHAR(15) NOT NULL ,
sage INT NOT NULL CHECK (sage>9) ,
sfee DECIMAL(8,2) DEFAULT 0.0
); 
INSERT INTO student(sname,semail,smobile,sage)
VALUE('Rahul Sharma','rahul@gmail.com','+919728358279',24);

SELECT * FROM student;
INSERT INTO student(sname,semail,smobile,sage)
VALUE('Manu Yadav','manu@gmail.com','+919728358279',17);

SELECT * FROM student;
INSERT INTO student(sname,semail,smobile,sage)
VALUE('Abhishek Kumar','abhishek@gmail.com','+9197276789292',16);

SELECT * FROM student;
UPDATE student SET semail='abhishek123@gmail.com' WHERE sid=5;

DELETE FROM student WHERE sid=2;
DELETE FROM student WHERE semail='abhishek123@gmail.com';

# DDL , DML


# DDL:- CREATE , ALTER , DROP , TRUNCATE , RENAME
CREATE DATABASE amazon;
USE amazon;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT , 
ename VARCHAR(100) NOT NULL , 
eadd VARCHAR(100) NOT NULL , 
esal DECIMAL(8,2) NOT NULL
);

ALTER TABLE employee ADD COLUMN bonus DECIMAL(8,2);
DESCRIBE employee;
# MODIFY USE TO change data type
ALTER TABLE employee MODIFY esal DECIMAL(12,2) NOT NULL;

SHOW TABLES;
SHOW DATABASES;
# Currently Selected Database
SELECT DATABASE();

DROP TABLE table1,table2,table3;
DROP TABLE student,trainer,employee;
DROP TABLE IF EXISTS student,trainer,employee;

# DDL commands can not be ROLLBACK
# Only DML commands can be ROLLBACK

DESCRIBE employee;
# Using CHANGE rename A COLUMN and its data type
ALTER TABLE employee CHANGE eadd eaddress VARCHAR(100);

# ALTER TABLE table_names MODIFY/CHANGE/ADD/DROP/RENAME col_name;
ALTER TABLE employee RENAME TO staff;
SHOW TABLES;
DESCRIBE staff;

ALTER TABLE staff DROP COLUMN bonus;

# RENAME command is use change the name of a column or table
ALTER TABLE staff RENAME COLUMN esal TO esalary;
DESCRIBE staff;
# CHANGE command is use to rename column and data type also if you want
ALTER TABLE staff CHANGE esalary esalary DECIMAL(12,2);

# DROP
DROP TABLE table1;
DROP TABLE table1,table2,table3;
DROP DATABASE db1;
ALTER TABLE table_names DROP COLUMN col_name;


# TRUNCATE
# USE  to delete all rows from table structure 
# Faster THAN DELETE
TRUNCATE TABLE table_name;
SELECT * FROM student;
TRUNCATE TABLE student;  # DDL
DELETE FROM student;     # DML

# RENAME 
RENAME TABLE old_table TO new_table;
SHOW TABLES;
RENAME TABLE staff TO employee;

DESCRIBE employee;