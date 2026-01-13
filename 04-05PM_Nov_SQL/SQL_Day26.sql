/*
Security And User Management

*/
# CREATING A NEW USER
CREATE USER 'user1'@'localhost' identified by '12345';

SELECT user FROM mysql.user;
GRANT SELECT ON sales.* TO 'user1'@'localhost';

use college;
SHOW TABLES;
GRANT SELECT ON college.employee TO
'user1'@'localhost';

GRANT INSERT,UPDATE ON college.employee TO
'user1'@'localhost';

GRANT DELETE ON college.employee TO
'user1'@'localhost';

SELECT * FROM employee;

GRANT ALL privileges ON college.* TO
'user1'@'localhost';

REVOKE ALL privileges ON college.* FROM 
'user1'@'localhost';


SHOW GRANTS FOR 'user1'@'localhost';
REVOKE SELECT ON sales.* FROM 'user1'@'localhost';
REVOKE ALL PRIVILEGES ON college.employee
FROM 'user1'@'localhost';

DROP USER 'user1'@'localhost';

# ROLES
CREATE ROLE 'read_only';
GRANT SELECT ON college.* TO 'read_only';

CREATE USER 'new_user'@'localhost' identified BY '1234';

GRANT 'read_only' TO 'new_user'@'localhost';
DROP USER 'new_user'@'localhost';

SHOW GRANTS FOR 'read_only';
# For activating user's role
SET DEFAULT ROLE 'read_only' TO 'new_user'@'localhost';

ALTER USER 'new_user'@'localhost' identified by '5536';

# NEED TO CREATE A NEW PASSWORD ON NEXT LOGIN
ALTER USER 'new_user'@'localhost' 
PASSWORD EXPIRE;

ALTER USER 'new_user'@'localhost' 
PASSWORD EXPIRE INTERVAL 90 DAY;

ALTER USER 'new_user'@'localhost' ACCOUNT LOCK;
ALTER USER 'new_user'@'localhost' ACCOUNT UNLOCK;


