/*

*/
USE college;
CREATE TABLE employees (
 emp_id INT PRIMARY KEY AUTO_INCREMENT,
 name VARCHAR(100),
 salary DECIMAL(10,2),
 department VARCHAR(50)
);
CREATE TABLE salary_log (
 log_id INT PRIMARY KEY AUTO_INCREMENT,
 emp_id INT,
 old_salary DECIMAL(10,2),
 new_salary DECIMAL(10,2),
 changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //
CREATE TRIGGER update_sal
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
	IF OLD.salary <> NEW.salary THEN
		INSERT INTO salary_log(emp_id,old_salary,new_salary)
		VALUE(OLD.emp_id , OLD.salary , NEW.salary);
	END IF;
END // DELIMITER ;



# Q2 
CREATE TABLE accounts (
 acc_id INT PRIMARY KEY AUTO_INCREMENT,
 holder_name VARCHAR(100),
 balance DECIMAL(10,2)
);
INSERT INTO accounts VALUE(101,'Anu',2000);
DELIMITER $$ 
CREATE TRIGGER prevent_negative
BEFORE UPDATE ON accounts
FOR EACH ROW
BEGIN
	IF NEW.balance < 0 THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = "BALANCE CAN NOT BE NEGATIVE";
	END IF;
END $$ DELIMITER ;

UPDATE accounts SET balance=-1000;

CREATE TABLE orders (
 order_id INT PRIMARY KEY AUTO_INCREMENT,
 total_amount DECIMAL(10,2) DEFAULT 0
);
CREATE TABLE order_items (
 item_id INT PRIMARY KEY AUTO_INCREMENT,
 order_id INT,
 quantity INT,
 price DECIMAL(10,2)
);

DELIMITER $$
CREATE TRIGGER cal_bill
AFTER INSERT ON order_items
FOR EACH ROW
BEGIN
	INSERT INTO orders VALUE(NEW.order_id,NEW.quantity*NEW.price);
END $$ DELIMITER ;

