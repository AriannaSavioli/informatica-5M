### TESTO DELL'ESERCIZIO

Una clinica medica vuole progettare una piattaforma web per la gestione delle attività cliniche, al fine di migliorare l'organizzazione e l'efficienza dei servizi offerti ai pazienti.
Ciascun medico, una volta completata la registrazione alla piattaforma, può gestire il proprio calendario di visite, specificando le disponibilità settimanali e le specializzazioni offerte (es. Cardiologia, Dermatologia).
Nella piattaforma è presente un elenco delle specializzazioni mediche disponibili nella clinica (es: cardiologia, dermatologia, ortopedia …). Ogni medico può selezionare una o più specializzazioni per indicare le proprie competenze.
Per ogni visita medica, il medico può inserire una descrizione dettagliata del tipo di visita, la durata prevista e le eventuali preparazioni richieste al paziente.
Un paziente può registrarsi sulla piattaforma e prenotare una visita scegliendo tra le disponibilità dei medici. Durante la prenotazione, il paziente può specificare il motivo della visita e allegare eventuali documenti medici rilevanti.
Partecipando a ciascuna visita, il paziente riceverà diagnosi e trattamenti personalizzati. Il medico potrà aggiornare la cartella clinica del paziente con i dettagli della visita, le prescrizioni e le raccomandazioni per il follow-up.
Attraverso la piattaforma, i pazienti possono visualizzare lo storico delle proprie visite, ricevere notifiche per le visite future e accedere ai propri dati medici in qualsiasi momento.
La piattaforma permette inoltre di gestire le risorse della clinica, come le sale visite e le attrezzature mediche, per ottimizzare l'uso degli spazi e dei tempi. I responsabili della clinica possono monitorare l'occupazione delle sale 
e pianificare la manutenzione delle attrezzature.
Infine, la piattaforma offre strumenti di comunicazione tra medici e pazienti, come messaggistica sicura e videochiamate, per facilitare il contatto e il supporto continuo.

### DIAGRAMMA ER

```mermaid
erDiagram

    DOCTOR {
        int ID PK
        string Name
    }
    PATIENT {
        int ID PK
        string FirstName
        string LastName
        string Email
        string Address
    }
    APPOINTMENT {
        int ID PK
        date AppointmentDate
        string Description
        int Duration
        string Preparation
        int DoctorID FK
        int PatientID FK
    }
    MEDICAL_RECORD {
        int ID PK
        int PatientID FK
        int DoctorID FK
        date VisitDate
        string Diagnosis
        string Treatment
        string FollowUp
    }
    SPECIALIZATION {
        int ID PK
        string Name
    }
    DOCTOR_SPECIALIZATION {
        int DoctorID PK, FK
        int SpecializationID PK, FK
    }
    ROOM {
        int ID PK
        string Name
        string Equipment
    }
    EQUIPMENT {
        int ID PK
        string Name
        string MaintenanceSchedule
    }

    DOCTOR ||--o{ APPOINTMENT : schedules
    PATIENT ||--o{ APPOINTMENT : books
    DOCTOR ||--o{ MEDICAL_RECORD : updates
    PATIENT ||--o{ MEDICAL_RECORD : has
    DOCTOR ||--o{ DOCTOR_SPECIALIZATION : has
    SPECIALIZATION ||--o{ DOCTOR_SPECIALIZATION : includes
    ROOM ||--o{ APPOINTMENT : hosts
    ROOM ||--o{ EQUIPMENT : contains
```

### Progettazione Logica

### Tabelle

