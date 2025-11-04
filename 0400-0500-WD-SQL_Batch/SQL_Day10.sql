USE flipkart;
SHOW TABLES;
SELECT * FROM employee;
SELECT * FROM employee WHERE eadd!="GZB";


/*
JOINS
store
(customer,product,orders)
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
(101, 'Rahul Sharma','Noida','+918735498738'),
(102, 'Ravi Gupta','Delhi','+913864926845'),
(103, 'Aman Singh','GZB','+913754872344'),
(104, 'Mahesh Kumar','Meerut','+914786598344');

CREATE TABLE product(
pid INT PRIMARY KEY AUTO_INCREMENT , 
pname VARCHAR(100) NOT NULL , 
price DECIMAL(8,2)
);

INSERT INTO product VALUES
(501,'HDD',7534),
(502,'Graphic Card',18000),
(503,'RAM DDR4',3500),
(504,'SSD',2850);

CREATE TABLE orders(
oid INT PRIMARY KEY AUTO_INCREMENT , 
cid INT ,
pid INT ,
qty INT
);

INSERT INTO orders(cid,pid,qty) VALUES
(102,503,5),
(104,502,6),
(103,509,7),
(107,501,4),
(106,506,8);

SELECT * FROM product;
SELECT * FROM customer;
SELECT * FROM orders;

# JOIN
# JOIN / CROSS JOIN   table1_rows X table2_rows
SELECT * FROM customer
JOIN orders;

# JOIN or CROSS JOIN are same.
SELECT * FROM customer
CROSS JOIN orders;

# JOIN / INNER JOIN (Print Common Values)
SELECT * FROM customer
JOIN orders
ON customer.cid = orders.cid;

# JOIN and INNER JOIN are same
SELECT * FROM customer
INNER JOIN orders
ON customer.cid = orders.cid;

SELECT * FROM customer AS c
INNER JOIN orders AS o
ON c.cid = o.cid;

SELECT * FROM customer c
INNER JOIN orders o
ON c.cid = o.cid;


SELECT * FROM customer AS c
INNER JOIN orders AS o
ON c.cid = o.cid
JOIN product p
ON p.pid = o.pid;



SELECT cname,pname FROM customer AS c
INNER JOIN orders AS o
ON c.cid = o.cid
JOIN product p
ON p.pid = o.pid;

SELECT c.*,p.pname,p.price,o.qty FROM customer AS c
INNER JOIN orders AS o
ON c.cid = o.cid
JOIN product p
ON p.pid = o.pid;


SELECT c.*,p.pname,p.price,o.qty
FROM customer AS c INNER JOIN orders AS o
ON c.cid = o.cid JOIN product p ON p.pid = o.pid;



SELECT c.*,p.pname,p.price,o.qty,price*qty AS Amount, price*qty*0.18
AS GST, price*qty+price*qty*0.18 AS Net_Amount
FROM customer AS c INNER JOIN orders AS o
ON c.cid = o.cid JOIN product p ON p.pid = o.pid;



SELECT cname,pname,price,qty,price*qty AS Amount
FROM customer AS c INNER JOIN orders AS o
ON c.cid = o.cid
JOIN product p
ON p.pid = o.pid;