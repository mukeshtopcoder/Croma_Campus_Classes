/*
INDEX
Indexes in MySQL are used to speed up data retrival (SELECT queries).

An index is a data structure that improves query performance by reducing the number 
of rows MySQL must scan.

Pros:-
Faster SELECT
Faster WHERE , JOIN , ORDER BY
Cons:-
Slower INSERT , UPDATE , DELETE (because index must update)

*/
USE amazon;
SHOW TABLES;
DROP TABLE employee;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT ,
ename VARCHAR(100) NOT NULL , 
eadd VARCHAR(100) NOT NULL , 
esal DECIMAL(8,2) NOT NULL
);

INSERT INTO employee VALUES
(106,'Renu Singh','Noida',37670);

SELECT * FROM employee;
SELECT * FROM employee WHERE eid=104;
SELECT * FROM employee WHERE eid>103;

/*
Avoid INDEX when:-
small table
columns has very few unique values (Gender)
Index_Type		Description
PRIMARY KEY 	(UNIQUE + NOT NULL)
UNIQUE 			No Duplicate Values
INDEX (Normal)  Allow Duplicates
Composite 		Multiple Columns

*/


SELECT * FROM employee WHERE eid=103;    # It is fast because eid is a primary key index
SELECT * FROM employee WHERE eadd='Noida';  # It is slow because eadd is not a INDEX

/*
Syntax for creating INDEX
CREATE INDEX index_name
ON employee(column_name);
Example:-
CREATE INDEX idx_eadd
ON employee(eadd);		# Allow Duplicate

# UNIQUE INDEX
CREATE UNIQUE INDEX idx_eadd    
ON employee(eadd);      # Do not allow duplicates
*/
# Normal INDEX
CREATE INDEX idx_eadd
ON employee(eadd);

SELECT * FROM employee WHERE eadd='Noida';  # It will work fast because eadd is now an INDEX
SHOW INDEX FROM employee;

EXPLAIN SELECT * FROM employee WHERE esal>20000;   # type=> All (FULL TABLE SCAN) means slow
EXPLAIN SELECT * FROM employee WHERE eadd='Noida'; # type=> ref (Filtred Table Scan) Means fast


SELECT * FROM employee WHERE eadd='Delhi' AND esal>40000; 
# This query will work slow because only eadd is an INDEX not esal
EXPLAIN SELECT * FROM employee WHERE eadd='Delhi' AND esal>40000;

# COMPOSITE INDEX
CREATE INDEX idx_esal_eadd
ON employee(eadd,esal); 

SELECT * FROM employee WHERE eadd='Delhi' AND esal>40000; 
EXPLAIN SELECT * FROM employee WHERE eadd='Delhi' AND esal>40000; 

SHOW INDEX FROM EMPLOYEE;

/*
Index use BTREE (Balanced TREE) Fast Search (O(Log n)) Algorithm
USED for = > < BETWEEN LIKE 'abc%'
*/

