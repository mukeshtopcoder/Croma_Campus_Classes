/*
Transactions:- 
A transaction is a group of SQL queries executed together.
if all successed -> The whole transaction is saved
if any fail -> everything is undone

This ensures data accuracy, consistency and reliability
ACID Properties:-
A - Atomicity (All queries succeed or all fail)
C - Consistency (Data remains valid before and after transaction)
I - Isolation (Multiple transactions don't affect each other)
D - Durability (After commit , data stays saved even if system crashes)

*/
CREATE DATABASE bank;
USE bank;
CREATE TABLE accounts(
aid INT PRIMARY KEY AUTO_INCREMENT , 
aname VARCHAR(100) NOT NULL , 
balance DECIMAL(8,2) NOT NULL CHECK (balance>0)
);
INSERT INTO accounts VALUES
(101,'Mohit',4000),
(102,'Naresh',1000),
(103,'Sonu',2000);

UPDATE accounts SET balance=balance-1000 WHERE aid=101;
UPDATE accounts SET balance=balance+1000 WHERE aid=102;

SELECT * FROM accounts;

START TRANSACTION;
UPDATE accounts SET balance=balance-1000 WHERE aid=101;
UPDATE accounts SET balance=balance+1000 WHERE aid=102;
COMMIT;
ROLLBACK;

SELECT * FROM accounts;

START TRANSACTION;
UPDATE accounts SET balance=balance-1000 WHERE aid=101;
UPDATE accounts SET balance=balance+1000 WHERE aid=102;
SAVEPOINT t1;
UPDATE accounts SET balance=balance-2000 WHERE aid=102;
UPDATE accounts SET balance=balance+2000 WHERE aid=103;
ROLLBACK TO t1;
ROLLBACK;
COMMIT;

CREATE TABLE acc_log(
logid INT PRIMARY KEY AUTO_INCREMENT,
acc_deb INT,
acc_cre INT,
balance DECIMAL(8,2)
);
SELECT * FROM accounts;
DELIMITER $$
CREATE TRIGGER transaction_log
AFTER INSERT ON accounts
FOR EACH ROW
BEGIN 
-- INSERT INTO acc_log(acc_deb,acc_cre,balance) VALUE();
END $$ DELIMITER ;