- **DOCTOR**: id `PK`, name, specializations
- **PATIENT**: id `PK`, first_name, last_name, email, address
- **APPOINTMENT**: id `PK`, appointment_date, description, duration, preparation, doctor_id `FK` → DOCTOR.id, patient_id `FK` → PATIENT.id
- **MEDICAL_RECORD**: id `PK`, patient_id `FK` → PATIENT.id, doctor_id `FK` → DOCTOR.id, visit_date, diagnosis, treatment, follow_up
- **SPECIALIZATION**: id `PK`, name
- **DOCTOR_SPECIALIZATION**: doctor_id `FK` → DOCTOR.id, specialization_id `FK` → SPECIALIZATION.id, `PK`(doctor_id, specialization_id)
- **ROOM**: id `PK`, name, equipment
- **EQUIPMENT**: id `PK`, name, maintenance_schedule

### Creazione delle Tabelle in SQL

```sql
CREATE TABLE DOCTOR (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    specializations TEXT
);

CREATE TABLE PATIENT (
    id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    address TEXT
);

CREATE TABLE APPOINTMENT (
    id INT PRIMARY KEY,
    appointment_date DATE,
    description TEXT,
    duration INT,
    preparation TEXT,
    doctor_id INT,
    patient_id INT,
    FOREIGN KEY (doctor_id) REFERENCES DOCTOR(id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT(id)
);

CREATE TABLE MEDICAL_RECORD (
    id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    visit_date DATE,
    diagnosis TEXT,
    treatment TEXT,
    follow_up TEXT,
    FOREIGN KEY (patient_id) REFERENCES PATIENT(id),
    FOREIGN KEY (doctor_id) REFERENCES DOCTOR(id)
);

CREATE TABLE SPECIALIZATION (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE DOCTOR_SPECIALIZATION (
    doctor_id INT,
    specialization_id INT,
    PRIMARY KEY (doctor_id, specialization_id),
    FOREIGN KEY (doctor_id) REFERENCES DOCTOR(id),
    FOREIGN KEY (specialization_id) REFERENCES SPECIALIZATION(id)
);

CREATE TABLE ROOM (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    equipment TEXT
);

CREATE TABLE EQUIPMENT (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    maintenance_schedule TEXT
);
```

### Inserimento dei Dati in SQL

```sql
INSERT INTO DOCTOR (id, name, specializations) VALUES
(1, 'Dr. John Smith', 'Cardiology, Dermatology'),
(2, 'Dr. Jane Doe', 'Orthopedics, Pediatrics');

INSERT INTO PATIENT (id, first_name, last_name, email, address) VALUES
(1, 'Alice', 'Johnson', 'alice.johnson@example.com', '123 Main St'),
(2, 'Bob', 'Brown', 'bob.brown@example.com', '456 Elm St');

INSERT INTO APPOINTMENT (id, appointment_date, description, duration, preparation, doctor_id, patient_id) VALUES
(1, '2023-01-01', 'Routine check-up', 30, 'None', 1, 1),
(2, '2023-01-02', 'Follow-up visit', 45, 'Fasting required', 2, 2);

INSERT INTO MEDICAL_RECORD (id, patient_id, doctor_id, visit_date, diagnosis, treatment, follow_up) VALUES
(1, 1, 1, '2023-01-01', 'Healthy', 'None', 'Annual check-up'),
(2, 2, 2, '2023-01-02', 'Minor injury', 'Rest and medication', 'Follow-up in 2 weeks');

INSERT INTO SPECIALIZATION (id, name) VALUES
(1, 'Cardiology'),
(2, 'Dermatology'),
(3, 'Orthopedics'),
(4, 'Pediatrics');

INSERT INTO DOCTOR_SPECIALIZATION (doctor_id, specialization_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4);

INSERT INTO ROOM (id, name, equipment) VALUES
(1, 'Room 101', 'EKG Machine, Ultrasound'),
(2, 'Room 102', 'X-Ray Machine, MRI');

INSERT INTO EQUIPMENT (id, name, maintenance_schedule) VALUES
(1, 'EKG Machine', 'Monthly'),
(2, 'Ultrasound', 'Quarterly'),
(3, 'X-Ray Machine', 'Bi-Annually'),
(4, 'MRI', 'Annually');
```
