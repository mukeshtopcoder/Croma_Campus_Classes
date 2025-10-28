USE bank;
SHOW TABLES;
SELECT * FROM accounts;

UPDATE accounts SET balance=balance-500 WHERE aid=101;
UPDATE accounts SET balance=balance+500 WHERE aid=103;

START TRANSACTION;
UPDATE accounts SET balance=balance-500 WHERE aid=101;
UPDATE accounts SET balance=balance+500 WHERE aid=103;
SELECT * FROM accounts;
ROLLBACK;
COMMIT;

START TRANSACTION;
UPDATE accounts SET balance=balance-500 WHERE aid=101;
UPDATE accounts SET balance=balance+500 WHERE aid=103;
SAVEPOINT tran2;
UPDATE accounts SET balance=balance-500 WHERE aid=102;
UPDATE accounts SET balance=balance+500 WHERE aid=103;
COMMIT;
SELECT * FROM accounts;
ROLLBACK;
ROLLBACK TO tran2;

SET SQL_SAFE_UPDATES=0;

