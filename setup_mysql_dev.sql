-- Setup a mysql server for HBNB project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates a user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants all privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Greants privileges for performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
