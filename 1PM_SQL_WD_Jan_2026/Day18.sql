/*
# Window Function

*/
USE amazon;
SHOW TABLES;
SELECT * FROM employee;

SELECT SUM(esal) FROM employee;
SELECT eadd , SUM(esal) FROM employee GROUP BY eadd;

# Syntax:-
/*
SELECT col_name , window_function() OVER (
PARTITION BY col_name ORDER BY col_name 
) FROM table_name;
*/

SELECT * FROM employee;
# ROW_NUMBER()
SELECT *,ROW_NUMBER() OVER() FROM employee;
SELECT *,ROW_NUMBER() OVER(ORDER BY esal DESC) FROM employee;
SELECT *,ROW_NUMBER() OVER(ORDER BY esal ASC) FROM employee;

SELECT *,ROW_NUMBER() OVER
(PARTITION BY eadd ORDER BY esal DESC)
FROM employee;


# RANK
SELECT *,RANK() OVER() FROM employee;
SELECT *,RANK() OVER(ORDER BY esal DESC) FROM employee;
# it skip the rank number if is there any tie

# DENSE_RANK()
SELECT *,DENSE_RANK() OVER() FROM employee;
SELECT *,DENSE_RANK() OVER(ORDER BY esal DESC) FROM employee;
# it do not skip the rank number if is there any tie

# NTILE()
SELECT *,NTILE(2) OVER() FROM employee;
SELECT *,NTILE(2) OVER(ORDER BY esal DESC) FROM employee;
SELECT *,NTILE(3) OVER(ORDER BY esal DESC) FROM employee;
SELECT *,NTILE(4) OVER(ORDER BY esal DESC) FROM employee;


SELECT sum(esal) FROM employee;

# SUM()
SELECT *,SUM(esal) OVER() FROM employee;
SELECT *,AVG(esal) OVER() FROM employee;
SELECT *,COUNT(esal) OVER() FROM employee;

SELECT *,SUM(esal) OVER(PARTITION BY eadd) FROM employee;
SELECT *,SUM(esal) OVER(PARTITION BY eadd
ORDER BY esal DESC) FROM employee;

# LAG   (Print Previous Value)
SELECT *,LAG(esal) OVER() FROM employee;

# LEAD   (Print Next Value)
SELECT *,LEAD(esal) OVER() FROM employee;

# SUB QUERY
# FIND HIGHEST SALARY
SELECT MAX(esal) FROM employee;
SELECT MAX(esal) FROM employee WHERE esal<105300;
# Second Highest USING SUBQUERY
SELECT MAX(esal) FROM employee 
WHERE esal<(SELECT MAX(esal) FROM employee);

SELECT * FROM employee ORDER BY esal DESC LIMIT 1;
SELECT * FROM employee ORDER BY esal DESC LIMIT 1 OFFSET 1;

# FIND 2nd Highest Salary using window functions

SELECT * FROM (
SELECT *,DENSE_RANK() OVER(ORDER BY esal DESC) AS rnk
FROM employee ) AS t
WHERE rnk=2 LIMIT 1;
