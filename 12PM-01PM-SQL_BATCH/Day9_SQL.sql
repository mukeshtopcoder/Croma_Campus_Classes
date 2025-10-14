# TRIGGER's PRACTICE DAY
# 1.Write a trigger to automatically update a last_modified column in a table when a record
# is updated.

DROP DATABASE school;
CREATE DATABASE school;
USE school;
CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT , 
sname VARCHAR(100) NOT NULL , 
course VARCHAR(100) NOT NULL ,
sfee DECIMAL(8,2) NOT NULL ,
last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO student(sid,sname,course,sfee)
VALUE(101,'Ravi','Python',72530);
SELECT * FROM student;
UPDATE student SET sfee=65000 WHERE sid=101;

DELIMITER $$ 
CREATE TRIGGER update_trigger
BEFORE UPDATE ON student
FOR EACH ROW
BEGIN
	SET NEW.last_modified = NOW();
END $$ DELIMITER ;