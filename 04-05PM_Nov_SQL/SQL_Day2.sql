/*
Multiline Comments
DDL (Data Definition Langauge)
We use to create SCHEMA
CREATE , DROP , ALTER
# How to create a Database
CREATE DATABASE database_name;

SQL is not case sensitive
CREATE , create (both are same)

# HOW TO DELETE/DROP A DATABASE
DROP DATABASE database_name;

# HOW TO SELECT A DATABASE TO USE
USE database_name;

# HOW TO CREATE A TABLE INSIDE A DATABASE
CREATE TABLE table_name(
col_name1 Data_Type ,
col_name2 Data_Type ,
......
);

INT (integer (numerical data ..-3,-2,-1,0,1,2,3...))
*/

CREATE DATABASE school;
DROP DATABASE school;

USE school;
CREATE TABLE student(
student_id INT ,
student_name TEXT ,
student_course TEXT ,
student_address TEXT 
); 

DROP TABLE student;
DESCRIBE student;

ALTER TABLE student ADD COLUMN student_email TEXT;
DESCRIBE student;
ALTER TABLE student ADD COLUMN student_mobile TEXT;

# CHANGE DATA TYPE
ALTER TABLE student MODIFY student_mobile INT;
DESCRIBE student;

# CHANGE THE POSITION OF A COLUMN IN A TABLE
ALTER TABLE student MODIFY student_email TEXT 
AFTER student_name;

ALTER TABLE student MODIFY student_id TEXT FIRST;

# THIS type of modification (positiob of column)
# can only in MySQL and MariaDB 
# NOT SQL Server/Oracle/Postgre etc
