DROP DATABASE flipkart;
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
DELETE FROM employee WHERE eid=101;

INSERT INTO emp_log(empid,empname,empdesg,empsal,empadd,event_)
VALUE(102, 'Mohan','IT',87568,'Delhi','Joining');

INSERT INTO employee VALUES
(102, 'Mohan','IT',87568,'Delhi');
# Trigger 

DELIMITER $$
CREATE TRIGGER emp_ins
AFTER INSERT ON employee
FOR EACH ROW
BEGIN
INSERT INTO emp_log(empid,empname,empdesg,empsal,empadd,event_)
VALUE(NEW.eid,NEW.ename,NEW.edesg,NEW.esal,NEW.eadd,'Joining');
END $$ DELIMITER ;

INSERT INTO employee VALUES
(103, 'Yogesh','Admin',37583,'GZB');
SELECT * FROM employee;
SELECT * FROM emp_log;
