/*
STORED PROCEDURE

*/
USE amazon;
SHOW TABLES;
SELECT * FROM employee;

SELECT SUM(esal) FROM employee;


DELIMITER //
CREATE PROCEDURE get_sal()
BEGIN	
	SELECT sum(esal) FROM employee;
END // DELIMITER ;

CALL get_sal();


DELIMITER //
CREATE PROCEDURE get_sal(IN address VARCHAR(100))
BEGIN	
	SELECT sum(esal) FROM employee WHERE eadd=address;
END // DELIMITER ;

CALL get_sal('Noida');


SET @myname = 'AMAN KUMAR';

SELECT @myname;


DELIMITER $$
CREATE PROCEDURE get_sal(OUT salary DECIMAL(8,2))
BEGIN
	SELECT SUM(esal) INTO salary FROM employee;
END $$ DELIMITER ;

CALL get_sal( @totalSalary );

SELECT @totalSalary;



DELIMITER $$
CREATE PROCEDURE get_sal(OUT salary DECIMAL(8,2),IN adr VARCHAR(100))
BEGIN
	SELECT SUM(esal) INTO salary FROM employee WHERE eadd=adr;
END $$ DELIMITER ;

CALL get_sal( @totalSalary,'Delhi' );

SELECT @totalSalary;


SHOW PROCEDURE STATUS;
DROP PROCEDURE get_sal;
