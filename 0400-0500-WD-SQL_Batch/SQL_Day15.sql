/*
Window Functions
OVER()
window function perform calculation accross set of rows related to the 
current row without missing any other row grouping by GROUP BY clause

*/
USE flipkart;
SHOW TABLES;
SELECT * FROM employee;
SELECT sum(esal) FROM employee;
SELECT edesg,sum(esal) FROM employee GROUP BY edesg;

/*
<function_name>() OVER(PARTITION BY column_name ORDER BY col_name);
*/
SELECT * FROM employee;
SELECT *,sum(esal) OVER(PARTITION BY edesg) AS Total_Salary 
FROM employee;

SELECT *,ROW_NUMBER() OVER() AS "Row_number" FROM employee;
SELECT *,ROW_NUMBER() OVER(ORDER BY esal DESC) AS "RANK"
FROM employee;

INSERT INTO employee VALUE(114,'Ravi','HR',19198.02,'Noida',28);

# RANK

SELECT *,RANK() OVER(ORDER BY esal DESC) AS "RANK"
FROM employee;

# DENSE_RANK
SELECT *,DENSE_RANK() OVER(ORDER BY esal DESC) AS "RANK"
FROM employee;

# LAG (Get Previous value)
SELECT *,LAG(esal) OVER(ORDER BY esal DESC) AS "RANK"
FROM employee;

# LEAD (get Next value)
SELECT *,LEAD(esal) OVER(ORDER BY esal DESC) AS "RANK"
FROM employee;

# FIRST VALUE
SELECT *,FIRST_VALUE(esal) OVER(ORDER BY esal DESC) AS "Highest_Salary"
FROM employee;

# LAST VALUE
SELECT *,LAST_VALUE(esal) OVER(ORDER BY esal DESC 
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING )
AS "Smallest_Salary" FROM employee;

SELECT *,MIN(esal) OVER(ORDER BY esal DESC
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
FROM employee;

# NTILE
SELECT *,NTILE(3) OVER(ORDER BY esal DESC)
FROM employee;

# <> not equal to   ( !=  Not equal to )  
SELECT * FROM employee WHERE edesg != "HR";
 
USE store;
SHOW TABLES;
SELECT cid,cname FROM customer WHERE EXISTS (
SELECT * FROM orders WHERE customer.cid = orders.cid
);