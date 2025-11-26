/*

USE amazon;
SHOW TABLES;
USE college;
SHOW TABLES;

CREATE TABLE college.product LIKE amazon.product;
DESC product;

CREATE TABLE product2 LIKE product;
INSERT INTO college.product SELECT * FROM amazon.product;
SELECT * FROM product;


JOIN
*/


CREATE DATABASE store;
USE store;
CREATE TABLE customer(
cid INT PRIMARY KEY AUTO_INCREMENT ,
cname VARCHAR(100) NOT NULL , 
cadd VARCHAR(100) NOT NULL
);
INSERT INTO customer VALUES
(101,'Raman Kumar','Noida'),
(102,'Rajesh Singh','Noida'),
(103,'Suraj Kumar','Delhi'),
(104,'Riya Kumari','GZB');

ALTER TABLE customer MODIFY cid INT; # Remove Auto_increment
DESCRIBE customer;
ALTER TABLE customer DROP PRIMARY KEY;
ALTER TABLE customer ADD PRIMARY KEY (cid);

CREATE TABLE products(
pid INT PRIMARY KEY AUTO_INCREMENT ,
pname VARCHAR(100) NOT NULL , 
price DECIMAL(8,2) NOT NULL
);

INSERT INTO products VALUES
(301,'Keyboard',870),
(302,'HDD',3860),
(303,'SDD',8620),
(304,'Monitor',6700);

USE store;
SELECT * FROM customer;
SELECT * FROM products;
SELECT * FROM orders;

# JOIN
# CROSS JOIN (table1_Rows X table2_Rows)
SELECT * FROM customer
JOIN orders;

SELECT * FROM customer
CROSS JOIN orders;

# JOIN / INNER JOIN (with condition - joining column)
SELECT * FROM customer
JOIN orders
ON customer.cid = orders.cid;

SELECT * FROM customer
INNER JOIN orders
ON customer.cid = orders.cid;

SELECT * FROM customer
JOIN orders
USING (cid); 

SELECT * FROM customer
INNER JOIN orders
USING (cid); 

SELECT * FROM customer
JOIN orders
ON customer.cid = orders.cid;

SELECT * FROM customer AS c
JOIN orders AS o
ON c.cid = o.cid;

SELECT * FROM customer c
JOIN orders o
ON c.cid = o.cid;

SELECT * FROM customer c
JOIN orders o
ON c.cid = o.cid
JOIN products p
ON p.pid = o.pid; 

SELECT * FROM products p 
JOIN orders o
ON p.pid = o.pid;

SELECT * FROM customer c
JOIN orders o
ON c.cid = o.cid
JOIN products p
ON p.pid = o.pid; 


SELECT c.*,p.pname,p.price,o.qty FROM customer c
JOIN orders o
ON c.cid = o.cid
JOIN products p
ON p.pid = o.pid ;


SELECT c.*,p.pname,p.price,o.qty, p.price*o.qty AS Net_Amount
FROM customer c JOIN orders o
ON c.cid = o.cid
JOIN products p
ON p.pid = o.pid ;

SELECT c.*,p.pname,p.price,o.qty, p.price*o.qty AS Gross_Amount,
p.price*o.qty*0.18 AS GST
FROM customer c JOIN orders o ON c.cid = o.cid
JOIN products p
ON p.pid = o.pid ;

SELECT c.*,p.pname,p.price,o.qty, p.price*o.qty AS Gross_Amount,
p.price*o.qty*0.18 AS GST , p.price*o.qty+p.price*o.qty*0.18 AS Net_Amount
FROM customer c JOIN orders o ON c.cid = o.cid
JOIN products p
ON p.pid = o.pid ; 

# LEFT JOIN / LEFT OUTER JOIN
SELECT * FROM customer c
LEFT JOIN orders o
ON c.cid = o.cid;

SELECT * FROM customer c
LEFT OUTER JOIN orders o
ON c.cid = o.cid;

# RIGHT JOIN / RIGHT OUTER JOIN
SELECT * FROM customer c
RIGHT JOIN orders o
ON c.cid = o.cid;


# FULL OUTER   (Do not support in MySQL)

SELECT * FROM customer c
FULL OUTER JOIN orders o
ON c.cid = o.cid;

# using UNION you can apply FULL OUTER JOIN (Duplicates Not Allowed)
SELECT * FROM customer c
RIGHT JOIN orders o
ON c.cid = o.cid
UNION
SELECT * FROM customer c
LEFT JOIN orders o
ON c.cid = o.cid;

# UNION ALL  (Duplicates Allowed)
SELECT * FROM customer c
RIGHT JOIN orders o
ON c.cid = o.cid
UNION
SELECT * FROM customer c
LEFT JOIN orders o
ON c.cid = o.cid;

# SELF JOIN
SELECT * FROM customer c1
JOIN customer c2
ON c1.cid = c2.cid;


# EMPLOYEE (programmer, tester , TL , managers) 