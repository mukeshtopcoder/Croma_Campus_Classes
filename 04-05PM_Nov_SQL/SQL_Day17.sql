/*
Stored Procedure
*/
CREATE DATABASE school;
USE school;
CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT , 
sname VARCHAR(100) NOT NULL , 
sadd VARCHAR(100) NOT NULL , 
sfee DECIMAL(8,2) NOT NULL
);

INSERT INTO student VALUES
(101,'Raman Yadav','Noida',72533),
(102,'Mohan Kumar','Noida',54654),
(103,'Suman Yadav','Delhi',34656),
(104,'Riya Yadav','Noida',34577),
(105,'Yogesh Saini','Delhi',56754);

SELECT * FROM student;

DELIMITER $$
CREATE PROCEDURE student()
BEGIN
	SELECT * FROM student;
END $$ DELIMITER ;

CALL student();

SELECT * FROM student WHERE sid=102;

DELIMITER $$
CREATE PROCEDURE by_sid(IN id INT)
BEGIN 
	SELECT * FROM student WHERE sid = id;
END $$ DELIMITER ;
CALL by_sid(102); 

SELECT avg(sfee) FROM student; 

DELIMITER //
CREATE PROCEDURE average(OUT afee DECIMAL(8,2))
BEGIN 
	SELECT avg(sfee) INTO afee FROM student; 
END // DELIMITER ;
CALL average(@a_fee);

SELECT @a_fee;
SELECT * FROM student WHERE sfee>@a_fee;

SELECT avg(sfee) FROM student WHERE sadd='Noida';

DELIMITER //
CREATE PROCEDURE avg_add(IN address TEXT,OUT aver DECIMAL(8,2))
BEGIN 	
	SELECT avg(sfee) INTO aver FROM student WHERE sadd=address;
END // DELIMITER ;
CALL avg_add('Delhi',@avg_fee);

SELECT @avg_fee;

ALTER TABLE student ADD COLUMN discount DECIMAL(8,2) DEFAULT 0;

SELECT * FROM student WHERE sfee>@avg_fee;
SELECT * FROM student;

DELIMITER //
CREATE PROCEDURE update_discount(IN dis INT)
BEGIN
	UPDATE student SET discount=sfee*dis/100;
END // DELIMITER ;
CALL update_discount(0);
SELECT *,sfee-discount AS Final_FEE FROM student;

