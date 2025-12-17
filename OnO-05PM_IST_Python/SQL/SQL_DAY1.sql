/*
Data
Database
Database Management System (DBMS)
MySQL , SQL Server , PostgreSQL , Oracle etc
SQL -> Structure Query Language
SQL :- It is a standard programming language used to manage
and interact with databases
SQL Works on commands

DDL : Data Definition Language
It is use to create SCHEMA (Structure of Database)
CREATE , DROP , ALTER

DML : Data Manipulation Language
It is use to manage data in a table
INSERT , DELETE , UPDATE , SELECT

TCL : Transaction Control Language
DCL : Data Control Language


SQL is not case sensitive
aman = AMAN
create  =  CREATE
SQL query can be reuse.


DDL
WAQ to create a database.
Syntax:-   CREATE DATABASE database_name;
CREATE DATABASE school;

WAQ to delete a database.
Syntax:-   DROP DATABASE database_name;
DROP DATABASE store;

WAQ to select a database.
Syntax:-    USE database_name;
USE school;

WAQ to create a table.
Syntax:-    CREATE TABLE table_name;
With columns:-
CREATE TABLE table_name(
col_name1 Data_Type ,
col_name2 Data_Type , 
col_name3 Data_Type ,
.......
);

WAQ to add a new column in a existing table.
Syntax: ALTER TABLE table_name ADD COLUMN col_name Data_Type;
ALTER TABLE student ADD COLUMN sadd TEXT;

WAQ to drop a column from a existing table.
Syntax: ALTER TABLE table_name DROP COLUMN col_name;
ALTER TABLE student DROP COLUMN semail;
*/
CREATE DATABASE school;
USE school;
CREATE TABLE student(
sid INT ,
sname TEXT ,
smobile TEXT ,
semail TEXT 
);
ALTER TABLE student ADD COLUMN sadd TEXT;
ALTER TABLE student DROP COLUMN semail;