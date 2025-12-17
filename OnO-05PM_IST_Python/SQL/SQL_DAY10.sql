/*
Transaction:-
A transaction is a set of SQL statements that execute as 
a single unit work.
Either all statements succeed or none of them apply.

This ensures data integirty, especially in banking,
payments, bookings , inventory etc

ACID
A -> Atomicity (All operations succeed or none)
C -> Consitency (Data must remain valid before and after transaction)
I -> Isolation (Transaction should not affect each other)
D -> Durablity (Once committed, data is permanent)

# Basic Commands
START TRANSACTION;
write your SQL queries
COMMIT;
Saves all the changes permanently
ROLLBACK;
Undo all changes since the transaction started
*/

USE bank;
SHOW TABLES;
SELECT * FROM accounts;

UPDATE accounts SET balance=balance-1000 WHERE aid=102;
UPDATE accounts SET balance=balance+1000 WHERE aid=101;

START TRANSACTION;
UPDATE accounts SET balance=balance-1000 WHERE aid=102;
UPDATE accounts SET balance=balance+1000 WHERE aid=101;
COMMIT;
ROLLBACK;

TRUNCATE accounts;

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