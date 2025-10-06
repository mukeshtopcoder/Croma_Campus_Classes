# Foreign Key
/*
Database school
student (sid , sname , sadd, smobile , cid)
course (cid , cname , cfee , desc)

*/
create database school;
use school;
CREATE TABLE student (
sid INT PRIMARY KEY AUTO_INCREMENT,
sname VARCHAR(50) NOT NULL,
sadd VARCHAR(100) NOT NULL,
smob INT,
cid INT ,
FOREIGN KEY (cid) REFERENCES course(cid)
);
INSERT INTO student (sname,sadd,smob,cid) VALUES
('Raman Singh','Noida',396485, 2);

SELECT * FROM student;


CREATE TABLE course (
cid INT PRIMARY KEY AUTO_INCREMENT,
cname VARCHAR(50) NOT NULL,
cfee DECIMAL(10,2) NOT NULL,
des TEXT
);
INSERT INTO course(cname,cfee,des) VALUE
('Data Science',83548,'Python , ML , DL , AI , NLP etc'),
('Data Analytics',34750,'Excel , Power BI , Python , SQL');
SELECT * FROM course;

DELETE FROM course WHERE cid=2;
DELETE FROM course WHERE cid=4;

UPDATE course SET cid=5 WHERE cid=3;
UPDATE course SET cid=6 WHERE cid=2;


create database college;
use college;
CREATE TABLE student (
sid INT PRIMARY KEY AUTO_INCREMENT,
sname VARCHAR(50) NOT NULL,
sadd VARCHAR(100) NOT NULL,
smob VARCHAR(100) NOT NULL,
cid INT ,
FOREIGN KEY (cid) REFERENCES course(cid) ON UPDATE CASCADE ON DELETE CASCADE
);
INSERT INTO student (sname,sadd,smob,cid) VALUES
('Raman Singh','Noida',396485, 2);

SELECT * FROM student;


CREATE TABLE course (
cid INT PRIMARY KEY AUTO_INCREMENT,
cname VARCHAR(50) NOT NULL,
cfee DECIMAL(10,2) NOT NULL,
des TEXT
);
INSERT INTO course(cname,cfee,des) VALUE
('Data Science',83548,'Python , ML , DL , AI , NLP etc'),
('Data Analytics',34750,'Excel , Power BI , Python , SQL');

SELECT * FROM course;
SELECT * FROM student;

UPDATE course SET cid=5 WHERE cid=2;

DELETE FROM course WHERE cid=5;
