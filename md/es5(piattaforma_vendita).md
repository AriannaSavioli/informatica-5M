### TESTO DELL'ESERCIZIO 

Una piattaforma di e-commerce vuole creare un sistema per gestire i prodotti, i clienti, gli ordini e le recensioni. 
Il sistema deve essere in grado di tenere traccia dei prodotti disponibili, dei clienti registrati, degli ordini effettuati e delle recensioni dei prodotti.

### REQUISITI

1. Ogni prodotto ha un ID, un nome, una descrizione, un prezzo e una categoria.
2. Ogni cliente ha un ID, un nome, un cognome, un'email e un indirizzo.
3. Ogni ordine ha un ID, una data di ordine, una data di consegna prevista e uno stato (in elaborazione, spedito, consegnato).
4. Ogni recensione ha un ID, un punteggio, una data e un commento.
5. Un cliente può effettuare più ordini, ma un ordine è associato a un solo cliente.
6. Un ordine può contenere più prodotti, e un prodotto può essere presente in più ordini.
7. Un cliente può scrivere più recensioni per diversi prodotti, ma una recensione è unica per ogni cliente e prodotto.

### DIAGRAMMA ER

```mermaid

erDiagram
    PRODOTTO {
        int ID PK
        string Nome
        string Descrizione
        float Prezzo
        string Categoria
    }
    CLIENTE {
        int ID PK
        string Nome
        string Cognome
        string Email
        string Indirizzo
    }
    ORDINE {
        int ID PK
        date DataOrdine
        date DataConsegna
        string Stato
        int ClienteID FK
    }
    RECENSIONE {
        int ID PK
        int Punteggio
        date Data
        string Commento
        int ClienteID FK
        int ProdottoID FK
    }
    ORDINE_PRODOTTO {
        int OrdineID PK ,FK
        int ProdottoID PK, FK
        int Quantita
    }

    CLIENTE ||--o{ ORDINE : effettua
    ORDINE ||--o{ ORDINE_PRODOTTO : contiene
    PRODOTTO ||--o{ ORDINE_PRODOTTO : incluso_in
    CLIENTE ||--o{ RECENSIONE : scrive
    PRODOTTO ||--o{ RECENSIONE : riceve

```

### PROGETTAZIONE LOGICA

### TABELLE

- **PRODOTTO**: id `PK`, nome, descrizione, prezzo, categoria
- **CLIENTE**: id `PK`, nome, cognome, email, indirizzo
- **ORDINE**: id `PK`,  data_ordine, data_consegna, stato, cliente_id `FK` → CLIENTE.id
- **RECENSIONE**: id `PK`, punteggio, data, commento, cliente_id `FK` → CLIENTE.id, prodotto_id `FK` → PRODOTTO.id
- **ORDINE_PRODOTTO**: ordine_id `FK` → ORDINE.id, prodotto_id `FK` → PRODOTTO.id, quantita, `PK`(ordine_id, prodotto_id)

### CREATE QUERY

```sql

CREATE TABLE PRODOTTO (
    id INT PRIMARY KEY,
    nome VARCHAR(255),
    descrizione TEXT,
    prezzo DECIMAL(10, 2),
    categoria VARCHAR(255)
);

CREATE TABLE CLIENTE (
    id INT PRIMARY KEY,
    nome VARCHAR(255),
    cognome VARCHAR(255),
    email VARCHAR(255),
    indirizzo TEXT
);

CREATE TABLE ORDINE (
    id INT PRIMARY KEY,
    data_ordine DATE,
    data_consegna DATE,
    stato VARCHAR(50),
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES CLIENTE(id)
);

CREATE TABLE RECENSIONE (
    id INT PRIMARY KEY,
    punteggio INT,
    data DATE,
    commento TEXT,
    cliente_id INT,
    prodotto_id INT,
    FOREIGN KEY (cliente_id) REFERENCES CLIENTE(id),
    FOREIGN KEY (prodotto_id) REFERENCES PRODOTTO(id)
);

CREATE TABLE ORDINE_PRODOTTO (
    ordine_id INT,
    prodotto_id INT,
    quantita INT,
    PRIMARY KEY (ordine_id, prodotto_id),
    FOREIGN KEY (ordine_id) REFERENCES ORDINE(id),
    FOREIGN KEY (prodotto_id) REFERENCES PRODOTTO(id)
);

```

### INSERT QUERY

```sql

INSERT INTO PRODOTTO (id, nome, descrizione, prezzo, categoria) VALUES
(1, 'Laptop', 'Laptop ad alte prestazioni', 999.99, 'Elettronica'),
(2, 'Smartphone', 'Smartphone di ultima generazione', 699.99, 'Elettronica');

INSERT INTO CLIENTE (id, nome, cognome, email, indirizzo) VALUES
(1, 'Giovanni', 'Rossi', 'giovanni.rossi@example.com', 'Via Roma 123'),
(2, 'Maria', 'Bianchi', 'maria.bianchi@example.com', 'Via Milano 456');

INSERT INTO ORDINE (id, data_ordine, data_consegna, stato, cliente_id) VALUES
(1, '2023-01-01', '2023-01-05', 'spedito', 1),
(2, '2023-01-02', '2023-01-06', 'in elaborazione', 2);

INSERT INTO RECENSIONE (id, punteggio, data, commento, cliente_id, prodotto_id) VALUES
(1, 5, '2023-01-10', 'Prodotto eccellente!', 1, 1),
(2, 4, '2023-01-11', 'Molto buono, ma un po\' costoso.', 2, 2);

INSERT INTO ORDINE_PRODOTTO (ordine_id, prodotto_id, quantita) VALUES
(1, 1, 1),
(2, 2, 2);

```
