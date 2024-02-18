-- forgot to do this one 

CREATE DATABASE IF NOT EXISTS htbn_0d_2

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd'
GRANT SELECT on htbn_0d_2.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
