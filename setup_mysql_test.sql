-- Create the test database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the test user with the specified password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to the user hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema database to the user hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to ensure the changes are applied
FLUSH PRIVILEGES;

