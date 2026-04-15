# 🚀 Project Management Backend (Django REST API)

## 📌 Overview

This is a **Project Management Backend System** built using **Django and Django REST Framework**.

The system allows:

* User Management (CRUD)
* Project Management (CRUD)
* Task Management (CRUD)
* Task Assignment (User ↔ Project ↔ Task relationships)

This project was developed as part of an **internship assessment** to demonstrate backend development skills, API design, and database relationships.

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework (DRF)
* SQLite (default database)
* Postman (API testing)

---

## 📂 Project Structure

project-management-backend/
│
├── core/                 # Main app (User, Project, Task)
├── project_management/  # Project settings
├── manage.py
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

git clone https://github.com/Jasbirsingh17050/project-management-backend.git

cd project-management-backend

---

### 2️⃣ Create virtual environment

python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

---

### 3️⃣ Install dependencies

pip install -r requirements.txt

---

### 4️⃣ Apply migrations

python manage.py makemigrations
python manage.py migrate

---

### 5️⃣ Run server

python manage.py runserver

Server will run at:
http://127.0.0.1:8000/

---

## 🔗 API Endpoints

### 👤 User APIs

* POST /users/ → Create user
* GET /users/ → List users
* PUT /users/{id}/ → Update user
* DELETE /users/{id}/ → Delete user

---

### 📁 Project APIs

* POST /projects/
* GET /projects/
* PUT /projects/{id}/
* DELETE /projects/{id}/

---

### ✅ Task APIs

* POST /tasks/
* GET /tasks/
* PUT /tasks/{id}/
* DELETE /tasks/{id}/

---

## 🔄 Relationships

* One **User** can have multiple Tasks
* One **Project** can have multiple Tasks
* Each Task:

  * belongs to one Project
  * is assigned to one User

---

## ✅ Validation Rules

* Task must have valid user
* Task must have valid project
* Status must be:

  * pending
  * in-progress
  * completed

---

## 🧪 Testing

APIs were tested using **Postman**.

---

## 💡 Key Learnings

* Django ORM relationships (ForeignKey)
* REST API design
* CRUD operations
* Clean code structure
* Git & GitHub workflow

---

## 👨‍💻 Author

Jasbir Singh
GitHub: https://github.com/Jasbirsingh17050

---

## ⭐ Future Improvements

* Authentication (JWT)
* Pagination
* Filtering & Search
* Deployment (Render / AWS)
## 📬 Postman Collection

The Postman collection is included in this repository:

`project_management_postman_collection.json`

Import this file into Postman to test all APIs easily.
---
