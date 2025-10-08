CREATE DATABASE amazon;
USE amazon;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT , 
ename VARCHAR(100) NOT NULL , 
eadd VARCHAR(100) NOT NULL , 
depart VARCHAR(100) NOT NULL , 
salary DECIMAL(8,2) NOT NULL
);
INSERT INTO employee VALUES
(101,'Raman Singh','Amroha','IT',72546),
(102,'Shubham','MBD','HR',83640),
(103,'Harish','Noida','IT',88200),
(104,'Mohan','Delhi','HR',35340),
(105,'Riya','Noida','HR',54700),
(106,'Simran','Delhi','IT',12300);

SELECT * FROM employee;
# AGGREAGTE FUNCTIONS
# SUM , AVG , MAX , MIN , COUNT
SELECT sum(salary) FROM employee;
SELECT max(salary) FROM employee;
SELECT min(salary) FROM employee;
SELECT avg(salary) FROM employee;
SELECT count(salary) FROM employee;

# WHERE CLAUSE
SELECT * FROM employee;
SELECT * FROM employee WHERE depart='IT';
SELECT * FROM employee WHERE eadd='Noida';

# GROUP BY
SELECT eadd,sum(salary) FROM employee GROUP BY eadd;
SELECT depart,sum(salary) FROM employee GROUP BY depart;

# HAVING
SELECT eadd,sum(salary) FROM employee GROUP BY eadd
HAVING sum(salary)>80000;

# LIMIT , OFFSET , ORDER BY
# 2nd Highest Salary
SELECT * FROM employee ORDER BY salary DESC;
SELECT * FROM employee ORDER BY salary DESC
LIMIT 1;
SELECT * FROM employee ORDER BY salary DESC
LIMIT 1 OFFSET 1;



# Logical Clauses
# AND , OR
# AND :-  return true if both  conditions are true
SELECT * FROM employee WHERE eadd='Noida';
SELECT * FROM employee WHERE depart='IT';
SELECT * FROM employee WHERE depart='HR' AND eadd='Delhi';
SELECT * FROM employee WHERE depart='HR' AND eadd='Delhi' AND salary>30000;
# OR :- return true if any condition is true
SELECT * FROM employee WHERE depart='HR' OR eadd='Delhi';

# BETWEEN
SELECT * FROM employee WHERE salary>30000 AND salary<39000;
SELECT * FROM employee WHERE salary BETWEEN 30000 AND 39000;

INSERT INTO employee VALUES
(107,'Baman Singh','Nagpur','IT',37346),
(108,'Sameer','Nanital','HR',38654),
(109,'Tanu','Dehradun','IT',37547);

# WILDCARDS   => LIKE Clause  (Operator % _)
SELECT * FROM employee;
SELECT * FROM employee WHERE eadd='Noida';
SELECT * FROM employee WHERE eadd LIKE "N%"; 
SELECT * FROM employee WHERE eadd LIKE "Na%"; 
SELECT * FROM employee WHERE eadd LIKE "%a%"; 

# _
SELECT * FROM employee WHERE eadd LIKE "_a%";
SELECT * FROM employee WHERE eadd LIKE "_e%";
SELECT * FROM employee WHERE eadd LIKE "__h%";

# Aggregate SUM MAX MIN COUNT AVG
# STRING functions length , upper = ucase , lower = lcase,
# concat , substring , left , right , reverse etc
SELECT * FROM employee;
SELECT ename, LENGTH(ename) FROM employee;
SELECT ename, UPPER(ename) FROM employee;
SELECT ename, LOWER(ename) FROM employee;
SELECT CONCAT(ename," ",eadd) FROM employee;
SELECT CONCAT("Name  :-> ",ename," | Address :-> ",eadd) FROM employee;
SELECT left(eadd,3) FROM employee;
SELECT UPPER(left(eadd,3)) FROM employee;
SELECT RIGHT(eadd,3) FROM employee;
SELECT eadd,SUBSTRING(eadd,2,3) FROM employee;
SELECT eadd , REVERSE(eadd) FROM employee;


# Date And Time Functions
# current_time , current_date , current_timestamp = now , 
# YEAR , MONTH , DAY , DAYNAME , DATEDIFF , TIMESTAMPDIFF
SELECT CURRENT_TIME();
SELECT CURRENT_DATE();
SELECT CURRENT_TIMESTAMP();
SELECT NOW();
SELECT YEAR(NOW());
SELECT MONTH(NOW());
SELECT DAY(NOW());
SELECT DAYNAME(NOW());
SELECT DATEDIFF(CURRENT_DATE(),'1998-11-12');
SELECT TIMESTAMPDIFF(YEAR,'1998-11-12',NOW());

