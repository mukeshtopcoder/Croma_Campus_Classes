/*
JOINS and FOREIGN KEY Revision
*/
CREATE DATABASE college;
USE college;
CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT , 
sname VARCHAR(100) NOT NULL ,
sadd VARCHAR(100) NOT NULL , 
cid INT NOT NULL
);
INSERT INTO student VALUES
(101,'Rahul Kumar','Noida',301),
(102,'Raman','Delhi',303),
(103,'Suman Kumar','Noida',303),
(104,'Riya Kumar','GZB',302);

CREATE TABLE course(
cid INT PRIMARY KEY AUTO_INCREMENT , 
cname VARCHAR(100) NOT NULL , 
cfee DECIMAL(8,2) NOT NULL 
);

INSERT INTO course VALUES 
(301,'Data Science',82750),
(302,'Data Analytics',47280),
(303,'Java Full Stack',75270),
(304,'Python Full Stack',75380);

SELECT * FROM student;
SELECT * FROM course;

SELECT * FROM student
JOIN course
ON student.cid = course.cid;


DELETE FROM course WHERE cid=303;




# FOREIGN KEY
DROP TABLE student;
DROP TABLE course;

CREATE TABLE course(
cid INT PRIMARY KEY AUTO_INCREMENT , 
cname VARCHAR(100) NOT NULL , 
cfee DECIMAL(8,2) NOT NULL 
);

CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT , 
sname VARCHAR(100) NOT NULL ,
sadd VARCHAR(100) NOT NULL , 
cid INT NOT NULL , 
FOREIGN KEY (cid) REFERENCES course(cid)
);

INSERT INTO course VALUES 
(301,'Data Science',82750),
(302,'Data Analytics',47280),
(303,'Java Full Stack',75270),
(304,'Python Full Stack',75380);

INSERT INTO student VALUES
(101,'Rahul Kumar','Noida',301),
(102,'Raman','Delhi',303),
(103,'Suman Kumar','Noida',303),
(104,'Riya Kumar','GZB',302);

SELECT * FROM student;
SELECT * FROM course;

SELECT * FROM student
JOIN course
ON student.cid = course.cid;

DELETE FROM course WHERE cid=302;
UPDATE course SET cid=305 WHERE cid=303;

DROP TABLE course;
DROP TABLE student;


CREATE TABLE course(
cid INT PRIMARY KEY AUTO_INCREMENT , 
cname VARCHAR(100) NOT NULL , 
cfee DECIMAL(8,2) NOT NULL 
);

CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT , 
sname VARCHAR(100) NOT NULL ,
sadd VARCHAR(100) NOT NULL , 
cid INT NOT NULL , 
FOREIGN KEY (cid) REFERENCES course(cid)
ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO course VALUES 
(301,'Data Science',82750),
(302,'Data Analytics',47280),
(303,'Java Full Stack',75270),
(304,'Python Full Stack',75380);

INSERT INTO student VALUES
(101,'Rahul Kumar','Noida',301),
(102,'Raman','Delhi',303),
(103,'Suman Kumar','Noida',303),
(104,'Riya Kumar','GZB',302);

SELECT * FROM student;
SELECT * FROM course;

SELECT * FROM student
JOIN course
ON student.cid = course.cid;

UPDATE course SET cid=355 WHERE cid=303;

DELETE FROM course WHERE cid=302;