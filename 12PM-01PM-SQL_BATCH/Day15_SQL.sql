/*
# CTE (Common Table Expression)
It is use to create a Temporary Result Set we can use it for SELECT, INSERT,
DELETE or UPDATE queries.
Syntax:-

WITH cte_function_name AS (
	SQL Queries
    SELECT col1,col2,..
    FROM table_name
    WHERE condition
) SELECT * FROM cte_function_name;

*/
USE flipkart;
SHOW tables;
SELECT * FROM emp_log;
SELECT * FROM emp_log WHERE empadd='Delhi';

WITH delhi_emp AS (
SELECT empid,empname,empsal,empadd
FROM emp_log WHERE empadd='Delhi'
) SELECT * FROM delhi_emp;

SELECT * FROM emp_log;

WITH avg_sal AS (
SELECT avg(empsal) AS av_sal FROM emp_log
) SELECT * FROM emp_log,avg_sal WHERE empsal > av_sal; 
