# ALL DATA TYPES PDF
CREATE DATABASE flipkart;
USE flipkart;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT ,
ename VARCHAR(40) NOT NULL , 
esal DECIMAL(8,2) NOT NULL , 
edesg VARCHAR(20) NOT NULL , 
eadd VARCHAR(20) NOT NULL
);
INSERT INTO employee VALUE (101,'Rahul',34786.56,'IT','Noida');
INSERT INTO employee(ename,esal,edesg,eadd) VALUES
('Raman',43254.45,'HR','Delhi'),
('Baman',67433.45,'HR','Noida'),
('Suman',34765.66,'IT','Noida'),
('Riya',47555.43,'IT','Delhi');

SELECT * FROM employee;
# SUM , MAX , MIN , AVG , count 
SELECT sum(esal) FROM employee;
SELECT max(esal) FROM employee;
SELECT min(esal) FROM employee;
SELECT avg(esal) FROM employee;
SELECT count(esal) FROM employee;

# ORDER BY
SELECT * FROM employee;
SELECT * FROM employee ORDER BY esal ASC;
SELECT * FROM employee ORDER BY esal DESC;

# GROUP BY
SELECT edesg,sum(esal) FROM employee GROUP BY edesg;
SELECT eadd,sum(esal) FROM employee GROUP BY eadd;
SELECT eadd,edesg,sum(esal) FROM employee GROUP BY eadd,edesg;

# HAVING
SELECT edesg,sum(esal) FROM employee GROUP BY edesg
HAVING sum(esal)>115000;
SELECT * FROM employee WHERE edesg='IT';

# LIMIT
SELECT * FROM employee;
SELECT * FROM employee LIMIT 2;
# Highest salary of an employee
SELECT * FROM employee ORDER BY esal DESC LIMIT 1;

# OFFSET
SELECT * FROM employee LIMIT 2 OFFSET 2;
# 2nd Highest Salary
SELECT * FROM employee ORDER BY esal DESC LIMIT 1 OFFSET 1;
# 3rd Highest Salary
SELECT * FROM employee ORDER BY esal DESC LIMIT 1 OFFSET 2;

# WILDCARDS % _  (LIKE Clause)
SELECT * FROM employee;
INSERT INTO employee(ename,esal,edesg,eadd) VALUES
('Yogesh',38768,'IT','Nanital'),
('Yaman',38758,'IT','Nagpur');

SELECT * FROM employee WHERE eadd='Noida';
SELECT * FROM employee WHERE eadd LIKE "N%";
SELECT * FROM employee WHERE eadd LIKE "%i%";
SELECT * FROM employee WHERE eadd LIKE "%a";

SELECT * FROM employee WHERE eadd LIKE "N__i%";
SELECT * FROM employee WHERE eadd LIKE "N_i%";


SELECT * FROM employee;
# JOINS