/*
Store Database
customer , product , orders
customer (cid , cname, cmobile , cadd)
product (pid , pname , price)
order (oid , cid , pid , qty)
*/
CREATE DATABASE store;
USE store;
CREATE TABLE customer(
cid INT PRIMARY KEY AUTO_INCREMENT , 
cname VARCHAR(100) NOT NULL , 
cadd VARCHAR(100) NOT NULL , 
cmobile VARCHAR(15) NOT NULL
);

INSERT INTO customer VALUES
(101,'Rahul','Noida','5672573344'),
(102,'Mohan','Delhi','567762573344'),
(103,'Rihan','GZB','34562573344'),
(104,'Mohit','Noida','9862573344')
;

SELECT * FROM customer;

CREATE TABLE product(
pid INT PRIMARY KEY AUTO_INCREMENT , 
pname VARCHAR(100) NOT NULL , 
price DECIMAL(8,2) DEFAULT 0
);

INSERT INTO product VALUES
(501,'SSD',8364),
(502,'Hard Disk',4364),
(503,'Monitor',13000),
(504,'SMPS',5732)
;

SELECT * FROM product;

CREATE TABLE orders(
oid INT PRIMARY KEY AUTO_INCREMENT , 
cid INT NOT NULL , 
pid INT NOT NULL , 
qty INT NOT NULL
);

INSERT INTO orders(cid,pid,qty) VALUES
(102,504,5),
(103,502,7),
(101,507,9),
(106,503,4),
(110,509,3);

SELECT * FROM orders;

# JOIN 
# CROSS JOIN    table1_rows X table2_rows
SELECT * FROM customer
JOIN orders;
SELECT * FROM customer
CROSS JOIN orders;

# JOIN (INNER JOIN)  Common Data
SELECT * FROM customer
JOIN orders
ON customer.cid = orders.cid;

# JOIN / INNER JOIN  (Both are same)
SELECT * FROM customer
INNER JOIN orders
ON customer.cid = orders.cid;

# Add product also
SELECT * FROM customer
INNER JOIN orders
ON customer.cid = orders.cid
INNER JOIN product 
ON orders.pid = product.pid;


SELECT * FROM customer AS c
INNER JOIN orders AS o
ON c.cid = o.cid
INNER JOIN product AS p
ON o.pid = p.pid;

SELECT * FROM customer c
INNER JOIN orders o
ON c.cid = o.cid
INNER JOIN product p
ON o.pid = p.pid;


SELECT c.*,p.*,qty FROM customer AS c
INNER JOIN orders AS o
ON c.cid = o.cid
INNER JOIN product AS p
ON o.pid = p.pid;

SELECT c.*,p.*,qty, p.price*o.qty AS Amount, p.price*qty*0.18
AS Tax,price*qty+price*qty*0.18 AS Net_Amount FROM customer
AS c INNER JOIN orders AS o ON c.cid = o.cid
INNER JOIN product AS p
ON o.pid = p.pid;

# LEFT JOIN / LEFT OUTER JOIN (Both Same)
SELECT * FROM customer AS c
LEFT JOIN orders AS o
ON c.cid = o.cid;

SELECT * FROM customer AS c
LEFT OUTER JOIN orders AS o
ON c.cid = o.cid;

# RIGHT JOIN / RIGHT OUTER JOIN ( Both Are Same)alter
SELECT * FROM customer AS c
RIGHT JOIN orders AS o
ON c.cid = o.cid;

SELECT * FROM customer AS c
RIGHT OUTER JOIN orders AS o
ON c.cid = o.cid;

# FULL JOIN /  FULL OUTER JOIN (SQL Server)
# Do not support in MySQL
SELECT * FROM customer AS c
FULL OUTER JOIN orders AS o
ON c.cid = o.cid;
# FULL OUTER EXAMPLE in MYSQL
SELECT * FROM customer AS c
LEFT JOIN orders AS o
ON c.cid = o.cid
UNION
SELECT * FROM customer AS c
RIGHT JOIN orders AS o
ON c.cid = o.cid;

# self JOIN
SELECT * FROM customer c1
JOIN customer c2
ON c1.cid = c2.cid;