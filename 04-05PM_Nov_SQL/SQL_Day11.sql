/*
MySQL Functions
STRING Functions
CONCAT , LENGTH , UPPER , LOWER , TRIM , REPLACE , SUBSTRING

*/
USE flipkart;
SHOW TABLES;
SELECT * FROM employee;
SELECT CONCAT(ename,edesg) FROM employee;
SELECT CONCAT(ename," ",edesg) FROM employee;
SELECT ename,LENGTH(ename) FROM employee;
SELECT ename , UPPER(ename) FROM employee;
SELECT ename , LOWER(ename) FROM employee;
SELECT ename , TRIM(ename) FROM employee;
SET @myname = "      aman   kumar        ";
SELECT @myname,TRIM(@myname);

SELECT ename FROM employee;
SELECT ename,REPLACE(ename,'n','NN') FROM employee;

SET @str = 'I LOVE SQL';
SELECT @str , REPLACE(@str,'SQL','MySQL');

SELECT ename FROM employee;
SELECT ename,SUBSTRING(ename,1,3) FROM employee;
SELECT ename,UPPER(SUBSTRING(ename,1,3)) FROM employee;

/*
MATHEMATICAL/NUMERICAL Functions
ABS , ROUND , CEIL , FLOOR , POWER , SQRT , MOD

*/
SELECT * FROM employee;
SELECT esal FROM employee;
SELECT esal , ABS(esal) FROM employee;

SELECT esal,ROUND(esal) FROM employee;
SELECT esal,CEIL(esal) FROM employee;
SELECT esal,FLOOR(esal) FROM employee;

SELECT POWER(5,3); # 5X5X5
SELECT SQRT(16);
SELECT MOD(18,4);    # it is use to calculate the remainder

/*
Date And Time Functions
NOW , CURRENT_TIMESTAMP , CURRENT_DATE , DATE_ADD , DATEDIFF
*/
SELECT CURRENT_DATE();
SELECT CURRENT_TIME();
SELECT CURRENT_TIMESTAMP();
SELECT NOW();
SELECT CURDATE();
SELECT CURTIME();
SELECT DATEDIFF('2025-12-2','2025-10-13');
SELECT DATEDIFF(CURDATE(),'1998-11-12');
SELECT DATEDIFF(CURDATE(),'1998-11-12')/365;
SELECT FLOOR(DATEDIFF(CURDATE(),'1998-11-12')/365);

SELECT DATE_ADD(CURDATE() ,  INTERVAL 10 DAY);
SELECT DATE_ADD(CURDATE() ,  INTERVAL 3 MONTH);
SELECT DATE_ADD(CURDATE() ,  INTERVAL 2 YEAR);
SELECT DATE_ADD(CURDATE() ,  INTERVAL 2 YEAR);

# 2 YEAR 3 MONTH 5 DAY
SELECT DATE_ADD(DATE_ADD(DATE_ADD(CURDATE() ,
INTERVAL 2 YEAR),INTERVAL 3 MONTH),INTERVAL 5 DAY);

/*
AGGREGATE Functions
SUM , MAX , MIN , AVERAGE , COUNT
*/

/*
CONDITIONAL Formula
IF ( condition ,  true ,  false )
CASE (Alternative of Nested IF)
*/
SELECT esal FROM employee;
# IF Example
SELECT esal , IF(esal>0,"Profit","Loss") FROM employee;
# Nested IF Example
SELECT esal,IF(esal<0,"Loss",IF(esal<10000,"Average_Profit",
"High_Profit")) FROM employee;

SELECT esal , 
CASE 
	WHEN esal<0 THEN 'Loss'
    WHEN esal<10000 THEN 'AVERAGE_PROFIT'
    ELSE 'HIGH_PROFIT'
END
AS Profit_Status FROM employee;