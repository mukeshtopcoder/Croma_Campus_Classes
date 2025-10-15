/*
Procedure:- Stored Procedure is a block of SQL queries
that can be called whenever needed.
Syntax:-
DELIMITER //
CREATE PROCEDURE procedure_name(arguments)
BEGIN
	-- SQL Query
END // DELIMITER ;

CALL procedure_name(parameters);
*/
CREATE DATABASE oracle;
USE oracle;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT , 
ename VARCHAR(100) NOT NULL ,
eadd VARCHAR(100) NOT NULL ,
esal DECIMAL(8,2) NOT NULL
);
INSERT INTO employee VALUE(101,'Raman','Noida',27673.87);
SELECT * FROM employee;
INSERT INTO employee(ename,eadd,esal) 
VALUE('Mohan','Delhi',38464.84);
SELECT * FROM employee;

DELIMITER $$
CREATE PROCEDURE emp()
BEGIN
	SELECT * FROM employee;
END $$ DELIMITER ;

INSERT INTO employee(ename,eadd,esal) 
VALUE('Shristi','Noida',72353.93);
CALL emp();

SELECT * FROM employee WHERE eadd='Delhi';

DROP PROCEDURE emp;
DELIMITER $$ 
CREATE PROCEDURE emp(IN address VARCHAR(100))
BEGIN
	SELECT * FROM employee WHERE eadd=address;
END $$ DELIMITER ;
CALL emp('Delhi');

SELECT sum(esal) FROM employee WHERE eadd='Delhi';

DELIMITER $$
CREATE PROCEDURE salbyadd(IN address TEXT,OUT sal DECIMAL(8,2))
BEGIN
	SELECT sum(esal) INTO sal FROM employee
    WHERE eadd=address;
END $$ DELIMITER ;
CALL salbyadd('Delhi',@salary);
SELECT @salary;