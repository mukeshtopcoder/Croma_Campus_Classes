/*
Clauses
*/
CREATE DATABASE amazon;
USE amazon;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT , 
ename VARCHAR(30) NOT NULL ,
mobile VARCHAR(15) UNIQUE ,
esal DECIMAL(8,2) DEFAULT 0.0 , 
edesg VARCHAR(20) NOT NULL , 
eadd VARCHAR(20) NOT NULL
);

INSERT INTO employee 
VALUE(109,'Kamal Singh','+918632345546',87629.34,'IT','Noida');

SELECT * FROM employee;

INSERT INTO employee(ename , mobile , esal , edesg , eadd) VALUES
('Aman Kumar','+9186348759',75287.34,'IT','Delhi'),
('Baman Kumar','+9186348435',27354.34,'HR','Noida'),
('Riya Singh','+9186348754',34532.34,'HR','GZB'),
('Mohan Singh','+9186342345',29724.34,'IT','Delhi'),
('Rohan Yadav','+9186348434',43565.34,'HR','Delhi'),
('Shiva Singh','+9186343466',56744.34,'HR','Noida'),
('Abhishek Chauhan','+9186348729',56742.34,'IT','GZB');

SELECT * FROM employee;
DELETE FROM employee;
TRUNCATE TABLE employee;

# WHERE
SELECT * FROM employee WHERE eadd='Noida';
SELECT * FROM employee WHERE eadd='GZB';

SELECT * FROM employee WHERE esal>50000;
SELECT * FROM employee WHERE edesg='IT';

# AND
SELECT * FROM employee WHERE edesg='IT' AND esal>50000;

# OR
SELECT * FROM employee WHERE edesg='IT' OR eadd='Delhi';
SELECT * FROM employee WHERE edesg='IT' AND eadd='Delhi';

# Aggregate Functions
# sum , count , average , max , min 
SELECT * FROM employee;
SELECT count(*) FROM employee;
SELECT esal FROM employee;
SELECT sum(esal) FROM employee;
SELECT max(esal) FROM employee;
SELECT min(esal) FROM employee;
SELECT avg(esal) FROM employee;


# GROUP BY
SELECT * FROM employee;
SELECT COUNT(*) FROM employee;
SELECT COUNT(*) FROM employee GROUP BY edesg;
SELECT edesg,COUNT(*) FROM employee GROUP BY edesg;
SELECT edesg,SUM(esal) FROM employee GROUP BY edesg;

SELECT eadd,count(*) FROM employee GROUP BY eadd;
SELECT eadd,SUM(esal) FROM employee GROUP BY eadd;
SELECT eadd,AVG(esal) FROM employee GROUP BY eadd;

# ORDER BY 
SELECT * FROM employee;
SELECT * FROM employee ORDER BY esal;
SELECT * FROM employee ORDER BY esal ASC;
SELECT * FROM employee ORDER BY esal DESC;


SELECT eadd,SUM(esal) FROM employee GROUP BY eadd;
SELECT eadd,SUM(esal) FROM employee GROUP BY eadd
ORDER  BY SUM(esal) ASC;

SELECT * FROM employee ORDER BY ename ASC;


# Where clause can not work with aggregate functions if you have group by in your query
SELECT eadd,sum(esal) FROM employee GROUP BY eadd
WHERE SUM(esal)>150000;
# Instead of WHERE we use HAVING
SELECT eadd,sum(esal) FROM employee GROUP BY eadd
HAVING SUM(esal)>150000;

# But you can use HAVING instead of WHERE , if there is no GROUP BY
SELECT * FROM employee WHERE esal>50000;
SELECT * FROM employee HAVING esal>50000;

# LIMIT
SELECT * FROM employee;
SELECT * FROM employee LIMIT 3;
SELECT * FROM employee ORDER BY esal DESC;
SELECT * FROM employee ORDER BY esal DESC LIMIT 3;

# Highest Salary
SELECT * FROM employee ORDER BY esal DESC LIMIT 1;

# 2nd Highest Salary
SELECT * FROM employee ORDER BY esal DESC LIMIT 1 OFFSET 1;

# 3rd Highest Salary
SELECT * FROM employee ORDER BY esal DESC LIMIT 1 OFFSET 2;

