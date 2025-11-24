/*
MySQL Clauses
WHERE , ORDER BY , HAVING , GROUP BY , LIMIT , OFFSET , 
DISTINCT , BETWEEN , IN , IS NULL , IS NOT NULL
AND , OR 

Aggregate Functions
SUM , MAX , MIN , COUNT , AVG
*/
USE flipkart;
SHOW TABLES;
SELECT * FROM employee;

SELECT sum(esal) FROM employee;
SELECT max(esal) FROM employee;
SELECT min(esal) FROM employee;
SELECT avg(esal) FROM employee;
SELECT count(eid) AS Number_of_Employees FROM employee;

SELECT * FROM employee;
# SELECT * FROM employee WHERE condition;
SELECT * FROM employee WHERE edesg='HR';
SELECT * FROM employee WHERE esal>50000;
SELECT * FROM employee WHERE eage>30;

SELECT * FROM employee WHERE esal>50000 AND eadd='Noida';
SELECT * FROM employee WHERE esal>50000 OR eadd='Noida';

SELECT * FROM employee WHERE eadd!='Delhi';
SELECT * FROM employee WHERE NOT eadd='Delhi';

SELECT * FROM employee WHERE NOT (esal>50000 OR eadd='Noida');

SELECT * FROM employee;
SELECT * FROM employee ORDER BY esal;
SELECT * FROM employee ORDER BY esal ASC;
SELECT * FROM employee ORDER BY esal DESC;

SELECT * FROM employee WHERE eadd='Delhi'
ORDER BY esal DESC;

SELECT * FROM employee WHERE eadd='Delhi' AND esal>50000
ORDER BY esal DESC;

# GROUP BY
SELECT sum(esal) FROM employee GROUP BY eadd;
SELECT eadd,sum(esal) FROM employee GROUP BY eadd;
SELECT eadd,max(esal) FROM employee GROUP BY eadd;
SELECT eadd,count(eid) FROM employee GROUP BY eadd;

SELECT eadd,sum(esal) FROM employee GROUP BY eadd
HAVING sum(esal)>100000;

SELECT * FROM employee;
SELECT * FROM employee WHERE esal>50000;
SELECT * FROM employee HAVING esal>50000;


SELECT * FROM employee;
SELECT * FROM employee LIMIT 3;
SELECT * FROM employee ORDER BY esal DESC;
SELECT * FROM employee ORDER BY esal DESC LIMIT 2;
SELECT * FROM employee ORDER BY esal DESC LIMIT 1;

# SECOND HIGHEST PERSON/SALARY  USING OFFSET
SELECT * FROM employee ORDER BY esal DESC LIMIT 1 OFFSET 1;
# THIRD HIGHEST PERSON/SALARY  USING OFFSET
SELECT * FROM employee ORDER BY esal DESC LIMIT 1 OFFSET 2;
SELECT esal FROM employee ORDER BY esal DESC LIMIT 1 OFFSET 2;

SELECT DISTINCT edesg FROM employee;
SELECT count(DISTINCT edesg) FROM employee;
SELECT count(DISTINCT eadd) FROM employee;
SELECT DISTINCT eadd FROM employee;

SELECT COUNT(NULL); # always return 0
# COUNT ONLY null
SELECT sum(IF(eid IS NULL , 1 , 0)) FROM employee;

# IF( condition , True , False )
# count employee who is 30+ age
SELECT * FROM employee;
SELECT SUM(IF(eage>30,1,0)) FROM employee;
SELECT count(eid) FROM employee WHERE eage>30;

# COUNT NULL VALUES IN eage COLUMN
SELECT count(eid) FROM employee WHERE eage IS NULL;

# 5th Highest
SELECT * FROM employee ORDER BY esal DESC LIMIT 1 OFFSET 4;

SELECT * FROM employee WHERE esal>30000;
SELECT * FROM employee WHERE esal<50000;
SELECT * FROM employee WHERE esal>30000 AND esal<50000;
SELECT * FROM employee WHERE esal BETWEEN 30000 AND 50000;

SELECT * FROM employee WHERE eadd='Noida' OR eadd='Delhi';
SELECT * FROM employee WHERE eadd IN ('Noida','Delhi','Nanital');

SELECT DISTINCT column_name --;
-- SELECT * FROM employee where /group/having order;

SELECT * FROM employee WHERE eadd='Noida' ORDER BY esal DESC;
