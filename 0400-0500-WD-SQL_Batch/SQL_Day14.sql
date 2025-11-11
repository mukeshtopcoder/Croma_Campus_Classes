/*
MySQL Functions
Aggregate Functions
SUM , AVG , MAX , MIN , COUNT

String Functions
length, upper , lower , concat , substring , replace, trim

USE flipkart;
SHOW TABLES;
SELECT ename FROM employee;
SELECT ename,upper(ename) FROM employee;
SELECT ename,length(ename) FROM employee;
SELECT ename,lower(ename) FROM employee;
SELECT ename,concat(ename," ",eadd) FROM employee;
SELECT ename,substring(ename,3) FROM employee;
SELECT eadd,REPLACE(eadd,'Noida','Nanital') FROM employee;
SELECT ename,trim(ename) FROM employee;

Numerical Functions
ABS , ROUND , CEIL , FLOOR , MOD , POWER

SELECT esal,abs(esal) FROM employee;  # it convert negative value to positive\
SELECT esal,round(esal) FROM employee;
SELECT esal,CEIL(esal) FROM employee;
SELECT esal,FLOOR(esal) FROM employee;
SELECT mod(11,4); # modulus (calculate remainder)
SELECT power(5,3); # 5*5*5
SELECT *,floor(esal*0.10) AS Bonus FROM employee;

Date & Time Functions:-
NOW, CURDATE, CURTIME, DATE_FORMAT, DATEDIFF, YEAR,MONTH,DAY,
CURRENT_TIMESTAMP

SELECT NOW();
SELECT CURRENT_TIMESTAMP();
SELECT CURDATE();
SELECT CURTIME();
SELECT DATE_FORMAT(CURDATE(),"%w"); # %d %D %y %Y %w %W %m %M
SELECT DATE_FORMAT(CURDATE(),"%W");
SELECT DATEDIFF(CURDATE(),'1998-12-11')/365;
SELECT YEAR(CURDATE());
SELECT MONTH(CURDATE());
SELECT DAY(CURDATE());


NEXT-> Window , CTE
*/

SELECT FLOOR(10/3);

SELECT DATE_ADD(CURDATE() , INTERVAL 10 DAY);
SELECT DATE_ADD(CURDATE() , INTERVAL 2 MONTH);
