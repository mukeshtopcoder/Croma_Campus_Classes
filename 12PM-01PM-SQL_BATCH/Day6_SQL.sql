# Functions
# Aggreagte Functions
# sum , max , min , avg , count
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
# Aggregate Functions   sum , max , min , count , avg
SELECT sum(salary) FROM employee;
SELECT max(salary) FROM employee;
SELECT min(salary) FROM employee;
SELECT avg(salary) FROM employee;
SELECT count(eid) FROM employee;

# WHERE
SELECT * FROM employee WHERE salary>50000;
# ORDER BY
SELECT * FROM employee ORDER BY salary DESC;
SELECT * FROM employee ORDER BY salary ASC;

# LIMIT
SELECT * FROM employee ORDER BY salary DESC LIMIT 1;
SELECT * FROM employee ORDER BY salary DESC LIMIT 2;

# OFFSET

# 2nd Highest Salary
SELECT * FROM employee ORDER BY salary 
DESC LIMIT 1 OFFSET 1;
# 3rd highest Salary
SELECT * FROM employee ORDER BY salary 
DESC LIMIT 1 OFFSET 2;

# GROUP BY 
SELECT sum(salary) FROM employee;
SELECT depart,sum(salary) FROM employee 
GROUP BY depart;
SELECT eadd,sum(salary) FROM employee 
GROUP BY eadd;


# Finding Minimum or Maximum salary department wise.
SELECT depart,min(salary) FROM employee 
GROUP BY depart;

SELECT * FROM employee WHERE depart='HR'
ORDER BY salary DESC LIMIT 1;

# SUB-QUERIES
SELECT max(salary) FROM employee 
WHERE salary< (SELECT max(salary) FROM employee);