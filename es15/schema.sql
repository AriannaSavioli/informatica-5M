CREATE TABLE CAMERA (
    numero INT PRIMARY KEY,
    tipo VARCHAR(50),
    disponibile BOOLEAN,
    prezzo FLOAT,
    numero_posti INT
);

CREATE TABLE PRENOTAZIONE (
    id INT PRIMARY KEY AUTO_INCREMENT,
    camera_numero INT,
    cliente VARCHAR(100),
    data_inizio DATE,
    data_fine DATE,
    FOREIGN KEY (camera_numero) REFERENCES CAMERA(numero)
);