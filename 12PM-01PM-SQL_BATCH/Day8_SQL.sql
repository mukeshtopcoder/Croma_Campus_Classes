/*
Triggers:- It is a stored program that executes automatically
when an event occur.
EVENT :- INSERT | DELETE | UPDATE
Types of Triggers:-
BEFORE INSERT
AFTER INSERT
BEFORE DELETE
AFTER DELETE
BEFORE UPDATE
AFTER UPDATE

Syntax:-
DELIMITER //
CREATE TRIGGER trigger_name
AFTER|BEFORE   INSERT|DELETE|UPDATE
ON table_name FOR EACH EVERY
BEGIN
	-- SQL Statements;
END // DELIMITER ;
*/
CREATE DATABASE flipkart;
USE flipkart;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT , 
ename VARCHAR(100) NOT NULL , 
eadd VARCHAR(100) NOT NULL ,
esal DECIMAL(8,2)
);

INSERT INTO employee VALUES
(101,'Ravi Shanakar','Noida',72533.58);

SELECT * FROM employee;
DELETE FROM employee WHERE eid=101;

CREATE TABLE employee_log(
logid INT PRIMARY KEY AUTO_INCREMENT  ,
empid INT NOT NULL , 
empname VARCHAR(100) NOT NULL , 
empadd VARCHAR(100) NOT NULL , 
empsal DECIMAL(8,2) NOT NULL , 
eevent VARCHAR(40) NOT NULL ,
time_ TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$
CREATE TRIGGER emp_ins
AFTER INSERT ON employee
FOR EACH ROW
BEGIN 
	INSERT INTO employee_log(empid,empname,empadd,empsal,eevent)
    VALUES(NEW.eid,NEW.ename,NEW.eadd,NEW.esal,"Joined");
END $$ DELIMITER ;

INSERT INTO employee(ename,eadd,esal) VALUES
('Raman','Noida',72530);
SELECT * FROM employee;
SELECT * FROM employee_log;

DELIMITER //
CREATE TRIGGER emp_del
BEFORE DELETE ON employee
FOR EACH ROW
BEGIN 
	INSERT INTO employee_log(empid,empname,empadd,empsal,eevent)
    VALUES(OLD.eid,OLD.ename,OLD.eadd,OLD.esal,"Resigned");
END // DELIMITER ;

INSERT INTO employee(ename,eadd,esal) VALUES
('Riya','Delhi',35470);
SELECT * FROM employee;
SELECT * FROM employee_log;
DELETE FROM employee WHERE eid=103;

CREATE TABLE update_log(
logid INT PRIMARY KEY AUTO_INCREMENT , 
eid INT NOT NULL , 
ename VARCHAR(100) NOT NULL , 
eadd VARCHAR(100) NOT NULL , 
old_sal DECIMAL(8,2) NOT NULL , 
new_sal DECIMAL(8,2) NOT NULL
);
ALTER TABLE update_log ADD COLUMN time_ TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

DELIMITER $$ 
CREATE TRIGGER emp_update
BEFORE UPDATE ON employee
FOR EACH ROW
BEGIN
	INSERT INTO update_log(eid,ename,eadd,old_sal,new_sal)
    VALUE(OLD.eid,OLD.ename,OLD.eadd,OLD.esal,NEW.esal);
END $$ DELIMITER ;

SELECT * FROM employee;
UPDATE employee SET esal=73700 WHERE eid=104;
SELECT * FROM employee;
SELECT * FROM update_log;
