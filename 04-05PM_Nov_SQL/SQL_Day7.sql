/*
LIKE , WILDCARDS
*/
USE flipkart;
SHOW TABLES;
SELECT * FROM employee;
SELECT * FROM employee WHERE eadd='Noida';

# LIKE , WILDCARDS %
SELECT * FROM employee WHERE eadd LIKE "N%";
SELECT * FROM employee WHERE eadd LIKE "D%";
SELECT * FROM employee WHERE eadd LIKE "%B%";
SELECT * FROM employee WHERE eadd LIKE '%L%';

# Relational Operators for Numerical Data
# > < >= <= != =   (!= , <>  Not equal to)
SELECT * FROM employee WHERE eadd!='Noida';
SELECT * FROM employee WHERE eadd<>'Noida';


SELECT * FROM employee WHERE mobile LIKE '987%';
SELECT * FROM employee WHERE esal LIKE '7%';

# LIKE , WILDCARDS _
SELECT * FROM employee WHERE eadd LIKE '_elhi';
SELECT * FROM employee WHERE eadd LIKE '_a%';
SELECT * FROM employee WHERE eadd LIKE '___hi';

# JOIN
DROP DATABASE store;
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

SELECT * FROM customer;
SELECT * FROM products;

CREATE TABLE orders(
oid INT PRIMARY KEY AUTO_INCREMENT , 
cid INT NOT NULL ,
pid INT NOT NULL ,
qty INT DEFAULT 1
);

INSERT INTO orders(cid,pid,qty) VALUES
(102,303,4),
(103,301,5),
(107,302,5),
(101,308,6),
(109,307,5);

USE store;
SELECT * FROM orders;
# CROSS JOIN  (table1_rows X table2_rows)
# JOIN without CONDITION
SELECT * FROM customer
JOIN orders;

SELECT * FROM customer
CROSS JOIN orders;

# INNER JOIN / JOIN  (Both Are Same)
SELECT * FROM customer
JOIN orders
ON customer.cid = orders.cid; 

SELECT * FROM customer
INNER JOIN orders
ON customer.cid = orders.cid; 

SELECT * FROM customer
INNER JOIN orders
USING (cid); 
