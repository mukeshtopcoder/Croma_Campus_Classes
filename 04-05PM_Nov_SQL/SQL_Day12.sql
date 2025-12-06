USE college;
SHOW TABLES;
CREATE TABLE student(
sname VARCHAR(100) NOT NULL ,
course VARCHAR(100) NOT NULL
);
INSERT INTO student VALUES
("Rahul",'BTech');

SELECT * FROM student;
SELECT sname FROM student ORDER BY sname;

SELECT  sname,count(sname) FROM student GROUP BY sname
HAVING count(sname)>1;

SELECT s1.* FROM student s1
JOIN ( SELECT sname,count(*) FROM student
GROUP BY sname HAVING count(*)>1 ) s2
ON s1.sname = s2.sname;

SELECT sname,course , count(*) FROM student
GROUP BY sname,course HAVING count(*)>1;

SELECT *, count(*) FROM student
GROUP BY sname,course HAVING count(*)>1; 

