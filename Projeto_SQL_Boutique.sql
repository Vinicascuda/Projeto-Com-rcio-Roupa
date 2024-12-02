CREATE DATABASE projeto_sql_boutique;
USE projeto_sql_boutique;

CREATE TABLE Manager (
    ID_Manager INT AUTO_INCREMENT PRIMARY KEY,
    Name_Manager VARCHAR(100) NOT NULL,
    Email_Manager VARCHAR(100) NOT NULL UNIQUE,
    Tele_Manager VARCHAR(15)
    );
    
CREATE TABLE Client (
    ID_Client INT AUTO_INCREMENT PRIMARY KEY,
    Name_Client VARCHAR(100) NOT NULL,
    CEP_Client VARCHAR(20),
    User_Client VARCHAR(50) NOT NULL UNIQUE,
    Tele_Client VARCHAR(15),
    ID_Manager INT,
    FOREIGN KEY (ID_Manager) REFERENCES Manager(ID_Manager) ON DELETE SET NULL
);

CREATE TABLE Supplier (
    ID_Supplier INT AUTO_INCREMENT PRIMARY KEY,
    Name_Supplier VARCHAR(100) NOT NULL,
    Email_Supplier VARCHAR(100) NOT NULL UNIQUE,
    ID_Manager INT,
    FOREIGN KEY (ID_Manager) REFERENCES Manager(ID_Manager) ON DELETE SET NULL
);