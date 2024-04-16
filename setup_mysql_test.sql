-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create the user if it doesn't exist and set the password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Revoke all privileges on performance_schema database
-- REVOKE ALL PRIVILEGES ON performance_schema.* FROM 'hbnb_dev'@'localhost';
-- Grant SELECT privilege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
