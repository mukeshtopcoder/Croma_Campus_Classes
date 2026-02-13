/*
Foreign Key:- In a table a foreign key is a primary key in
another table, it is use to build a relation b/w tables. 

*/
CREATE DATABASE school;
USE school;
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
cfee DECIMAL(8,2)
);

DESCRIBE student;
INSERT INTO student(sname , sadd , cid ) VALUES
('Mohit Singh','Noida',301);

SELECT * FROM student;
SELECT * FROM student
JOIN course
USING (cid);
 

DESCRIBE course;
INSERT INTO course VALUES
(301,'Data Science',92683),
(302,'Data Analytics',34865),
(303,'Python With AI',62376),
(304,'Python Full Stack',34899);

SELECT * FROM course;

DELETE FROM course WHERE cid=303;
UPDATE student SET cid=303;

UPDATE course SET cid=307 WHERE cid=303;

SELECT * FROM student;


CREATE DATABASE school;
USE school;

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
cfee DECIMAL(8,2)
);


INSERT INTO course VALUES
(301,'Data Science',92683),
(302,'Data Analytics',34865),
(303,'Python With AI',62376),
(304,'Python Full Stack',34899);

INSERT INTO student(sname , sadd , cid ) VALUES
('Mohit Singh','Noida',301);

SELECT * FROM student;
UPDATE course SET cid=305 WHERE cid=301;
SELECT * FROM course;

DELETE FROM course WHERE cid=305;
