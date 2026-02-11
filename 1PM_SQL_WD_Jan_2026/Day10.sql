/*
JOIN
Database:->   store
table :->   customer , product , orders
customer (cid , cname , cmob , cadd)
product  (pid , pname , price)
orders   (oid , cid , pid , qty)


*/

CREATE DATABASE store;
USE store;

CREATE TABLE customer(
cid INT PRIMARY KEY AUTO_INCREMENT , 
cname VARCHAR(100) NOT  NULL ,
cmob VARCHAR(15) NOT NULL UNIQUE , 
cadd VARCHAR(100) NOT NULL
);

INSERT INTO customer VALUES
(101,'Raman','98378623345','Noida'),
(102,'Mohan','83548273945','GZB'),
(103,'Yogesh','97583445576','Delhi'),
(104,'Simran','84658343465','Noida');

CREATE TABLE product(
pid INT PRIMARY KEY AUTO_INCREMENT , 
pname VARCHAR(100) NOT NULL , 
price DECIMAL(8,2)
);

INSERT INTO product VALUES
(501,'Monitor',8650),
(502,'Keyboard',870),
(503,'Graphic Card',18900),
(504,'Mouse',350);

CREATE TABLE orders(
oid INT PRIMARY KEY AUTO_INCREMENT , 
cid INT NOT NULL ,
pid INT NOT NULL ,
qty INT DEFAULT 1
);

INSERT INTO orders(cid,pid , qty) VALUES
(102,503,4),
(103,501,8),
(104,507,5),
(106,503,9),
(107,509,5);

SELECT * FROM customer;
SELECT * FROM product;
SELECT * FROM orders;

# JOIN
SELECT * FROM customer;
SELECT * FROM orders;

# CROSS JOIN  (rows = table1_rows X table2_rows)
SELECT * FROM customer
JOIN orders;
SELECT * FROM customer
CROSS JOIN orders;
# BOTH QUERIES ARE SAME

#  INNER JOIN
SELECT * FROM customer
JOIN orders
ON customer.cid = orders.cid;

SELECT * FROM customer
INNER JOIN orders
ON customer.cid = orders.cid;
# JOIN and INNER JOIN both are the same

SELECT * FROM customer
JOIN orders
USING (cid); 
# AGAIN SAME AS INNER JOIN

# USE OF AS (ALIAS)
SELECT * FROM customer AS c
JOIN orders AS o
ON c.cid = o.cid;


# USE OF AS (ALIAS)
SELECT * FROM customer c
JOIN orders o
ON c.cid = o.cid; 


# MULTIPLE JOIN
SELECT * FROM customer c
JOIN orders o 
ON c.cid = o.cid
JOIN product p
ON p.pid = o.pid; 


SELECT c.cid,cname,cmob,cadd,pname,price,qty 
FROM customer c JOIN orders o 
ON c.cid = o.cid
JOIN product p
ON p.pid = o.pid; 

SELECT c.cid,cname,cmob,cadd,pname,price,qty ,price*qty AS NetAmount
FROM customer c JOIN orders o 
ON c.cid = o.cid
JOIN product p
ON p.pid = o.pid; 


SELECT c.cid,cname,cmob,cadd,pname,price,qty ,price*qty AS NetAmount,
price*qty*18/100 AS GST,price*qty+price*qty*18/100 AS GrossAmt
FROM customer c JOIN orders o  ON c.cid = o.cid
JOIN product p
ON p.pid = o.pid; 