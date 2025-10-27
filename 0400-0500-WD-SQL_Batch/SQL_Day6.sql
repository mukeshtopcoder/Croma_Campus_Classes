/*
Revision
*/
USE amazon;
SHOW TABLES;
SELECT * FROM employee;

SELECT edesg,count(esal) FROM employee GROUP BY edesg
HAVING count(esal)>2;

/*
Triggers:- Trigger is a set of SQL statements, which fires
automatically when an event occur.

EVENTS:-   INSERT , DELETE , UPDATE
Types of Triggers:-
AFTER INSERT
BEFORE INSERT
AFTER DELETE
BEFORE DELETE
AFTER UPDATE 
BEFORE UPDATE

*/
CREATE DATABASE flipkart;
USE flipkart;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT , 
ename VARCHAR(100) NOT NULL , 
edesg VARCHAR(100) NOT NULL , 
esal DECIMAL(8,2) NOT NULL , 
eadd VARCHAR(100) NOT NULL
);

INSERT INTO employee VALUES
(101, 'Rahul','HR',37554,'Noida');
SELECT * FROM employee;
DELETE FROM employee WHERE eid=101;

CREATE TABLE emp_log(
logid INT PRIMARY KEY AUTO_INCREMENT , 
empid INT ,
empname VARCHAR(100) , 
empdesg VARCHAR(100) , 
empsal DECIMAL(8,2) , 
empadd VARCHAR(100) ,
joining_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP , 
event_ VARCHAR(100)
);
SELECT * FROM employee;
SELECT * FROM emp_log;

INSERT INTO employee VALUES
(101, 'Rahul','HR',37554,'Noida');

INSERT INTO emp_log(empid,empname,empdesg,empsal,empadd,event_)
VALUE(101, 'Rahul','HR',37554,'Noida','Joining');

DELETE FROM employee WHERE eid=101;

/*
DELIMITER $$
CREATE TRIGGER trigger_name
AFTER|BEFORE INSERT|DELETE|UPDATE
ON table_name FOR EACH ROW
BEGIN
	-- SQL Statements;
END $$ DELIMITER;
*/
DELIMITER //
CREATE TRIGGER emp_ins
AFTER INSERT ON employee
FOR EACH ROW
BEGIN 
INSERT INTO emp_log(empid,empname,empdesg,empsal,empadd,event_)
VALUE(NEW.eid,NEW.ename,NEW.edesg,NEW.esal,NEW.eadd,'Joining');	
END // DELIMITER ;

SELECT * FROM employee;
SELECT * FROM emp_log;
INSERT INTO employee VALUES
(103, 'Ramesh','IT',45633,'Delhi');

DELETE FROM employee WHERE eid=101;

DELIMITER //
CREATE TRIGGER emp_del
BEFORE DELETE ON employee
FOR EACH ROW
BEGIN 
INSERT INTO emp_log(empid,empname,empdesg,empsal,empadd,event_)
VALUE(OLD.eid,OLD.ename,OLD.edesg,OLD.esal,OLD.eadd,'Service Off');	
END // DELIMITER ;


DELETE FROM employee WHERE eid = 102;
SELECT * FROM employee;
SELECT * FROM emp_log;

SHOW TRIGGERS;
DROP TRIGGER emp_ins;
