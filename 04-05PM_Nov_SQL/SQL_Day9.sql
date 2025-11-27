/*
employee
eid		ename	esal	emid
101		vivek	868	    103
102     ravi    384     105
103     harish  834     109

SELECT ename FROM employee e
JOIN employee m
ON e.emid = m.eid;


*/

DROP DATABASE IF EXISTS college;
CREATE DATABASE college;
USE college;
CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT , 
sname VARCHAR(100) NOT NULL ,  
sadd VARCHAR(100) NOT NULL ,
cid INT NOT NULL
);

INSERT INTO student VALUES
(101,'Raman','Noida',302),
(102,'Rahul','Delhi',301),
(103,'Mohit','Delhi',303),
(104,'Mahesh','Noida',301); 

SELECT * FROM student;

CREATE TABLE course(
cid INT PRIMARY KEY AUTO_INCREMENT , 
cname VARCHAR(100) NOT NULL ,
cfee DECIMAL(8,2) NOT NULL 
);
INSERT INTO course VALUES
(301,'Python Full Stack',87620),
(302,'SQL',75300);

SELECT * FROM student
JOIN course
USING (cid); 

DROP TABLE student;
DROP TABLE course;

# =====================================

CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT , 
sname VARCHAR(100) NOT NULL ,  
sadd VARCHAR(100) NOT NULL ,
cid INT NOT NULL , 
FOREIGN KEY (cid) REFERENCES course(cid)
);

CREATE TABLE course(
cid INT PRIMARY KEY AUTO_INCREMENT , 
cname VARCHAR(100) NOT NULL ,
cfee DECIMAL(8,2) NOT NULL 
); 

INSERT INTO course VALUES
(301,'Python Full Stack',87620),
(302,'SQL',75300);

DELETE FROM course WHERE cid=302;
DELETE FROM course WHERE cid=301;
SELECT * FROM course;

INSERT INTO student VALUES
(101,'Raman','Noida',302); 
SELECT * FROM student;
DELETE FROM student WHERE sid=101;

UPDATE course SET cid=305 WHERE cid=302;

DROP TABLE student;
DROP TABLE course;


CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT , 
sname VARCHAR(100) NOT NULL ,  
sadd VARCHAR(100) NOT NULL ,
cid INT NOT NULL , 
FOREIGN KEY (cid) REFERENCES course(cid) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE course(
cid INT PRIMARY KEY AUTO_INCREMENT , 
cname VARCHAR(100) NOT NULL ,
cfee DECIMAL(8,2) NOT NULL 
); 

INSERT INTO course VALUES
(301,'Python Full Stack',87620),
(302,'SQL',75300);

INSERT INTO student VALUES
(101,'Raman','Noida',302); 
SELECT * FROM student;
SELECT * FROM course;
UPDATE course SET cid=305 WHERE cid=302;

DELETE FROM course WHERE cid=305;