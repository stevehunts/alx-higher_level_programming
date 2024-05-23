-- 1-create_user.sql
-- Creates the user user_0d_1 with all privileges if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges on the entire server to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Applies the changes
FLUSH PRIVILEGES;
