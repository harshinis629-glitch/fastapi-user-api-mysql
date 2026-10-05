# FastAPI User API with MySQL

A RESTful User Management API built using **FastAPI**, **MySQL**, **SQLAlchemy**, and **Alembic**.

This project demonstrates how to build a backend API with persistent relational database storage, ORM-based database operations, validation, and database migrations.

---

## 🚀 Features

- Create users
- Retrieve all users
- Retrieve a user by ID
- Update user details
- Delete users
- UUID-based user IDs
- Request validation using Pydantic
- MySQL database integration
- SQLAlchemy ORM
- Alembic database migrations
- Environment variable configuration
- Interactive API documentation using Swagger UI

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend API framework |
| Uvicorn | ASGI server |
| MySQL | Relational database |
| SQLAlchemy | ORM |
| Alembic | Database migrations |
| Pydantic | Data validation |
| PyMySQL | MySQL database driver |
| python-dotenv | Environment variable management |
| HTML/CSS/JavaScript | Frontend |

---

## 📁 Project Structure

```text
user-api-db/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .gitignore
├── alembic.ini
├── database.py
├── main.py
├── models.py
├── schemas.py
└── README.md
|__test.py


📖 Learning Outcomes

Through this project, I learned how to:

Build REST APIs using FastAPI
Implement CRUD operations
Validate API requests using Pydantic
Connect FastAPI with MySQL
Use SQLAlchemy for database operations
Define database models
Manage database migrations using Alembic
Use environment variables for configuration
Test APIs using Swagger UI
Connect a frontend application with a backend API

🔮 Future Improvements
JWT authentication
Role-based access control
Redis caching
Pagination
Search and filtering
Automated testing with Pytest
Docker containerization
API deployment
👩‍💻 Author

Harshini S

B.Tech Information Technology
