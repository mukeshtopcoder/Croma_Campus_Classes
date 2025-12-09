
USE flipkart;
SHOW TABLES;
SELECT * FROM employee;
SELECT sum(esal) FROM employee;
SELECT edesg,sum(esal) FROM employee GROUP BY edesg;

/*
Window Functions
Syntax
SELECT *,agg/incr OVER () FROM table_name;
*/
SELECT *,sum(esal) OVER () FROM employee;
SELECT *,sum(esal) OVER (PARTITION BY edesg) FROM employee;

SELECT *,ROW_NUMBER() OVER () FROM employee ORDER BY esal DESC;

SELECT *,RANK() OVER (ORDER BY esal DESC) FROM employee;

SELECT *,DENSE_RANK() OVER (ORDER BY esal DESC) FROM employee;

SELECT *,ROW_NUMBER() OVER ()
AS total FROM employee;

SELECT *,ROW_NUMBER() OVER (PARTITION BY edesg)
AS total FROM employee;

SELECT *,ROW_NUMBER() OVER (PARTITION BY edesg ORDER BY esal DESC)
AS total FROM employee;

SELECT *,SUM(esal) OVER (ORDER BY esal) FROM employee;

SELECT *,AVG(esal) OVER () FROM employee;

# LAG , LEAD
SELECT * FROM employee;
SELECT *,LAG(esal) OVER () FROM employee;
SELECT *,LAG(esal) OVER (PARTITION BY edesg) FROM employee;

# LEAD 
SELECT *,LEAD(esal) OVER () FROM employee;
SELECT *,LEAD(esal) OVER (PARTITION BY edesg) FROM employee;


# CTE Functions (Common Table Expression)
WITH my_table AS (
SELECT eid,ename,esal FROM employee
) SELECT * FROM my_table WHERE esal>30000;

# Second Highest Salary
WITH my_table AS (
SELECT *,DENSE_RANK() OVER (ORDER BY esal DESC) AS rnk FROM employee )
SELECT * FROM my_table WHERE rnk=2;


SET @mysalary = 30000;
SELECT @mysalary; 
# VARIABLE => VARY(CHANGE) + ABLE
SET @mysalary = 90000;
SELECT @mysalary;
SELECT * FROM employee WHERE esal > @mysalary; 