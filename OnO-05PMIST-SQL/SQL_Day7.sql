/*
triggers:- A trigger is a set of SQL statements that fires/execute 
automatically when an event occur.
EVENT:-  INSERT , UPDATE , DELETE 
Types of trigger:- (6 Types)
BEFORE INSERT
AFTER INSERT
BEFORE DELETE 
AFTER DELETE
BEFORE UPDATE
AFTER UPDATE

*/
USE amazon;
SHOW TABLES;
SELECT * FROM employee;
DELETE FROM employee WHERE eid=103;
# we use to store data in log files/tables
# history create
CREATE TABLE emp_log(
logid INT PRIMARY KEY AUTO_INCREMENT ,
empid INT,
empname VARCHAR(100) , 
empadd VARCHAR(100) , 
empsal DECIMAL(8,2),
empdesg VARCHAR(100) , 
time_ TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
event_ VARCHAR(100) 
);

INSERT INTO employee VALUES(103,'Riya','Delhi',27354.37,'HR');
SELECT * FROM employee;
INSERT INTO emp_log(empid,empname,empadd,empsal,empdesg,event_)
VALUES(103,'Riya','Delhi',27354.37,'HR','Join');
SELECT * FROM emp_log;

# Trigger
# Syntax
/*
DELIMITER $$
CREATE TRIGGER trigger_name
AFTER|BEFORE   INSERT|DELETE|UPDATE
ON table_name FOR EACH ROW
BEGIN
	-- SQL Statement;
END $$ DELIMITER; 
*/
DELIMITER $$
CREATE TRIGGER emp_ins 
AFTER INSERT ON employee
FOR EACH ROW
BEGIN
INSERT INTO emp_log(empid,empname,empadd,empsal,empdesg,event_)
VALUES(NEW.eid,NEW.ename,NEW.eadd,NEW.esal,NEW.edesg,'Join');
END $$ DELIMITER ;

INSERT INTO employee VALUES(104,'Mahesh','Noida',34868.34,'IT');
SELECT * FROM employee;
SELECT * FROM emp_log;

DELIMITER $$
CREATE TRIGGER emp_del
BEFORE DELETE ON employee
FOR EACH ROW
BEGIN
INSERT INTO emp_log(empid,empname,empadd,empsal,empdesg,event_)
VALUES(OLD.eid,OLD.ename,OLD.eadd,OLD.esal,OLD.edesg,'Delete');
END $$ DELIMITER ;

DELETE FROM employee WHERE eid=104;
SELECT * FROM employee;
SELECT * FROM emp_log;

DELIMITER $$
CREATE TRIGGER emp_upd
AFTER UPDATE ON employee
FOR EACH ROW
BEGIN
INSERT INTO emp_log(empid,empname,empadd,empsal,empdesg,event_)
VALUES(NEW.eid,NEW.ename,NEW.eadd,NEW.esal,NEW.edesg,'Update');
END $$ DELIMITER ;

SELECT * FROM employee;
SELECT * FROM emp_log;
UPDATE employee SET esal=90000 , eadd='Noida' WHERE eid=103;

DELIMITER $$
CREATE TRIGGER prevent_delete
BEFORE DELETE ON employee
FOR EACH ROW
BEGIN
	SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = "DELETING EMPLOYEE IS NOT ALLOWED!";
END $$ DELIMITER ;

SET SQL_SAFE_UPDATES=0;
DELETE FROM employee WHERE eid=103;
DROP TRIGGER prevent_delete;

SELECT * FROM emp_log;