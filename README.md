# 📊 Finance Management API

A lightweight yet powerful API for managing personal and small business finances. Easily track income, expenses, budgets, and financial goals in a secure and organized way.

---

## 🚀 Key Features

- **🔐 Full User Authentication** – Secure user registration and JWT-based login system.
- **💳 Transactions & Budgets CRUD** – Create, Retrieve, Update, and Delete operations for full financial control.
- **📈 Financial Reports** – Monthly summary of income, expenses, and net savings.
- **⏰ Automated Budget Notifications** – Celery tasks check budget limits daily and trigger alerts.
- **🔎 Advanced API Tools** – Built-in filtering, searching, and pagination for list views.
- **📚 Auto-Generated API Docs** – Interactive Swagger/OpenAPI documentation out of the box.

---

## 🛠️ Tech Stack

| Layer | Technologies |
|---|---|
| **Backend** | Django · Django REST Framework |
| **Database** | PostgreSQL |
| **Async Tasks** | Celery · Redis |
| **Authentication** | JWT (JSON Web Token) |
| **Testing** | Pytest · Pytest-Django |
| **Containerization** | Docker · Docker Compose |
| **CI/CD** | GitHub Actions |

---

## 📖 API Documentation

Interactive documentation is available via Swagger UI after running the project:
**👉 [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)**

---

## ⚙️ Local Setup & Installation (with Docker)

This project is fully containerized. Follow these steps to get it running quickly:

#### 1️⃣ Prerequisites
Install [Docker](https://www.docker.com/products/docker-desktop/) and make sure it’s running.

#### 2️⃣ Clone the Repository
```bash
git clone [https://github.com/](https://github.com/)<your-username>/<your-repository-name>.git
cd <your-repository-name>
```
*(Replace `<your-username>/<your-repository-name>` with your actual repo path.)*

#### 3️⃣ Environment Variables
Create a `.env` file in the project root:

```env
# Django
SECRET_KEY=your-super-secret-key
DEBUG=True

# Database
POSTGRES_DB=finance_db
POSTGRES_USER=finance_user
POSTGRES_PASSWORD=your_strong_password
DATABASE_URL=psql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}

# Celery / Redis
REDIS_URL=redis://redis:6379/0
```

#### 4️⃣ Build & Start Containers
Run:
```bash
docker compose up --build
```
The API will be available at: **👉 `http://127.0.0.1:8000/`**

#### 5️⃣ Initial Database Setup
In a new terminal:
```bash
# Apply migrations
docker compose exec web python manage.py migrate

# Create admin user
docker compose exec web python manage.py createsuperuser
```

---

## ✅ Running Tests
To run automated tests:

**Option 1 – Local (virtualenv):**
```bash
pytest
```

**Option 2 – Inside Docker:**
```bash
docker compose exec web pytest
```
---
> ✨ Enjoy managing your finances with Finance Management API ✨
