/*
WINDOW Functions
*/
USE flipkart;
SHOW TABLES;
SELECT * FROM employee;

SELECT sum(esal) FROM employee;
SELECT sum(esal) FROM employee GROUP BY edesg;
SELECT edesg,sum(esal) FROM employee GROUP BY edesg;

# WINDOW functions
# Ranking , Aggregate , Value , Running Total

SELECT *,sum(esal) OVER() FROM employee ;
SELECT *,sum(esal) OVER(PARTITION BY edesg)
FROM employee ;

SELECT *,max(esal) OVER(PARTITION BY edesg)
FROM employee ;

SELECT *,ROW_NUMBER() OVER() FROM employee;
SELECT *,ROW_NUMBER() OVER(PARTITION BY edesg)
FROM employee;

SELECT *,RANK() OVER() FROM employee;
SELECT *,RANK() OVER(ORDER BY esal DESC)
FROM employee;
# without skipping
SELECT *,DENSE_RANK() OVER(ORDER BY esal DESC)
FROM employee;

SELECT * FROM employee;
# LEAD  (next value)
SELECT *,LEAD(esal) OVER() FROM employee;
SELECT *,LEAD(esal) OVER(ORDER BY esal)
FROM employee;

# LAG (previous value)
SELECT *,LAG(esal) OVER() FROM employee;
SELECT *,LAG(esal) OVER(ORDER BY esal DESC)
FROM employee;


# Running / Moving Average/Total
SELECT ename,esal,sum(esal) OVER(ORDER BY esal DESC)
AS Moving_Total FROM employee;

SELECT *,MAX(esal) OVER(PARTITION BY edesg ORDER BY esal DESC)
FROM employee;

# CTE (Common Table Expression)
# CTE is a temporary result set that you can reference 
# within a DML commands

WITH any_name AS (
	SELECT * FROM employee
)
SELECT * FROM any_name;

WITH noida_emp AS (
	SELECT * FROM employee WHERE eadd='Noida'
)
SELECT * FROM noida_emp ORDER BY esal DESC;

WITH emp_bonus AS (
	SELECT ename,esal*0.10 AS Bonus FROM employee
) SELECT * FROM emp_bonus;

WITH hig_sal AS (
	SELECT *,DENSE_RANK() OVER(ORDER BY esal DESC)
    AS ranks FROM employee
) SELECT * FROM hig_sal WHERE ranks=1; 