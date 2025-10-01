# JOINS
/*
Database :- Store
customer (cid , cname , cadd , cmobile) 
product (pid , pname , price)
orders (oid , cid , pid , qty)
*/

CREATE DATABASE store;
USE store;
CREATE TABLE customer(
cid INT PRIMARY KEY AUTO_INCREMENT , 
cname VARCHAR(100) NOT NULL , 
cadd VARCHAR(50) NOT NULL , 
cmobile VARCHAR(15) NOT NULL
);
INSERT INTO customer(cname,cadd,cmobile) VALUES
('Shiva Yadav','Noida','938783334'),
('Abhishek','GZB','398657333'),
('Vikas Kumar','Gurugram','28537873023');

SELECT * FROM customer;

CREATE TABLE product(
pid INT PRIMARY KEY AUTO_INCREMENT , 
pname VARCHAR(100) NOT NULL , 
price DECIMAL(8,2) NOT NULL
);
INSERT INTO product VALUES
(501,'Hard Disk',8752),
(502,'Cabinet',3760),
(503,'SSD-1TB',8920),
(504,'Pan Drive',470);
SELECT * FROM product;

CREATE TABLE orders(
oid INT PRIMARY KEY AUTO_INCREMENT , 
cid INT NOT NULL , 
pid INT NOT NULL , 
qty INT DEFAULT 1
);
INSERT INTO orders(cid , pid , qty) VALUES
(102,503,7),
(103,502,8),
(107,501,4),
(101,508,9),
(108,509,6);
SELECT * FROM orders;

# JOINS 
# CROSS JOIN (print table1row X table2row)
SELECT * FROM customer
JOIN orders;
SELECT * FROM customer
CROSS JOIN orders;

# JOIN / INNER JOIN
SELECT * FROM customer 
JOIN orders 
ON customer.cid = orders.cid;


# JOIN / INNER JOIN  (Both are same)
SELECT * FROM orders
INNER JOIN product 
ON orders.pid = product.pid;


SELECT * FROM customer
JOIN orders
ON customer.cid = orders.cid
JOIN product
ON orders.pid = product.pid;


SELECT * FROM customer AS c
JOIN orders AS o
ON c.cid = o.cid
JOIN product AS p
ON o.pid = p.pid;

SELECT * FROM customer c
JOIN orders o
ON c.cid = o.cid
JOIN product p
ON o.pid = p.pid;


SELECT c.*,p.pname,p.price,o.qty FROM customer AS c
JOIN orders AS o
ON c.cid = o.cid
JOIN product AS p
ON o.pid = p.pid;



SELECT c.*,p.pname,p.price,o.qty , p.price*o.qty AS Amount,
p.price*o.qty*0.18 AS GST, p.price*o.qty+p.price*o.qty*0.18 AS NetAmount 
FROM customer AS c JOIN orders AS o ON c.cid = o.cid
JOIN product AS p
ON o.pid = p.pid;

# LEFT JOIN / LEFT OUTER JOIN (Both Are Same) 
SELECT * FROM customer
LEFT JOIN orders ON customer.cid = orders.cid;

SELECT * FROM customer
LEFT OUTER JOIN orders ON customer.cid = orders.cid;
 

# RIGHT JOIN / RIGHT OUTER JOIN (Both Are Same)
SELECT * FROM customer
RIGHT JOIN orders ON customer.cid = orders.cid;

SELECT * FROM customer
RIGHT OUTER JOIN orders ON customer.cid = orders.cid;

# FULL OUTER JOIN (It works in SQL Server)
SELECT * FROM customer
FULL OUTER JOIN orders ON customer.cid = orders.cid;

# FULL OUTER JOIN in MySQL using UNION
SELECT * FROM customer
LEFT OUTER JOIN orders ON customer.cid = orders.cid
UNION
SELECT * FROM customer
RIGHT OUTER JOIN orders ON customer.cid = orders.cid;