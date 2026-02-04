/*

*/
USE amazon;
SHOW TABLES;
SELECT * FROM employee;
UPDATE employee SET ename='Anu';
# OFF SAFE UPDATES FOR DELETE OR UPDATE
SET SQL_SAFE_UPDATES = 0; 

# CLAUSES
DROP DATABASE croma;
CREATE DATABASE croma;
USE croma;
CREATE TABLE employee (
eid INT PRIMARY KEY AUTO_INCREMENT ,
ename VARCHAR(30) NOT NULL ,
emob VARCHAR(15) NOT NULL ,
esal DECIMAL(8,2) DEFAULT 0.0 ,
eadd VARCHAR(100) NOT NULL , 
eage INT NOT NULL CHECK (eage>17)
);

INSERT INTO employee 
VALUE(101,'Ramandeep','+919894649653',37465.56,'Noida',29);

SELECT * FROM employee;

INSERT INTO employee(ename,emob,eadd,eage)
VALUE('Siya Singh','+91865347824','Delhi',25);

INSERT INTO employee(ename,emob,esal,eadd,eage) VALUES
('Sohan','+91852374565',26346.45,'Noida',32),
('Mohan','+91852374454',45876.45,'Delhi',23),
('Rohan','+91852374455',34868.56,'Delhi',31),
('Ravi','+91852372356',27458.56,'Noida',27);

SELECT * FROM employee;
# WHERE
SELECT * FROM employee;
SELECT * FROM employee WHERE eage>30;
SELECT * FROM employee WHERE esal>30000;
SELECT * FROM employee WHERE eadd='Noida';
SELECT * FROM employee WHERE eadd='Delhi';

ALTER TABLE employee MODIFY eage SMALLINT CHECK (eage>17);
ALTER TABLE employee CHANGE eage eage TINYINT;
RENAME TABLE employee TO employee_db;
ALTER TABLE employee RENAME TO employee_db; 
DESCRIBE employee;

SELECT * FROM employee;
DELETE FROM employee WHERE eid=103;