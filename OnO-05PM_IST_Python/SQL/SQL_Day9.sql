/*
Stored Procedure:-

*/
CREATE DATABASE amazon;
USE amazon;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT , 
ename VARCHAR(100) NOT NULL , 
eadd VARCHAR(100) NOT NULL ,
edesg VARCHAR(15) NOT NULL ,
esal DECIMAL(8,2) NOT NULL
);
	INSERT INTO employee(ename,eadd,edesg,esal) 
	VALUE('Raman Kumar','Noida','HR',37458); 
SELECT * FROM employee;

DELIMITER //
CREATE PROCEDURE ins_emp(IN empn VARCHAR(50) , IN empa VARCHAR(100) ,
IN empd VARCHAR(100) , IN emps DECIMAL(8,2))
BEGIN
	INSERT INTO employee(ename,eadd,edesg,esal) 
	VALUE(empn,empa,empd,emps); 
END // DELIMITER ;



CALL ins_emp('Sohit','Noida','IT',75723);
SELECT * FROM employee;

SELECT sum(esal) FROM employee WHERE eadd='delhi';

DELIMITER $$
CREATE PROCEDURE show_salary(IN address VARCHAR(100) )
BEGIN 
	SELECT sum(esal) FROM employee WHERE eadd=address;
END $$ DELIMITER ;

CALL show_salary('Delhi');
DROP PROCEDURE show_salary;

DELIMITER $$
CREATE PROCEDURE show_salary(IN address VARCHAR(100),OUT salary DECIMAL(8,2) )
BEGIN 
	SELECT sum(esal) INTO salary FROM employee WHERE eadd=address;
END $$ DELIMITER ;

CALL show_salary('Delhi',@salary);

SELECT @salary;

SELECT * FROM employee WHERE esal>@salary;


# EVENT
CREATE EVENT run
ON SCHEDULE AT '2025-11-06 18:00:00'
DO
	CALL show_salary('Noida',@salary); 
    
CREATE EVENT daily_history
ON SCHEDULE EVERY 1 DAY
STARTS '2025-11-06 00:00:00'
DO
	CALL delete_log_emp();
    

CREATE EVENT daily_history
ON SCHEDULE EVERY 1 HOUR
DO
	CALL delete_log_emp();
    
