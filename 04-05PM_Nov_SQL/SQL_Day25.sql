/*

*/
CREATE DATABASE sales;
USE sales;
CREATE TABLE sales_data(
segment VARCHAR(100) , 
country VARCHAR(100) ,
product VARCHAR(100) ,
discount_band VARCHAR(100) ,
units_sold VARCHAR(100) ,
manufacturing_price VARCHAR(100) ,
sale_price VARCHAR(100) ,
gross_sales VARCHAR(100) ,
discounts VARCHAR(100) ,
sales VARCHAR(100) ,
cogs VARCHAR(100) ,
profit VARCHAR(100) ,
dates VARCHAR(20) ,
month_number INT , 
month_name VARCHAR(20) , 
years INT
);
DROP TABLE sales_data;

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Financial_Sample.csv"
INTO TABLE sales_data
FIELDS TERMINATED BY ","
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS ;

SELECT * FROM sales_data;

# Data Cleaning
UPDATE sales_data SET manufacturing_price = REPLACE(manufacturing_price,"$","");

UPDATE sales_data SET manufacturing_price = REPLACE(manufacturing_price,"$","");

SELECT COUNT(*) FROM sales_data WHERE manufacturing_price="";

ALTER TABLE sales_data MODIFY manufacturing_price DECIMAL(8,2);

SELECT avg(manufacturing_price) FROM sales_data;

SELECT COUNT(*) FROM sales_data WHERE segment="";

SELECT segment,sum(profit) FROM sales_data GROUP BY segment;
SELECT segment,sum(profit) FROM sales_data GROUP BY segment;

SELECT * FROM sales_data;

UPDATE sales_data SET profit = REPLACE(profit,"$","");
UPDATE sales_data SET profit = REPLACE(profit,",","");
UPDATE sales_data SET profit = REPLACE(profit,"-",0);
UPDATE sales_data SET profit = REPLACE(profit,"(","-");
UPDATE sales_data SET profit = REPLACE(profit,")","");

ALTER TABLE sales_data MODIFY profit DECIMAL(8,2);


SELECT COUNT(*) FROM sales_data WHERE segment="";
SELECT segment,sum(profit) FROM sales_data GROUP BY segment;
UPDATE sales_data SET segment="Government" WHERE segment="";

