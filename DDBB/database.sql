CREATE DATABASE jenkins;

CREATE TABLE audit (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Aplication VARCHAR(50) NOT NULL,
        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Repository VARCHAR(150) NOT NULL,
        End ENUM('Good', 'Bad') NOT NULL,
        Branch VARCHAR(100) NOT NULL
);

CREATE TABLE despliegues (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Aplication VARCHAR(50) NOT NULL,
        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Repository VARCHAR(150) NOT NULL,
        Ends ENUM('Bien', 'Mal') NOT NULL,
        Branch VARCHAR(100) NOT NULL,
        Path VARCHAR(100) NOT NULL,
        ServerName VARCHAR(100) NOT NULL
    );


CREATE DATABASE SensorData;

    CREATE TABLE data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Temperatura Double NOT NULL,
        Posicion VARCHAR(50) NOT NULL,
        Nombre VARCHAR(50) NOT NULL,
        Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    );

    CREATE TABLE sensor (
        Name VARCHAR(50) PRIMARY KEY,
        Batery Double NOT NULL,
        Estado ENUM('Active', 'Desactivate') NOT NULL
    );