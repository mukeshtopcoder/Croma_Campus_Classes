USE flipkart;
SHOW TABLES;
SELECT * FROM employee;
INSERT INTO employee VALUES
(101,'Riya','HR',72383,'Noida'),
(104,'Rohan','HR',54644,'Delhi'),
(105,'Raj','IT',47555,'Noida'),
(106,'Mohit','IT',56753,'Delhi'),
(107,'Sohit','IT',63543,'Delhi'),
(108,'Raju','HR',23445,'Noida');
SELECT * FROM employee;


/*
Window Functions
Functions that can perform calculations across rows 
without grouping.
function_name(expression)
OVER (PARTITION BY col ORDER BY col ASC/DESC)
*/

SELECT edesg,sum(esal) FROM employee GROUP BY edesg;

SELECT *,sum(esal) OVER (PARTITION BY edesg)
AS 'Total_Salary_By_Desg'FROM employee;

SELECT *,ROW_NUMBER() OVER (ORDER BY esal ASC)
FROM employee;

SELECT *,ROW_NUMBER() OVER (PARTITION BY edesg ORDER BY esal ASC)
FROM employee;

SELECT *,RANK() OVER (PARTITION BY edesg ORDER BY esal DESC) 
FROM employee;

SELECT *,DENSE_RANK() OVER (PARTITION BY edesg ORDER BY esal DESC) 
FROM employee;

# FIRST HIGHEST
SELECT *,RANK() OVER (ORDER BY esal DESC) FROM employee
LIMIT 1;

# SECOND HIGHEST
SELECT *,RANK() OVER (ORDER BY esal DESC) FROM employee
LIMIT 1 OFFSET 1;

# RUNNING Salary
SELECT *,SUM(esal) OVER (PARTITION BY edesg ORDER BY esal)
FROM employee;

# NTILE
SELECT *,NTILE(2) OVER(ORDER BY esal) FROM employee;

SELECT MAX(esal) FROM employee WHERE 
esal<(SELECT MAX(esal) FROM employee);