/*
# DML :- Data Manipulation Language
	INSERT (C) , SELECT (R) , UPDATE (U) , DELETE (D)
    CRUD Operations
    
    INSERT INTO table_name VALUE(val1,val2,val3...);
INSERT INTO employee VALUE(101,'Rahul','Noida','rahul123@gmail.com');

	SELECT * FROM table_name;
SELECT * FROM employee;

INSERT INTO table_name(col1,col2,col3) VALUE(val1,val2,val3); 
*/
CREATE DATABASE amazon;
USE amazon;
CREATE TABLE employee(
eid INT ,
ename TEXT , 
emobile TEXT , 
eadd TEXT
); 
ALTER TABLE employee ADD COLUMN eemail TEXT;
DESCRIBE employee;
ALTER TABLE employee DROP COLUMN emobile;
DESCRIBE employee;

INSERT INTO employee VALUE(102,'Ravi','Delhi','ravi123@gmail.com');
SELECT * FROM employee;

INSERT INTO employee VALUE(103,'Anu','anu123@gmail.com'); # It will raise an error
INSERT INTO employee(eid,ename,eemail) 
VALUE(103,'Anu','anu123@gmail.com'); 

SELECT * FROM employee;

# INSERT
INSERT INTO employee(eid,ename,eadd) 
VALUE(104,'Yogesh','Noida');

# READ
SELECT ename,eemail FROM employee; 

SELECT * FROM employee;		

# UPDATE
UPDATE employee SET eadd='GZB' WHERE eid=103; 
UPDATE employee SET eemail='yogesh123@gmail.com' WHERE eid=104; 

# DELETE
DELETE FROM employee WHERE eid=102; 
SELECT * FROM employee;
DELETE FROM employee WHERE eadd='Noida';

