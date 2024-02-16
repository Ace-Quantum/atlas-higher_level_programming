-- makes a table auto gen blah blah blah

CREATE DATABASE IF NOT EXISTS hbtn_0c_0_usa;

CREATE TABLE IF NOT EXISTS hbtn_0c_0_usa.states(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
)