/*
Index:- An index i MySQL is like an index in a book, it helps
the database find data faster without scanning every row
in a table.
Use of Index:-
To improve the speed of SELECT queries and sometimes sorting
and grouping functions. 

Trade-off
Indexes take up extra storage space and slow INSERT, UPDATE , 
DELETE operations (because the index also needs updating)

Types of indexes
1- Primary key
	- Automatically create a unique index
2- Unique Key
	- Prevents duplicate values in the columns
3- Normal Indexes
	CREATE INDEX idx_name
    ON table_name(col_name);

*/
USE flipkart;
SHOW TABLES;
SELECT * FROM employee;

SELECT * FROM employee WHERE eadd='Noida';

CREATE INDEX idx_add
ON employee(eadd);

SELECT * FROM employee WHERE eadd='Noida';

SELECT * FROM employee WHERE eadd='Delhi' AND esal>50000;

CREATE INDEX idx_add_sal
ON employee(eadd,esal);

SELECT * FROM employee WHERE eadd='Delhi' AND esal>50000;

/*
Cursor:- A cursor in MySQL is a database pointer that allows
you to iterate (loop) through rows one by one from a result
set.

Cursors are slower than set-based queries, so use them
only when necessary.

*/
SELECT * FROM employee;

DELIMITER $$
CREATE PROCEDURE example_cursor()
BEGIN
	-- Define Variable
	DECLARE done INT DEFAULT 0;
    DECLARE e_name VARCHAR(100);
    DECLARE e_sal DECIMAL(8,2);
    
    -- Define Cursor
    DECLARE cur CURSOR FOR
		SELECT ename,esal FROM employee;
	
    -- Declare what will happen if no more rows
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    
    -- Open The Curosr
    OPEN cur;
    
    -- Start loop
    read_loop: LOOP
    FETCH cur INTO e_name,e_sal;
    IF done THEN
		LEAVE read_loop;
	END IF;
    SELECT e_name,e_sal;
    END LOOP;
    
    CLOSE cur;

END $$ DELIMITER ;

CALL example_cursor();