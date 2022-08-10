DROP DATABASE IF EXISTS users_db;

CREATE DATABASE IF NOT EXISTS users_db;

CREATE USER 'vsec'@'%' IDENTIFIED WITH caching_sha2_password BY 'pass';

GRANT ALL PRIVILEGES ON users_db.* TO 'vsec'@'%';

FLUSH PRIVILEGES;

USE users_db;

CREATE TABLE users (username text, password text);

INSERT INTO `users` (`username`, `password`)
VALUES 
    ('freddy_frog', 'pass123'), 
    ('sally_likes_toads', 'toad'), 
    ('bob_bungus', 'cheerios');


