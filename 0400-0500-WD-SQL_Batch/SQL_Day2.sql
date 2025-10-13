# DDL -> Data Definition Language
# CREATE ALTER DROP
/*
How to create a database
CREATE DATABASE database_name;

How to select a Database
USE database_name;

How to create a table inside a database
CREATE TABLE table_name(
col_name1 Data_Type , 
col_name2 Data_Type , 
col_name3 Data_Type ,
.....
);

How to add a new column in a existing table
ALTER TABLE table_name ADD COLUMN col_name Data_Type;

How to remove a column from a table
ALTER TABLE table_name DROP COLUMN col_name;

How to convert data type of a column
ALTER TABLE table_name MODIFY COLUMN colname new_data_type;


*/
CREATE DATABASE school;
USE school;
CREATE TABLE student(
sid INT ,
sname TEXT ,
scourse TEXT ,
sadd TEXT 
);
ALTER TABLE student ADD COLUMN semail TEXT;
ALTER TABLE student DROP COLUMN sadd;
ALTER TABLE student ADD COLUMN mobile INT;
ALTER TABLE student MODIFY COLUMN mobile TEXT;

# DML :- Data Manipulation Language
# CURD- Create,Update,Read,Delete Opertions
# Commands:-  INSERT , UPDATE , SELECT , DELETE

/*
How to insert data in a table
INSERT INTO table_name VALUE(val1,val2,val3..);

How to read a data from a table
SELECT col1,col2,col3.. FROM table_name;
SELECT sid,sname,scourse,semail,mobile FROM student;
Other way
SELECT * FROM table_name;
*/
INSERT INTO student
VALUE(101,'Ravi','DSA','ravi@gmail.com','+9198628772');

SELECT sid,sname,scourse,semail,mobile FROM student;

SELECT * FROM student;
SELECT sid,sname FROM student;
INSERT INTO student(sid,sname,scourse,mobile) 
VALUE(102,'Mohan','Python','+91863803444');

SELECT * FROM student;
INSERT INTO student 
VALUE(103,'Rohan','Java','rohan@gmail.com','+91863803444');

# REMOVE SAFE_MODE
SET sql_safe_updates=0;

# UPDATE
UPDATE student SET semail='mohan@gmail.com' WHERE sid=102;
SELECT * FROM student;

# DELETE 
DELETE FROM student WHERE sid=101;