-- converts a specific database a MySQL server to UTF-8

USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHAR SET utf8mb4 COLLATE utf8mb4_unicode_ci
