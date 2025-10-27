/*
Transaction:- 
1- Debit
2- Credit   (After completing both query Transaction will complete)

Transaction is a set of SQL queries of two or more than two query
Transaction Follows ACID Properties
A - Atomicity (All Succeed or None of them)
ROLLBACK , COMMIT
C - Consistency (Rules will be same as it is) 
I - Isolation (No Interference between transaction)
D - Durability (Permanent Once Commited)

*/
CREATE DATABASE bank;
USE bank;
CREATE TABLE accounts(
aid INT PRIMARY KEY AUTO_INCREMENT , 
aname VARCHAR(100) NOT NULL ,
balance DECIMAL(8,2) DEFAULT 0
);

INSERT INTO accounts VALUES
(101,'Rohan Singh',8000),
(102,'Simran',0),
(103,'Yogesh',2000);

SELECT * FROM accounts;

UPDATE accounts SET balance=balance-1000 WHERE aid=101;
UPDATE accounts SET balance=balance+1000 WHERE aid=102;

SET @var = 1000;
START TRANSACTION ;
UPDATE accounts SET balance=balance-@var WHERE aid=101;
UPDATE accounts SET balance=balance+@var WHERE aid=103;
SELECT * FROM accounts;
COMMIT ;
ROLLBACK;
