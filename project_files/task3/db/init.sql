CREATE DATABASE IF NOT EXISTS test1;
use test1;
CREATE TABLE dataa (time TEXT , cpu TEXT  , ram TEXT  , disk TEXT  ) ;
CREATE USER 'alaa'@'%' IDENTIFIED WITH mysql_native_password BY '123';
GRANT ALL PRIVILEGES ON *.* TO 'alaa'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

