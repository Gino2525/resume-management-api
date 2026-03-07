# Resume Management API

A Resume Management System built using **FastAPI** that allows HR users to upload, manage, search, and delete candidate resumes through REST APIs and a simple web interface.

---
simple setup to run__

pip install -r requirements.txt

uvicorn app.main:app --reload

http://127.0.0.1:8000/frontend/

Database & Data Persistence

This application includes full data persistence for all submitted candidate information.

Backend Stack

Framework: FastAPI

ORM: SQLAlchemy

Database: SQLite

How Data Is Stored__

When a candidate form is submitted:

Resume file

Uploaded files are stored on the server at:

app/uploads/

Candidate details

All form fields (name, contact info, education, experience, skills, etc.)

Persisted in a relational database using SQLAlchemy ORM

Stored inside a local SQLite database file

Database Creation__

The database is automatically created on first application startup.

Base.metadata.create_all(bind=engine)

If the database file does not exist, it is generated automatically

Required tables are created programmatically

Generated database file:

resume.db
## Features

* Upload candidate details with resume (PDF/DOC/DOCX)
* Store candidate metadata
* Filter candidates by skill, experience, and graduation year
* View candidate list
* Delete candidates
* Simple frontend dashboard
* REST API documentation via Swagger UI

---

## Project Structure

```
Assignment/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       └── candidate.py
│
├── frontend/
│   └── index.html
│
├── requirements.txt
└── README.md
```

---

## Requirements

* Python 3.10+
* pip

---

## Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/Gino2525/resume-management-api.git
cd resume-management-api
```

---

### 2. Create Virtual Environment (Recommended)

Windows:

```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Run the Application

```
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## Access Application

### API Documentation (Swagger UI)

```
http://127.0.0.1:8000/docs
```

---

### Frontend Dashboard

```
http://127.0.0.1:8000/frontend/index.html
```

---

## Database

* SQLite database (`resume.db`) is automatically created on first run.
* No manual setup required.

---

## Supported File Types

* PDF
* DOC
* DOCX

---

## Technologies Used

* FastAPI
* SQLAlchemy
* SQLite
* HTML / CSS / JavaScript
* Uvicorn

---

## Notes

* Uploaded resumes are stored locally in the uploads directory.
* `.gitignore` excludes database and uploaded files for security.

---


