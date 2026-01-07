/*
Cursor:- CURSOR is use to fetch data from table and print
row-by-row in a different table

Example:-
*/
USE college;
SHOW TABLES;
CREATE TABLE employee (
eid INT PRIMARY KEY AUTO_INCREMENT , 
ename VARCHAR(100) NOT NULL , 
esal DECIMAL(8,2) NOT NULL , 
eadd VARCHAR(100) 
);

INSERT INTO employee VALUES
(101,'Rahul Kumar',37500,'Noida'),
(102,'Suman Yadav',45670,'GZB'),
(103,'Yogesh Kumar',38690,'Delhi'),
(104,'Vikas Saini',65740,'Noida');

SELECT * FROM employee;

DELIMITER $$
CREATE PROCEDURE show_emp()
BEGIN
	# Declare Variables
	DECLARE done INT DEFAULT 1;
    DECLARE salary DECIMAL(8,2);
    # Declare CURSOR
    DECLARE emp_cursor CURSOR FOR
		SELECT esal FROM employee;
	# Declare continue condition
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 0 ;
    # Open Cursor
    OPEN emp_cursor;
		read_loop:LOOP
			FETCH emp_cursor INTO salary;
				IF done = 0 THEN
					LEAVE read_loop;
				END IF;
            SELECT salary AS Emp_Salary;
		END LOOP;
	CLOSE emp_cursor;
END $$ DELIMITER ;


CALL show_emp();