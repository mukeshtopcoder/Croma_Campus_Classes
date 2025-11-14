/*
Window Functions 
OVER (PARTITION BY column_name ORDER BY column_name ASC/DESC)
*/
USE flipkart;
SELECT * FROM employee;
SELECT sum(esal) FROM employee;
SELECT edesg,sum(esal) FROM employee GROUP BY edesg;

SELECT *,sum(esal) OVER () FROM employee;
SELECT *,sum(esal) OVER (PARTITION BY edesg) FROM employee;
SELECT *,sum(esal) OVER (PARTITION BY edesg ORDER BY esal ASC)
FROM employee;

/*
CTE (Common Table Expression)
A CTE is a named temporary result set you define with "WITH" command
and can reference later in the same statement.
CTEs improve readability and let you reuse subqueries without
repeating code.

WITH temp_table_name AS (
-- SQL Query
) -- SQL Query;


*/


WITH top_desg AS (
SELECT edesg,sum(esal) AS 'Total_Salary'
FROM employee GROUP BY edesg HAVING sum(esal)>200000
) SELECT edesg FROM top_desg;

USE store;
SHOW TABLES;

WITH all_sales AS (
SELECT c.*,qty,p.* FROM customer c JOIN orders o
ON c.cid = o.cid JOIN product p ON o.pid = p.pid
) SELECT * FROM all_sales WHERE price>3000; 

