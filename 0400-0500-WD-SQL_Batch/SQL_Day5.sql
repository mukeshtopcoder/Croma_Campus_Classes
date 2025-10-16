/*
CLAUSES
Aggregate Functions
sum , avg , max , min , count
*/
CREATE DATABASE amazon;
USE amazon;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT , 
ename VARCHAR(100) NOT NULL ,
eadd VARCHAR(50) NOT NULL ,
esal DECIMAL(8,2) NOT NULL ,
edesg VARCHAR(100) NOT NULL
);
INSERT INTO employee VALUE(101,'Raman Singh','Noida',27330,'IT');
INSERT INTO employee(ename,eadd,esal,edesg) VALUES
('Rahul Sharma','Delhi',68460,'HR'),
('Siya Singh','Noida',37490,'HR'),
('Ramandeep','Delhi',86870,'IT'),
('Umesh Singh','GZB',73580,'IT');

SELECT * FROM employee;
# Aggregate functions sum , count , max , min , avg
SELECT sum(esal) FROM employee;
SELECT max(esal) FROM employee;
SELECT min(esal) FROM employee;
SELECT avg(esal) FROM employee;
SELECT count(*) FROM employee;

# CLAUSES
# WHERE
SELECT * FROM employee;
SELECT * FROM employee WHERE eadd='Noida';
SELECT * FROM employee WHERE eadd='Delhi';
SELECT * FROM employee WHERE esal>50000;
SELECT * FROM employee WHERE esal<50000;
# AND - OR
SELECT * FROM employee WHERE eadd='Noida' AND esal>30000;
SELECT * FROM employee WHERE eadd='Delhi' OR esal>70000;
# AND -> true if both conditions are true
# OR -> true if any condition is true
SELECT * FROM employee WHERE esal>40000 AND esal<70000;

# BETWEEN
SELECT * FROM employee WHERE esal BETWEEN 40000 AND 70000;

# ORDER BY
SELECT * FROM employee;
SELECT * FROM employee ORDER BY esal ASC;
SELECT * FROM employee ORDER BY esal DESC;
SELECT * FROM employee ORDER BY ename ASC;

# LIMIT 
SELECT * FROM employee;
SELECT * FROM employee LIMIT 2;
# TOP TWO EARNERS 
SELECT * FROM employee ORDER BY esal DESC LIMIT 2;

# HIGHEST SALARY PERSON
SELECT * FROM employee ORDER BY esal DESC LIMIT 1;

# 2nd HIGHEST SALARY PERSON
# OFFSET
SELECT * FROM employee ORDER BY esal DESC LIMIT 1 OFFSET 1;

# 3rd HIGHEST SALARY PERSON
# OFFSET
SELECT * FROM employee ORDER BY esal DESC LIMIT 1 OFFSET 2;

# GROUP BY
SELECT sum(esal) FROM employee;
SELECT sum(esal) FROM employee GROUP BY edesg;
SELECT edesg,sum(esal) FROM employee GROUP BY edesg;

# HAVING
SELECT edesg,sum(esal) FROM employee GROUP BY edesg
HAVING sum(esal)>150000;
SELECT edesg,avg(esal) FROM employee GROUP BY edesg;

SELECT * FROM employee WHERE edesg='IT';