USE store;
SHOW TABLES;
SELECT * FROM customer;
SELECT * FROM product;
SELECT * FROM orders;

# JOIN (CROSS)
SELECT * FROM customer
JOIN orders;
SELECT * FROM customer
CROSS JOIN orders;

# INNER JOIN
SELECT * FROM customer
JOIN orders
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

SELECT * FROM customer AS c
INNER JOIN orders AS o
ON c.cid = o.cid;  

SELECT * FROM customer AS c
CROSS JOIN orders AS o
ON c.cid = o.cid;  

# MULTIPLE JOINS
SELECT * FROM customer AS c
JOIN orders AS o
ON c.cid = o.cid
JOIN product
USING (pid); 

SELECT * FROM customer AS c
JOIN orders AS o
ON c.cid = o.cid
JOIN product p
ON o.pid = p.pid;

SELECT c.cid,cname,cmob,cadd,pname,price,qty FROM customer AS c
JOIN orders AS o
ON c.cid = o.cid
JOIN product p
ON o.pid = p.pid;
 
SELECT c.cid,cname,cmob,cadd,pname,price,qty,price*qty AS NetAmount
FROM customer AS c JOIN orders AS o
ON c.cid = o.cid
JOIN product p
ON o.pid = p.pid;

# RIGHT JOIN / RIGHT OUTER JOIN  (Both are same)
SELECT * FROM customer 
RIGHT JOIN orders 
ON customer.cid = orders.cid;

SELECT * FROM customer 
RIGHT OUTER JOIN orders 
ON customer.cid = orders.cid;


# LEFT JOIN / LEFT OUTER JOIN  (BOTH ARE SAME)
SELECT * FROM customer
LEFT JOIN orders
ON customer.cid = orders.cid; 

SELECT * FROM customer
LEFT OUTER JOIN orders
ON customer.cid = orders.cid; 

# FULL OUTER JOIN (LEFT RIGHT (UNION))

SELECT * FROM customer c
LEFT JOIN orders o ON c.cid = o.cid 
UNION
SELECT * FROM customer c
RIGHT JOIN orders o ON c.cid = o.cid;


# SELF JOIN 
SELECT * FROM customer AS c1
JOIN customer AS c2;

SELECT * FROM customer AS c1
JOIN customer AS c2
ON c1.cid = c2.cid; 