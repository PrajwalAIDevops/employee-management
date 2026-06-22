
CREATE DATABASE employee_db;
USE employee_db;
CREATE TABLE employee(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),email VARCHAR(120),phone VARCHAR(20),
department VARCHAR(100),designation VARCHAR(100),
salary DECIMAL(10,2),doj DATE);
