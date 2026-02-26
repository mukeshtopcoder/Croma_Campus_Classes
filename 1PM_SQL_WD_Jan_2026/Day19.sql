/*
CTE , VIEW 
CTE:- Common Table Expression
Syntax:-

WITH cte_table_name AS (
	SQL Query
) SQL query using that cte_table_name
*/

USE amazon;
SHOW TABLES;
SELECT * FROM employee;


SELECT * FROM employee WHERE
esal>80000;

# CREATE A CTE TABLE
WITH myTable AS (
SELECT eid,ename,eadd FROM employee WHERE
esal>80000 ) SELECT * FROM myTable;

# SECOND HIGHEST SALARY EMPLOYEE NAME AND ADDRESS
# USING CTE
WITH mytable AS (
SELECT *,DENSE_RANK() OVER(ORDER BY esal DESC) AS rnk
FROM employee ) SELECT ename,eadd FROM mytable WHERE rnk=2;

WITH temp AS (
SELECT ename,eadd,DENSE_RANK() OVER(ORDER BY esal DESC)
AS rnk FROM employee ) SELECT * FROM temp WHERE rnk=2; 


USE store;

WITH newTable AS (
SELECT c.* , pname,price,qty FROM customer c
JOIN orders o
ON c.cid = o.cid
JOIN product p
ON p.pid = o.pid )
SELECT *,price*qty AS Total FROM newTable;

# VIEW :- View is a temporay table which stores only query
# not data, it builds data at the runtime
USE amazon;
SELECT * FROM employee;
CREATE VIEW emp_detail AS
SELECT eid,ename,eadd FROM employee;


SELECT * FROM emp_detail;
SHOW TABLES;

/*
				CTE						VIEW
Storage			Temporary				Stored in DB
Scope	        Single Query    		Reuseable
Performance     Calcuated Every Time	Stored Query
Best for		Complex Logic			Reuseable Query

*/ 