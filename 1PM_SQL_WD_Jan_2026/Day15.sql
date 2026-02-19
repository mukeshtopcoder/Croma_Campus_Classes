/*
Stored Procedures :- It is like a stored query, which can be execute
whenever you want but you need to call it, it will not execute
automatically like trigger.
Stored procedure is like a functions
or it can call User Define Function

Syntax:-

DELIMITER //
CREATE PROCEDURE procedure_name(parameters)
BEGIN
	-- SQL Statements
END // DELIMITER ;

*/
USE amazon;
SHOW TABLES;
SELECT  *  FROM  employee;
INSERT INTO employee(ename,eadd,esal) VALUE('Rihan','Noida',73562);
SELECT sum(esal) FROM employee;


DELIMITER //
CREATE PROCEDURE total_sal()
BEGIN
	SELECT sum(esal) FROM employee;
END // DELIMITER ;

CALL total_sal();

SELECT avg(esal) FROM employee;


DELIMITER $$
CREATE PROCEDURE avg_sal()
BEGIN
	SELECT avg(esal) FROM employee;
END $$ DELIMITER ;

CALL avg_sal();

INSERT INTO employee(ename,eadd,esal) VALUE('Rihan','Noida',73562);


DELIMITER $$
CREATE PROCEDURE add_emp(IN en VARCHAR(50) , IN ea VARCHAR(50) , IN es DECIMAL(8,2))
BEGIN
	INSERT INTO employee(ename,eadd,esal) VALUE(en,ea,es);
END $$ DELIMITER  ;  

CALL add_emp('Mohit','Delhi',62354);
SELECT * FROM employee;
