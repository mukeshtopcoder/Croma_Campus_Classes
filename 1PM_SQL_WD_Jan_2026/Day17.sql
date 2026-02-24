/*
MySQL Functions
*/
USE amazon;
SHOW TABLES;
SELECT * FROM employee;

SELECT ename FROM employee;
# STRING FUNCTIONS
# upper , lower , length , concat , substring

SELECT ename FROM employee;
SELECT UPPER(ename) FROM employee;
SELECT LOWER(ename) FROM employee;
SELECT LENGTH(ename) FROM employee;
SELECT CONCAT(ename,eadd) FROM employee;
SELECT CONCAT(ename," => ",eadd) FROM employee;
SELECT SUBSTRING(ename,1,5) FROM employee;


# MATHEMATICAL FORMULA
# ROUND , CEIL , FLOOR , MOD , ABS
SELECT esal FROM employee;
UPDATE employee SET esal=esal+esal*0.17;
SELECT esal FROM employee;
SELECT esal, ROUND(esal) FROM employee;
SELECT esal, ROUND(esal), CEIL(esal) FROM employee;
SELECT esal, ROUND(esal), CEIL(esal), FLOOR(esal) FROM employee;
SELECT esal , ABS(esal) FROM employee; # will convert negative value to positive
SELECT MOD(11,4); # MODULUS (CALCULATE REMAINDER)
SELECT esal , MOD(esal , 10000) FROM employee;

# DATE FUCTIONS 
# NOW , TODAY , CURRENT_TIMESTAMP , CURTIME , CURDATE 
# YEAR , MONTH , DAY , DATEDIFF
SELECT  NOW(); 
SELECT  CURDATE(); 
SELECT CURTIME();
SELECT current_time();
SELECT current_timestamp();

SELECT CURDATE();
SELECT YEAR('2026-02-24');
SELECT MONTH('2026-02-24');
SELECT DAY('2026-02-24');
SELECT DATEDIFF( CURDATE() , '1998-11-12' );
SELECT DATEDIFF( CURDATE() , '1998-11-12' )/365;

# AGGREAGTE FUNCTIONS
# SUM , AVG , MAX , MIN , COUNT , COUNTA

# CONTROL STATEMENT FUNCTIONS
# IF , CASE
SELECT ename FROM employee;
# PRINT SALARY LABEL HIGH IF SALARY IS ABOVE 80000 OTHERWISE LOW
SELECT ename FROM employee;
SELECT ename,esal,'HIGH' AS Salary_Status FROM employee;

SELECT ename,esal,
IF (esal>80000, 'HIGH' , 'LOW') AS Salary_Status
FROM employee;


# PRINT SALARY LABEL HIGH IF SALARY IS ABOVE 80000
# AND AVERAGE IF ABOVE 50000 OTHERWISE LOW
SELECT ename,esal,
	CASE
		WHEN esal>=80000 THEN 'HIGH'
        WHEN esal>=50000 THEN 'AVERAGE'
        ELSE 'LOW'
	END AS SalaryStatus
FROM employee;

SELECT * FROM employee;
SELECT ename,eadd FROM employee;
SELECT ename,eadd,REPLACE(eadd,'Delhi','Delhi NCR') FROM employee;
