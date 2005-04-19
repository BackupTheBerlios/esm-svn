drop database if exists @DBNAME@;
create database @DBNAME@;
GRANT ALL ON @DBNAME@.* TO @DBUSER@@localhost IDENTIFIED BY "@DBPASSWORD@";
