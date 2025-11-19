USE store;
SHOW TABLES;
SELECT * FROM customer;
SELECT * FROM product;
SELECT * FROM orders;

SELECT * FROM customer c1 
JOIN customer c2;   # SELF JOIN  /  CROSS JOIN
SELECT * FROM customer c
RIGHT JOIN orders o
ON c.cid = o.cid
UNION
SELECT * FROM customer c
LEFT JOIN orders o
ON c.cid = o.cid;

SELECT * FROM customer;
SELECT * FROM customer WHERE cadd IN ('Noida','GZB');

DROP  TABLE  IF EXISTS student;
CREATE DATABASE IF NOT exists store;

SELECT * FROM customer c
RIGHT JOIN orders o
USING (cid);


USE flipkart;
SELECT * FROM employee;
SELECT edesg,sum(esal) FROM employee GROUP BY edesg;

# WINDOW function
SELECT *,sum(esal) OVER () FROM employee;
SELECT *,sum(esal) OVER (PARTITION BY edesg) FROM employee;

SELECT *,DENSE_RANK() OVER (ORDER BY esal DESC)
FROM employee;

DELETE FROM employee;
TRUNCATE TABLE employee;


sname CHAR(20); # ANU
sname VARCHAR(20); # ANU

USE store;
SELECT * FROM orders;
ALTER TABLE orders ADD COLUMN netqty INT;
SET SQL_SAFE_UPDATES = 0;
UPDATE orders SET netqty=30;
SELECT sum(qty) FROM orders;

CREATE TABLE ordersss(netqty INT);
SELECT * FROM orders;
INSERT INTO orders(cid,pid,qty) VALUE(102,203,4);
INSERT INTO ordersss VALUE(0);
DELIMITER $$
CREATE TRIGGER updateQty
AFTER INSERT ON orders
FOR EACH ROW
BEGIN 
	DECLARE total INT;
    SELECT sum(qty) INTO total FROM orders;
    UPDATE ordersss SET netqty=total;
END $$ DELIMITER ;
DROP TRIGGER updateQty;

SELECT * FROM ordersss;