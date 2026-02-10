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

# WILD CARDS % _
# LIKE 

SELECT * FROM employee;
SELECT * FROM employee WHERE eadd='Noida';

INSERT INTO employee(ename , mobile , esal , edesg , eadd) VALUES
('Vishal','+918634677643',45674.34,'IT','Nagpur'),
('Shiva','+918643566778',45332.34,'IT','Nanital'),
('Rohit','+918635776543',65763.34,'HR','Dehradun');

SELECT * FROM employee WHERE eadd='Noida';
# LIKE  %

SELECT * FROM employee WHERE eadd LIKE 'Noida';
SELECT * FROM employee WHERE eadd LIKE 'Na%';
SELECT * FROM employee WHERE eadd LIKE 'N%';

SELECT * FROM employee WHERE eadd LIKE '%n%';

# LIKE   _
SELECT * FROM employee WHERE eadd LIKE '_e%';

SELECT * FROM employee WHERE eadd LIKE '__i%';

# IN
SELECT * FROM employee WHERE eadd='Noida' OR eadd='Delhi';

SELECT * FROM employee WHERE eadd IN ('Noida','Delhi');


# BETWEEN
SELECT * FROM employee WHERE esal>50000 AND esal<70000;
SELECT * FROM employee WHERE esal BETWEEN 50000 AND 70000;


# DISTINCT
SELECT eadd FROM employee;
SELECT DISTINCT eadd FROM employee;
SELECT DISTINCT edesg FROM employee;

SELECT * FROM employee;

# DELETE EVERYTHING FROM THE TABLE
TRUNCATE employee;
DELETE FROM employee;

INSERT INTO employee(ename , mobile , esal , edesg , eadd) VALUES
('Aman Kumar','+9186348759',75287.34,'IT','Delhi'),
('Baman Kumar','+9186348435',NULL,'HR','Noida'),
('Riya Singh',NULL,34532.34,'HR','GZB'),
('Mohan Singh','+9186342345',29724.34,'IT','Delhi'),
('Rohan Yadav',NULL,43565.34,'HR','Delhi'),
('Shiva Singh','+9186343466',56744.34,'HR','Noida'),
('Abhishek Chauhan','+9186348729',NULL,'IT','GZB');

DESCRIBE employee;

SELECT * FROM employee;

# IS NULL
SELECT * FROM employee WHERE esal IS NULL;
SELECT * FROM employee WHERE esal IS NOT NULL;

SELECT * FROM employee WHERE mobile IS NULL;


DESCRIBE employee;

ALTER TABLE employee DROP COLUMN edesg;
ALTER TABLE employee ADD COLUMN edesg VARCHAR(20) ;

TRUNCATE employee;

DESCRIBE employee;
ALTER TABLE employee MODIFY edesg VARCHAR(20) NOT NULL;

