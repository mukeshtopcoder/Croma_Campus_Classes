/*
INDEX:- Index is a data structure which is help mySQL to find/search
data fast.
It is like an book's INDEX page in a database

Without Index :- FULL TABLE SCAN
With Index :- Fast Searching

INDEX PROS:-
1- Fast SELECT Query
2- Fast Searching ang Sorting (ORDER BY)
3- Fast Filtering (WHERE)
4- USEFUL in MySQL Joins

INDEX CONS:-
INSERT , UPDATE , DELETE work very slow

Types of INDEX
PRIMARY KEY - Unique+Not Null+ Data Sort
UNIQUE      - UNIQUE BUT NULL allowed
INDEX/Normal INDEX - Just improves the speed of SELECT Query

*/
USE flipkart;
SHOW TABLES;
SELECT * FROM employee;

SELECT * FROM employee WHERE eid=104;
SELECT * FROM employee WHERE eadd='Noida';
CREATE INDEX idx_eadd
ON employee(eadd);
SELECT * FROM employee WHERE eadd='Noida';

SELECT * FROM employee WHERE eadd='Delhi'AND esal>50000;
CREATE INDEX idx_eadd_esal
ON employee(eadd,esal);

SELECT * FROM employee WHERE eadd='Delhi'AND esal>50000;
DROP INDEX idx_sal_add ON employee;
SHOW INDEX FROM employee;

# CURSOR
SELECT ename FROM employee;
DELIMITER $$
CREATE PROCEDURE demo_cursor2()
BEGIN
	DECLARE done INT DEFAULT FALSE;
    DECLARE e_name VARCHAR(100);
    
    -- DECLARE cursor
    DECLARE cur CURSOR FOR
    SELECT ename FROM employee; 
    
    -- HANDLE CUrsor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=TRUE;
    
    -- START cursor
    OPEN cur;
    read_loop:LOOP
		FETCH cur INTO e_name;
        IF done THEN
			LEAVE read_loop;
		END IF;
		SELECT e_name AS emplyee_name;
	END LOOP;
    CLOSE cur;
END $$ DELIMITER ;

CALL demo_cursor2();