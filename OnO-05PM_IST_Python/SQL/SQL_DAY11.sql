/*
String funtions:-
length, lower , upper , concat , trim , replace , substring

Numeric Functions;-
abs , ceil , floor , mod , power , round

Date & Time Functions:- 
CURDATE , NOW , YEAR , MONTH , DATEDIFF , DATE_ADD , DATE_FORMAT

Aggregate Functions:-
count , sum , max , min , avg

Control flow:-
if , ifnull , case

*/

USE flipkart;
SHOW TABLES;
SELECT * FROM employee;

# String funtions:-
# length, lower , upper , concat , trim , replace , substring

SELECT ename, length(ename) FROM employee;    # count letters in word
SELECT ename , upper(ename), lower(ename) FROM employee;
SET @myname = "   MySQL       ";

SELECT @myname;
SELECT @myname , LTRIM(@myname) ,RTRIM(@myname) , TRIM(@myname);
SELECT @myname , REPLACE(@myname , 'y','Y');
SELECT CONCAT(ename," ",edesg) FROM employee;
SET @myname = "DATABASE";
SELECT LEFT(@myname,4);
SELECT RIGHT(@myname,4);

SELECT LEFT(ename,3) FROM employee;
SELECT ename,SUBSTRING(ename,3,2) FROM employee;

# Numeric Functions;-
# abs , ceil , floor , mod , power , round
SELECT * FROM employee;
SELECT esal, abs(esal) FROM employee;    # convert negative value to positive
SELECT CEIL(2.2);
SELECT CEIL(2.9);
SELECT FLOOR(2.2);
SELECT FLOOR(2.9);
SELECT ROUND(2.2);
SELECT ROUND(2.9);
SELECT ROUND(24.676,1);
SELECT POWER(5,3);
SELECT SQRT(16);
SELECT MOD(15,4);
SELECT RAND();     # print any value from 0 to 1
SELECT FLOOR(RAND()*100);


# Date & Time Functions:- 
# CURDATE , NOW , YEAR , MONTH , DATEDIFF , DATE_ADD , DATE_FORMAT
SELECT CURDATE();
SELECT CURRENT_TIME();
SELECT NOW();
SELECT YEAR(CURDATE());
SELECT MONTH(CURDATE());
SELECT DAY(CURDATE());

SELECT DATEDIFF('2025-11-24','1998-11-12');  # return number of days
SELECT DATEDIFF('2025-11-24','1998-11-12')/365;
SELECT DAYNAME('1998-11-12');
SELECT CURRENT_TIMESTAMP();


# Control FLow
# IF , IFNULL , CASE
SELECT * FROM employee;
# SELECT IF(condition , True , False);
SELECT esal,IF(esal>40000,"Good Salary","Average Salary") FROM employee;

SELECT * FROM employee;
SELECT IFNULL(eage,30) FROM employee;

SELECT esal,
CASE 
	WHEN esal<=30000 THEN 'BELOW_AVERAGE'
    WHEN esal<=50000 THEN 'AVERAGE'
    ELSE 'ABOVE_AVERAGE'
END AS Salary_Status
FROM employee;

# WINDOW , CTE