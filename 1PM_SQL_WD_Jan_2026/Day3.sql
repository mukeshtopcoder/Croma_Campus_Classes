/*
SQL :- Structure Query Language

Schemas:- Structure of the database (db , tables , columns , data_type)

SQL works on commands 
DDL - Data Definition Language
	Use to design a Schema ( CREATE , ALTER , DROP )
DML - Data Manipulation Language
	Interaction with data / CRUD Operation with Data ( SELECT , DELETE , UPDATE , INSERT )
DCL - Data Control Language
	GRANT , REVOKE
TCL - Transaction Control Language
	TRANSACTION , ROLLBACK , COMMIT , SAVEPOINT

DDL (Data Definition Language)
	CREATE ALTER DROP
SQL is not case sensitive language
	create , CREATE , Create (All are same for SQL)

# HOW TO CREATE A DATABASE
	CREATE DATABASE database_name;

# HOW TO SELECT A DATABASE
	USE database_name;

# HOW TO CREATE A TABLE
	CREATE TABLE table_name(col1 Data_Type, col2 Data_Type);
*/
CREATE DATABASE amazon;
create database amazon;
USE amazon;

CREATE TABLE customer(
cid INT , 
cname TEXT ,
cmobile TEXT ,
cadd TEXT
); 

CREATE TABLE product(
product_id INT ,
product_name TEXT ,
product_price INT 
);

# HOW to add a new column in table
# ALTER TABLE table_name ADD COLUMN col_name Data_Type;
ALTER TABLE product ADD COLUMN product_category TEXT;

DESCRIBE product;
DESCRIBE customer;
# HOW TO REMOVE A COLUMN FROM A TABLE
# ALTER TABLE table_name DROP COLUMN col_name;

ALTER TABLE customer DROP COLUMN cadd;
