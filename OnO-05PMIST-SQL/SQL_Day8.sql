/*
Procedure:- A set of SQL statements, which perform when you called.
it is also stored procedure.

DELIMITER $$
CREATE PROCEDURE procedure_name(parameter)
BEGIN
	-- SQL Statements
END $$ DELIMITER ;
*/

USE flipkart;
SHOW TABLES;
DESCRIBE employee;
SELECT * FROM employee;

DELIMITER $$
CREATE PROCEDURE emp()
BEGIN 
	SELECT * FROM employee;
END $$ DELIMITER ;
DROP PROCEDURE emp;

CALL emp();

SELECT * FROM employee WHERE eadd='Delhi';

DELIMITER $$
CREATE PROCEDURE emp(IN address VARCHAR(100))
BEGIN
	SELECT * FROM employee WHERE eadd=address;
END $$ DELIMITER ;

CALL emp('GZB');

SELECT * FROM employee;

DELIMITER //
CREATE PROCEDURE update_sal(IN per DECIMAL(5,2)) 
BEGIN
	UPDATE employee SET esal=esal+esal*per/100;
END // DELIMITER ;

SET SQL_SAFE_UPDATES=0;
CALL update_sal(200);
SELECT * FROM employee;

