USE store;
SHOW TABLES;
SELECT * FROM customer;
SELECT * FROM product;
SELECT * FROM orders;

SELECT * FROM customer
JOIN orders 
ON customer.cid = orders.cid;

# LEFT JOIN  /   LEFT OUTER JOIN
SELECT * FROM customer
LEFT JOIN orders 
ON customer.cid = orders.cid;

SELECT * FROM customer
LEFT OUTER JOIN orders 
ON customer.cid = orders.cid;

# RIGHT JOIN  /  RIGHT OUTER JOIN
SELECT * FROM customer
RIGHT JOIN orders 
ON customer.cid = orders.cid;

SELECT * FROM customer
RIGHT OUTER JOIN orders 
ON customer.cid = orders.cid;

# FULL OUTER   # Doesn't work in MySQL  (works in SQL Server)
SELECT * FROM customer
FULL OUTER JOIN orders 
ON customer.cid = orders.cid;

# Apply full outer join using UNION
SELECT * FROM customer
LEFT JOIN orders 
ON customer.cid = orders.cid UNION
SELECT * FROM customer
RIGHT JOIN orders 
ON customer.cid = orders.cid;


# It is called SELF JOIN
SELECT * FROM customer c1
JOIN customer c2
ON c1.cid=c2.cid;


SELECT * FROM customer;
SELECT * FROM product;
SELECT * FROM orders;
DELETE FROM customer WHERE cid=104;

# FOREIGN KEY
CREATE DATABASE school;
USE school;
CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT ,
sname VARCHAR(100) NOT NULL ,
sadd VARCHAR(100) NOT NULL ,
cid INT NOT NULL , FOREIGN KEY (cid) REFERENCES course(cid)
);
CREATE TABLE course(
cid INT PRIMARY KEY AUTO_INCREMENT , 
cname VARCHAR(100) NOT NULL ,
cfee DECIMAL(8,2)
);
INSERT INTO student(sname,sadd,cid) VALUE('Rahul','Noida',101);
INSERT INTO course VALUE(101,'Data Science',73580);
INSERT INTO course VALUE(102,'Data Analytics',45730);
SELECT * FROM course;
SELECT * FROM student;
SELECT * FROM student s  
JOIN course c
ON s.cid=c.cid;

DELETE FROM student WHERE sid=2;
DELETE FROM course WHERE cid=101;

UPDATE course SET cid=105 WHERE cid=101;

DROP TABLE student;
DROP TABLE course;


CREATE TABLE student(
sid INT PRIMARY KEY AUTO_INCREMENT ,
sname VARCHAR(100) NOT NULL ,
sadd VARCHAR(100) NOT NULL ,
cid INT NOT NULL , FOREIGN KEY (cid) REFERENCES course(cid) 
ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE course(
cid INT PRIMARY KEY AUTO_INCREMENT , 
cname VARCHAR(100) NOT NULL ,
cfee DECIMAL(8,2)
);
INSERT INTO student(sname,sadd,cid) VALUE('Rahul','Noida',101);
INSERT INTO course VALUE(101,'Data Science',73580);
INSERT INTO course VALUE(102,'Data Analytics',45730);

SELECT * FROM course;
SELECT * FROM student;
UPDATE course SET cid=155 WHERE cid=101;
DELETE FROM course WHERE cid=155;

SELECT * FROM student s
JOIN course c
ON s.cid=c.cid; 