/*
DDL:- Data Definition Language
# WAQ to create a database.
Syntax:-   CREATE DATABASE database_name;

# WAQ to select a database.
Syntax:-   USE database_name;

# WAQ to create a table;
Syntax:- CRAETE TABLE table_name;
CREATE TABLE table_name(
col_name1 data_type , 
col_name2 data_type , 
col_name3 data_type ,
.....
);

*/

CREATE DATABASE croma_campus;
USE croma_campus;
CREATE TABLE student(
sid INT ,
sname TEXT , 
sadd TEXT , 
smobile TEXT
);