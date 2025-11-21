/*
DML :- Data Manipulation Language
INSERT , UPDATE , DELETE , SELECT , REPLACE (Overwrite),
CALL  (Execute stored Procedure (Inside DML)), LOAD DATA
(import large datasets)

TINYBLOB    - 255 Bytes
BLOB        - 64 KB
MEIDUMBLOB  - 16 MB
LONGBLOB    - 4GB

USE flipkart;
SHOW TABLES;
DESCRIBE emp_log;
SELECT * FROM emp_log;
CREATE TABLE emp_log LIKE employee;
CREATE TABLE emp_log AS SELECT * FROM employee;
CREATE TABLE emp_log AS SELECT * FROM employee WHERE eage>17;
DROP TABLE emp_log;

# INSERT
INSERT INTO table_name VALUE(col1,col2,col3,..);
INSERT INTO table_name(col1,col2,col5) VALUE(v1,v2,v5);
INSERT INTO table_name(col1,col3,col7) VALUES
(val1,val3,val7),
(val1,val3,val7),
(val1,val3,val7);

INSERT INTO table_log SELECT * FROM table_name;
USE flipkart;
DROP TABLE emp_log;
CREATE TABLE emp_log LIKE employee;
SELECT * FROM emp_log;
INSERT INTO emp_log SELECT * FROM employee;
CREATE TABLE emp_log AS SELECT * FROM employee;


INSERT INTO users VALUE(1,'Rahul Kumar','Noida');
INSERT IGNORE INTO users VALUE(1,'Rahul Kumar','Noida');
# Prevents error if duplicate data is inserted


INSERT IGNORE INTO users VALUE(1,'Rahul Kumar','Noida');

USE flipkart;
DESCRIBE employee;
INSERT IGNORE INTO employee
VALUE(201,'Ravi','IT',48464,'Noida',27);

SELECT * FROM employee;


# UPDATE
#   Dangerous  (Update in every row)
UPDATE table_name SET col_name=value;

UPDATE table_name SET col_name=value WHERE condition;
UPDATE table_name SET col1=val1,col2=val2 WHERE cond;

You can use UPDATE with join
UPDATE orders AS o
JOIN customer AS c ON o.cid = c.cid
SET o.status = 'shipped' WHERE c.city='Delhi';


# DELETE
#   Dangerous (Delete All rows)
DELETE FROM table_name;

DELETE FROM table_name WHERE cond;
# You can also DELETE with JOIN

DELETE e FROM employee AS e
JOIN departments AS d ON e.dep_id = d.dep_id
WHERE d.name = 'IT';


CREATE TABLE new_db.table1 LIKE old_db.tableX;
INSERT INTO new_db.table1 SELECT * FROM old_db.tableX;


*/