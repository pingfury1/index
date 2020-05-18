-- 2020-05-16

-- table groups

CREATE TABLE groups (
    group_id INT AUTO_INCREMENT PRIMARY KEY,
    group_name VARCHAR(50)
) DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- table items

CREATE TABLE items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(50),
    item_url VARCHAR(255),
    item_notice TEXT,
    item_logo_url VARCHAR(255),
    item_manual_name VARCHAR(50),
    item_manual_url VARCHAR(255),
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES groups (group_id) ON DELETE SET NULL
) DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
