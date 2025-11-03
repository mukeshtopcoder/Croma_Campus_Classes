/*
Stored Procedure Exercise

*/
USE flipkart;
SHOW TABLES;
SELECT * FROM emp_log;
SELECT * FROM emp_log WHERE empadd='Noida' AND empsal>40000;

DELIMITER $$
CREATE PROCEDURE emp_view(IN address VARCHAR(50),IN salary DECIMAL(8,2))
BEGIN
	SELECT * FROM emp_log WHERE 
    empadd=address AND empsal>salary;
END $$ DELIMITER ;

CALL emp_view('Noida',70000);

SELECT * FROM emp_log WHERE empadd LIKE "N%";

DELIMITER $$
CREATE PROCEDURE emp_add(IN ch VARCHAR(10))
BEGIN
	SELECT * FROM emp_log WHERE empadd LIKE CONCAT(ch,"%"); 
END $$ DELIMITER ;
CALL emp_add('DEL');
ALTER TABLE emp_log ADD COLUMN bonus DECIMAL(8,2);

DELIMITER //
CREATE PROCEDURE update_bonus(IN per DECIMAL(5,2),IN eid INT)
BEGIN
	UPDATE emp_log SET bonus=empsal*per/100 WHERE empid=eid;
END // DELIMITER ;

CALL update_bonus(4);
SELECT * FROM emp_log; 

SELECT sum(empsal) FROM emp_log WHERE empadd='Noida';

DELIMITER $$
CREATE PROCEDURE fetchSal(IN address VARCHAR(40),OUT salary DECIMAL(8,2))
BEGIN
	SELECT sum(empsal) INTO salary FROM emp_log WHERE empadd=address;
END $$ DELIMITER ;

CALL fetchSal('Noida',@sal); 
SELECT @sal;
DROP PROCEDURE fetchSal;