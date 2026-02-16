/*
# TRIGGERS:- Trigger is a stored query which will execute/fires 
automatically when an event occur
EVENT:-  INSERT , DELETE , UPDATE

types of Triggers:-
BEFORE INSERT 
BEFORE DELETE
BEFORE UPDATE
AFTER INSERT 
AFTER DELETE
AFTER UPDATE


Syntax:-

DELIMITER $$
CREATE TRIGGER trigger_name
AFTER/BEFORE INSERT|DELETE|UPDATE ON table_name
FOR EACH ROW 
BEGIN
	-- SQL Query ;
END $$ DELIMITER ; 


*/
CREATE DATABASE amazon;
USE amazon;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT ,
ename VARCHAR(100) NOT NULL , 
eadd VARCHAR(100) NOT NULL , 
esal DECIMAL(8,2) NOT NULL 
);

INSERT INTO employee  VALUES
(101,'Amit Singh','Noida',72357.56);

SELECT * FROM employee;
DELETE FROM employee WHERE eid=101;

CREATE TABLE emp_log(
logid INT PRIMARY KEY AUTO_INCREMENT , 
id INT NOT NULL , 
name VARCHAR(100) NOT NULL , 
address VARCHAR(100) NOT NULL , 
sal DECIMAL(8,2) NOT NULL ,
time_ timestamp DEFAULT current_timestamp,
event_ VARCHAR(100)
);

INSERT INTO emp_log(id,name,address,sal,event_) VALUE
(101,'Amit Singh','Noida',72357.56,'Joined');
SELECT * FROM emp_log;
TRUNCATE emp_log;


# TRIGGER
DELIMITER $$
CREATE TRIGGER emp_ins
AFTER INSERT ON employee
FOR EACH ROW
BEGIN
	INSERT INTO emp_log(id,name,address,sal,event_) VALUE
	(NEW.eid,NEW.ename,NEW.eadd,NEW.esal,'Joined');
END $$ DELIMITER ;


INSERT INTO employee  VALUES
(101,'Amit Singh','Noida',72357.56);

SELECT * FROM employee;
SELECT * FROM emp_log;


INSERT INTO employee(ename,eadd,esal) VALUES
('Mohan Kumar','Delhi',75347.56);

# TRIGGER
DELIMITER //
CREATE TRIGGER emp_del
BEFORE DELETE ON employee
FOR EACH ROW
BEGIN
	INSERT INTO emp_log(id,name,address,sal,event_) VALUE
	(OLD.eid,OLD.ename,OLD.eadd,OLD.esal,'Resigned');
END // DELIMITER ; 

SELECT * FROM employee;
DELETE FROM employee WHERE eid=101;
SELECT * FROM emp_log;

# TRIGGER
DELIMITER //
CREATE TRIGGER emp_up
AFTER UPDATE ON employee
FOR EACH ROW
BEGIN
	INSERT INTO emp_log(id,name,address,sal,event_) VALUE
	(NEW.eid,NEW.ename,NEW.eadd,NEW.esal,'Updation');
END // DELIMITER ;

SELECT * FROM employee;
UPDATE employee SET esal=90000 WHERE eid=102;
SELECT * FROM emp_log;

