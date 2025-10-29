# Trigger Example
USE flipkart;
SHOW TABLES;
SELECT * FROM emp_log;
DELIMITER $$
CREATE TRIGGER emp_up
AFTER UPDATE ON employee
FOR EACH ROW
BEGIN
INSERT INTO emp_log(empid,empname,empdesg,empsal,empadd,event_)
VALUE(NEW.eid,NEW.ename,NEW.edesg,NEW.esal,NEW.eadd,"Updated");
END $$ DELIMITER ;
DROP TRIGGER emp_up;
SELECT * FROM emp_log;
UPDATE employee SET esal=45000 WHERE eid=108;

UPDATE employee SET esal=90000 , eadd='GZB' WHERE eid=106;
SELECT * FROM employee;
/*
Procedure:- Stored procedure is a set of SQL statements
which perform/fires/execute when you will call this procedure.

Syntax:-
DELIMITER $$ 
CREATE PROCEDURE procedure_name
BEGIN
	-- SQL
END $$ DELIMITER ;
*/

USE flipkart;
SELECT * FROM employee;

DELIMITER $$
CREATE PROCEDURE emp()
BEGIN
	SELECT * FROM employee;
END $$ DELIMITER ; 

CALL emp();

SELECT * FROM employee WHERE eadd='GZB';

DELIMITER $$
CREATE PROCEDURE empadd(IN address VARCHAR(100))
BEGIN
	SELECT * FROM employee WHERE eadd=address;
END $$ DELIMITER ;

CALL empadd('Delhi');


# WILDCARDS LIKE  % , _
SELECT * FROM employee WHERE eadd='Noida';
INSERT INTO employee VALUES(110,'Rihan','IT',38547,'Nanital');

SELECT * FROM employee WHERE eadd LIKE "N%";
SELECT * FROM employee WHERE eadd LIKE "_a%";

