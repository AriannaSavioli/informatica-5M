### TESTO DELL'ESERCIZIO

Un centro sportivo vuole progettare una piattaforma web per la gestione delle attività sportive, per migliorare l'organizzazione e la partecipazione degli utenti.
Ciascun istruttore, una volta completata la registrazione alla piattaforma, può creare uno o più corsi sportivi (identificati da un nome e una disciplina: es. Yoga, Calcio) 
e aprire l’iscrizione ai propri corsi agli utenti tramite la condivisione del codice di iscrizione (link o QR-code).
Nella piattaforma è presente il catalogo delle attività sportive, classificate in base ad un elenco di discipline prestabilite (es: yoga, calcio, nuoto …): ciascun istruttore può selezionare una o più attività per includerle in un corso.
Per ogni attività è presente un titolo, una descrizione breve di massimo 160 caratteri, una descrizione estesa, il numero di sessioni disponibili e fino a tre immagini dell'attività.
Un utente si iscriverà sulla piattaforma ai corsi cui è stato invitato (es: Yoga, Calcio ...) tramite il relativo codice di iscrizione, e all’interno di ciascun corso troverà i dettagli delle attività sportive proposte dall'istruttore.
Partecipando a ciascuna attività, l'utente potrà accumulare punti fitness tramite la frequenza e il completamento delle sessioni.
Un punto fitness è un riconoscimento che viene assegnato al completamento di determinate sessioni o traguardi sportivi.
Attraverso il numero di punti fitness, raccolti man mano da un utente in ciascuna attività di quel corso, si può determinare una classifica per ciascuna attività e anche una classifica generale comprensiva di tutte le attività del corso;
l'istruttore può quindi seguire l’andamento degli utenti e supportarli individualmente nel raggiungimento dei loro obiettivi sportivi.

### DIAGRAMMA ER

```mermaid
erDiagram
    INSTRUCTOR {
        int ID
        string Name
        string Email
    }
    COURSE {
        int ID
        string Name
        string Discipline
        string RegistrationCode
    }
    ACTIVITY {
        int ID
        string Title
        string ShortDescription
        string LongDescription
        int SessionCount
        string Image1
        string Image2
        string Image3
    }
    USER {
        int ID
        string Name
        string Email
    }
    FITNESS_POINT {
        int ID
        int Points
    }
    COURSE_ACTIVITY {
        int CourseID
        int ActivityID
    }
    USER_COURSE {
        int UserID
        int CourseID
    }
    USER_ACTIVITY {
        int UserID
        int ActivityID
    }

    INSTRUCTOR ||--o{ COURSE : creates
    COURSE ||--o{ COURSE_ACTIVITY : includes
    ACTIVITY ||--o{ COURSE_ACTIVITY : part_of
    USER ||--o{ USER_COURSE : enrolls
    COURSE ||--o{ USER_COURSE : has
    USER ||--o{ USER_ACTIVITY : participates
    ACTIVITY ||--o{ USER_ACTIVITY : includes
    USER_ACTIVITY ||--o{ FITNESS_POINT : earns
```
### PROGETTAZIONE LOGICA

### TABELLE

- **INSTRUCTOR**: id `PK`, name, email
- **COURSE**: id `PK`, name, enrollment_code, instructor_id `FK` → INSTRUCTOR.id
- **ACTIVITY**: id `PK`, title, short_description, long_description, sessions, course_id `FK` → COURSE.id
- **USER**: id `PK`, name, email
- **IMAGE**: id `PK`, url, activity_id `FK` → ACTIVITY.id
- **DISCIPLINE**: id `PK`, name
- **ENROLLMENT**: user_id `FK` → USER.id, course_id `FK` → COURSE.id, `PK`(user_id, course_id)
- **FITNESS_POINT**: id `PK`, points, award_date, user_id `FK` → USER.id, activity_id `FK` → ACTIVITY.id

### CREATE QUERY

```sql
CREATE TABLE INSTRUCTOR (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE COURSE (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    enrollment_code VARCHAR(255),
    instructor_id INT,
    FOREIGN KEY (instructor_id) REFERENCES INSTRUCTOR(id)
);

CREATE TABLE ACTIVITY (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    short_description VARCHAR(160),
    long_description TEXT,
    sessions INT,
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES COURSE(id)
);

CREATE TABLE USER (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE IMAGE (
    id INT PRIMARY KEY,
    url VARCHAR(255),
    activity_id INT,
    FOREIGN KEY (activity_id) REFERENCES ACTIVITY(id)
);

CREATE TABLE DISCIPLINE (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE ENROLLMENT (
    user_id INT,
    course_id INT,
    PRIMARY KEY (user_id, course_id),
    FOREIGN KEY (user_id) REFERENCES USER(id),
    FOREIGN KEY (course_id) REFERENCES COURSE(id)
);

CREATE TABLE FITNESS_POINT (
    id INT PRIMARY KEY,
    points INT,
    award_date DATE,
    user_id INT,
    activity_id INT,
    FOREIGN KEY (user_id) REFERENCES USER(id),
    FOREIGN KEY (activity_id) REFERENCES ACTIVITY(id)
);
```

### INSERT QUERY

```sql
INSERT INTO INSTRUCTOR (id, name, email) VALUES
(1, 'John Smith', 'john.smith@example.com'),
(2, 'Jane Doe', 'jane.doe@example.com');

INSERT INTO COURSE (id, name, enrollment_code, instructor_id) VALUES
(1, 'Yoga Basics', 'YOGA101', 1),
(2, 'Advanced Soccer', 'SOCCER201', 2);

INSERT INTO ACTIVITY (id, title, short_description, long_description, sessions, course_id) VALUES
(1, 'Morning Yoga', 'Basic yoga poses for beginners', 'Detailed description of yoga poses...', 10, 1),
(2, 'Soccer Training', 'Soccer drills and techniques', 'Detailed soccer training plan...', 12, 2);

INSERT INTO USER (id, name, email) VALUES
(1, 'Alice Johnson', 'alice@example.com'),
(2, 'Bob Wilson', 'bob@example.com');

INSERT INTO IMAGE (id, url, activity_id) VALUES
(1, 'yoga1.jpg', 1),
(2, 'soccer1.jpg', 2);

INSERT INTO DISCIPLINE (id, name) VALUES
(1, 'Yoga'),
(2, 'Soccer');

INSERT INTO ENROLLMENT (user_id, course_id) VALUES
(1, 1),
(2, 2);

INSERT INTO FITNESS_POINT (id, points, award_date, user_id, activity_id) VALUES
(1, 10, '2023-01-10', 1, 1),
(2, 15, '2023-01-15', 2, 2);
```
