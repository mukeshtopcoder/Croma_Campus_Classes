/*
Triggers:- A trigger is a stored program or an object of a database which will
execute automatically when an event occur.

Syntax:-
DELIMITER $$
CREATE TRIGGER trigger_name
BEFORE|AFTER INSERT|DELETE|UPDATE ON table_name
FOR EACH ROW
BEGIN 
	-- SQL Statements;
END $$ DELIMITER ;;

*/
CREATE DATABASE mydb;
USE mydb;
SHOW TABLES;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT , 
ename VARCHAR(100) NOT NULL , 
eadd VARCHAR(100) NOT NULL , 
esal DECIMAL(8,2) NOT NULL 
);

INSERT INTO employee VALUE(101,'Raman Kumar','Noida',25784.87);
INSERT INTO emp_log(eid,ename,eadd,esal,event_) VALUE
(101,'Raman Kumar','Noida',25784.87,'Joined');
SELECT * FROM employee;
SELECT * FROM emp_log;

DELETE FROM employee WHERE eid=101;

CREATE TABLE emp_log(
logid INT PRIMARY KEY AUTO_INCREMENT , 
eeid INT , 
eename VARCHAR(100) , 
eeadd VARCHAR(100) , 
eesal DECIMAL(8,2) ,
time_ TIMESTAMP DEFAULT current_timestamp,
event_ VARCHAR(100) NOT NULL
);
DROP TABLE emp_log;

# CREATE TRIGGER FOR INSERT
DELIMITER $$
CREATE TRIGGER emp_ins
AFTER INSERT ON employee FOR EACH ROW
BEGIN
	INSERT INTO emp_log(eeid,eename,eeadd,eesal,event_) VALUE
	(NEW.eid,NEW.ename,NEW.eadd,NEW.esal,'Joined');
END $$ DELIMITER ; 

INSERT INTO employee VALUE(102,'Mohan Kumar','Delhi',86537.45);
SELECT * FROM employee;
SELECT * FROM emp_log;
DELETE FROM employee WHERE eid=102;

# DELETE TRIGGER
DELIMITER //
CREATE TRIGGER emp_del
BEFORE DELETE ON employee
FOR EACH ROW
BEGIN
	INSERT INTO emp_log(eeid,eename,eeadd,eesal,event_) VALUE
	(OLD.eid,OLD.ename,OLD.eadd,OLD.esal,'Deleted');
END // DELIMITER ;

INSERT INTO employee VALUE(102,'Mohan Kumar','Delhi',86537.45);
SELECT * FROM employee;
SELECT * FROM emp_log;
DELETE FROM employee WHERE eid=101;

# UPDATE TRIGGER
DELIMITER $$
CREATE TRIGGER emp_upd
AFTER UPDATE ON employee FOR EACH ROW
BEGIN
	INSERT INTO emp_log(eeid,eename,eeadd,eesal,event_) VALUE
	(NEW.eid,NEW.ename,NEW.eadd,NEW.esal,'Updated');
END $$ DELIMITER ;

SELECT * FROM employee;
SELECT * FROM emp_log;
UPDATE employee SET esal=95000.76 WHERE eid=102; 