/*
DBMS (Database Management System) (MySQL , SQL Server , MongoDB)

RDBMS (Relational DBMS => MySQL , SQL Server , Oracle etc)
NoSQL DBMS (MongoDB , Mangoose , MariaDB etc) 

SQL:- Structure Query Language (SQL works on commands)
DDL , DML , DCL , TCL
DDL:- Data Definition Language
	CREATE , ALTER , DROP
these commands use to create schema

MySQL is not case sensitive language

# HOW TO DELETE/DROP DATABASE
DROP DATABASE database_name;

DROP DATABASE amazon;
drop database bank;
DROP DATABASE sales;

# HOW TO CREATE A DATABASE
CREATE DATABASE database_name;
CREATE DATABASE croma;
CREATE DATABASE college;   # ; ( terminator )

# HOW TO SELECT A DATABASE TO WORK ON IT
USE database_name;
USE croma;

# HOW TO CREATE A TABLE IN A DATABASE
CREATE TABLE table_name(col_name data_type);
INT => Numerical Data (non-decimal value / without point value)

CREATE TABLE trainer( trainer_id INT );


*/
CREATE TABLE student(
student_id INT ,
student_name TEXT , 
student_mobile TEXT , 
student_fee INT , 
student_address TEXT
);

SHOW DATABASES;
SHOW TABLES;
USE croma;
DESCRIBE student;

# ALTER (Changes)
# REMOVE A COLUMN
ALTER TABLE student DROP COLUMN student_address;
# ADD A NEW COLUMN
ALTER TABLE student ADD COLUMN student_email TEXT;