USE flipkart;
SHOW TABLES;
SELECT * FROM employee;

# SUB-Query
# SELECT -- FROM -- WHERE column = value;
# SELECT -- FROM -- WHERE column = (SELECT - FROM -- WHERE condition);

# Highest Salary 
SELECT MAX(esal) FROM employee;
# We got => 86200

# Second Highest Salary
SELECT MAX(esal) FROM employee WHERE esal<86200;
# 75670 Second Highest Salary

# Second Highest Salary Using SUB-QUERY
SELECT MAX(esal) FROM employee 
WHERE esal<(SELECT MAX(esal) FROM employee);

# EMPLOYEE's Average Salary
SELECT AVG(esal) FROM employee;
# We got 33115

# Employee who are earning above average salary
SELECT * FROM employee WHERE esal>33115;
SELECT * FROM employee
WHERE esal>(SELECT AVG(esal) FROM employee);

# IT edesg's Average Salary
SELECT AVG(esal) FROM employee WHERE edesg='IT';
# WE GOT 44922
SELECT * FROM employee WHERE esal>(SELECT AVG(esal)
FROM employee WHERE edesg='IT') AND edesg='IT';

# No of employees in edesg
SELECT edesg,count(*) FROM employee GROUP BY edesg;
SELECT edesg,MAX(esal) FROM employee GROUP BY edesg;

