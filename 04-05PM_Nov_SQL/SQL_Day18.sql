/*
SELECT * FROM employees AS e WHERE salary = 
(SELECT MAX(salary) FROM employees WHERE department = e.department)
OR salary =
(SELECT MIN(salary) FROM employees WHERE department = e.department);
*/

USE school;
SHOW TABLES;
SELECT * FROM student;

DELIMITER //
CREATE PROCEDURE update_salary_10per(INOUT sal DECIMAL(8,2))
BEGIN 
	SET sal = sal+sal*10/100;
END // DELIMITER ;
SET @salary = 40000;
CALL update_salary_10per(@salary);

SELECT @salary;


SELECT * FROM (
SELECT employee, sale_amount, max(sale_amount)
OVER ( PARTITION BY employee ) AS Highest_sale
FROM sales) AS t
WHERE sale_amount = Highest_sale;

