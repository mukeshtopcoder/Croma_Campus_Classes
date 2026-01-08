USE college;
SHOW TABLES;
SELECT * FROM employee;

SELECT eid,ename,eadd FROM employee;

CREATE VIEW emp_table AS
SELECT eid,ename,eadd FROM employee;

SELECT * FROM emp_table;
SHOW TABLES;

ALTER VIEW emp_table AS
SELECT eid,ename FROM employee;

SELECT * FROM emp_table;

DROP VIEW emp_table;


# RECURSIVE CTE
# refers to itself

# Write a recursive CTE to display numbers from 1 to 10.

WITH RECURSIVE numbers AS (
    SELECT 1 AS num
    UNION ALL
	-- Recursive Part
    SELECT num+1 FROM numbers
    WHERE num<10  
) SELECT * FROM numbers;

# Use a recursive CTE to generate a calendar of 
# dates between '2024-01-01' and '2024-01-10'.

WITH RECURSIVE print_date AS (
	SELECT DATE('2024-01-01') AS date_
    UNION ALL
    SELECT date_ + INTERVAL 1 DAY FROM print_date
    WHERE date_ < "2024-01-10"
) SELECT * FROM print_date;