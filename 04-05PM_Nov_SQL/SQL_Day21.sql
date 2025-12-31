/*
Transaction:- 
A transaction is a sequence of SQL statements that are executed as
one logical Unit of work.
Either all changes succeed (COMMIT) or none are applied (ROLLBACK).

10K
1- Deduct  
2- Credit  
if both done (COMMIT)
if none of these done (ROLLBACK)

- Updating multiple tables
- Handling banking , orders and inventory
- Preventing Partial updates on error or crashes

ACID Proprties
A - Automicity (All or Nothing) 
C - Consistency (Database rules remain valid)
I - Isolation (Concurrent transactions don't interface)
D - Durability (Commited data survives crashes) 

Basic Transaction Commands
Start a transaction
START TRANSACTION ;
--- SQL Statements; 

Commit (Save Changes)
COMMIT;

Rollback (Undo Changes)
ROLLBACK;

*/
DROP DATABASE bank;
CREATE DATABASE bank;
USE bank;
CREATE TABLE users(
aid INT PRIMARY KEY AUTO_INCREMENT , 
aname VARCHAR(100) NOT NULL , 
abal DECIMAL(8,2) NOT NULL
);

INSERT INTO users VALUES
(101,'Rahul Kumar',8753),
(102,'Mahes Kumar',0),
(103,'Suman Kumari',1000),
(104,'Yogesh Kumar',3000);

SELECT * FROM users;

UPDATE users SET abal=abal-1000 WHERE aid=101;
UPDATE users SET abal=abal+1000 WHERE aid=102;

START TRANSACTION;

UPDATE users SET abal=abal-1000 WHERE aid=101;
UPDATE users SET abal=abal+1000 WHERE aid=102;
COMMIT;
ROLLBACK;  