CREATE DATABASE bank;
USE bank;
CREATE TABLE accounts(
aid INT PRIMARY KEY AUTO_INCREMENT , 
aname VARCHAR(20) NOT NULL , 
balance DECIMAL(8,2) NOT NULL
); 

INSERT INTO accounts VALUES
(5536 , 'Aman Kumar' , 26000),
(5537 , 'Mohit Singh' , 72000),
(5538 , 'Rahul Yadav' , 25000);

SELECT * FROM accounts;
UPDATE accounts SET balance = balance-5000 WHERE aid = 5536; 
UPDATE accounts SET balance = balance+5000 WHERE aid = 5538; 

# TRANSACTION
START TRANSACTION;
-- EXECUTE YOUR QUERIES
COMMIT;
ROLLBACK;

SELECT * FROM accounts;
START TRANSACTION;
UPDATE accounts SET balance = balance-5000 WHERE aid = 5536; 
UPDATE accounts SET balance = balance+5000 WHERE aid = 5538; 
COMMIT;  # FOR PERMANENT SAVE
ROLLBACK;  # FOR UNDO/UNSAVE THE QUERY
