-- grants all permissions to a specified user

SELECT user FROM mysql.user;

CREATE USER IF NOT EXISTS 'user_01_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';