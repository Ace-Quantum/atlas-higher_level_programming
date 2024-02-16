-- grants all permissions to a specified user

CREATE USER IF NOT EXISTS 'user_01_1'@'%' IDENTIFIED BY 'user_0d_1_pwd'

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%' WITH GRANT OPTION;