/*
Stored Procedure :- A Group of SQL statements saved in the database,
which you can call whenever needed
(that you can execute again and again)

Syntax:- 
DELIMITER $$
CREATE PROCEDURE procedure_name(parameters)
BEGIN
	-- SQL
END  $$ DELIMITER ;

CALL procedure_name(argument);
*/

CREATE DATABASE mydb;
USE mydb;
SHOW TABLES;
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT , 
ename VARCHAR(100) NOT NULL , 
eadd VARCHAR(100) NOT NULL , 
esal DECIMAL(8,2) NOT NULL 
);

SELECT * FROM employee;
INSERT INTO employee VALUES
(103,"Siya Singh",'Noida',38468),
(104,"Riya Yadav",'Delhi',45567),
(105,"Priya Saini",'Noida',56733),
(106,"Somya Singh",'GZB',87765);

SELECT * FROM employee;

DELIMITER //
CREATE PROCEDURE emp()
BEGIN
	SELECT * FROM employee;
END // DELIMITER ;

CALL emp();

SELECT * FROM employee WHERE eadd="Noida";

DELIMITER $$
CREATE PROCEDURE show_emp(IN address VARCHAR(100))
BEGIN
	SELECT * FROM employee WHERE eadd = address;
END $$ DELIMITER ;

CALL show_emp("Noida");
CALL show_emp("Delhi");
CALL show_emp("GZB");


INSERT INTO employee(ename,eadd,esal) VALUE('Ram','GZB',82563);

DELIMITER // 
CREATE PROCEDURE ins_emp(IN en VARCHAR(100) , IN ea VARCHAR(100) , IN es DECIMAL(8,2))
BEGIN
	INSERT INTO employee(ename,eadd,esal) VALUE(en,ea,es);
END // DELIMITER ;

CALL ins_emp("Mohan","Noida",78263); 
CALL emp();

DELIMITER //
CREATE TRIGGER tri_name
AFTER INSERT ON employee 
FOR EACH ROW
BEGIN
	CALL ins_emp(NEW.ename,NEW.eadd,NEW.esal);
END // DELIMITER ;

SELECT avg(esal) FROM employee;

DELIMITER $$
CREATE PROCEDURE average(OUT aver DECIMAL(8,2))
BEGIN
	SELECT avg(esal) INTO aver FROM employee;
END $$ DELIMITER ;

CALL average(@sal_avg);
SELECT @sal_avg;
SELECT * FROM employee WHERE esal > @sal_avg; 

DROP PROCEDURE average;



#
DELIMITER //
CREATE PROCEDURE avg_add(IN address VARCHAR(100) ,OUT aver DECIMAL(8,2))
BEGIN
	SELECT avg(esal) INTO aver FROM employee WHERE eadd=address;
END // DELIMITER ; 

CALL avg_add("GZB",@avg_sal); 

SELECT @avg_sal;

