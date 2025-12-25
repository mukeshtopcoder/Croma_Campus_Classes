/*
VIEWS
Views is like a saved SELECT query
CREATE VIEW view_table_name AS write_your_query_here;

*/
USE flipkart;
SELECT * FROM employee;

CREATE VIEW emp_view AS
SELECT eid,ename,edesg,eadd,eage FROM employee;

SHOW TABLES;
SELECT * FROM emp_view;
SELECT * FROM emp_view WHERE eage>18;
UPDATE emp_view SET eage=92 WHERE eid=111;

SELECT * FROM employee;
# Update Data using View
# Not all views are updateable
# JOIN , GROUP BY , DISTINCT , Aggregate Function , Subquery


# ALTER VIEW
CREATE OR REPLACE VIEW emp_view AS
SELECT eid,ename,edesg,eadd FROM employee;
SELECT * FROM emp_view;

# DROP VIEW
DROP VIEW emp_view;


USE store;
SHOW TABLES;
SELECT * FROM customer;

CREATE VIEW sales AS
SELECT c.*,p.pname,p.price,o.qty, p.price*o.qty AS Gross_Amount,
p.price*o.qty*0.18 AS GST , p.price*o.qty+p.price*o.qty*0.18 AS Net_Amount
FROM customer c JOIN orders o ON c.cid = o.cid
JOIN products p
ON p.pid = o.pid ; 

CREATE VIEW above_30 AS
SELECT * FROM sales WHERE Net_Amount>30000;

SELECT * FROM sales;
SELECT * FROM sales WHERE Net_Amount>30000;

SELECT * FROM above_30;