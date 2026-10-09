Expense Tracker API

A REST API built using FastAPI to manage personal expenses with JWT authentication.

Features

- User registration and login
- Password hashing
- JWT-based authentication
- Create, read, update, and delete expenses
- Users can access only their own expenses
- SQLite database with SQLAlchemy
- Interactive API documentation using Swagger UI

Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication

Installation

1. Clone or download this project.

2. Install the dependencies:
   
   pip install -r requirements.txt

3. Configure the environment variables in ".env".

4. Start the application:
   
   uvicorn app.main:app --reload

5. Open the API documentation:
   
   http://127.0.0.1:8000/docs

Authentication

Register a user using "POST /auth/register", then log in using "POST /auth/login" to obtain an access token.

Authorize the token in Swagger UI to access the protected expense endpoints.

Expense Endpoints

- "POST /expenses/" — Create an expense
- "GET /expenses/" — List your expenses
- "GET /expenses/{expense_id}" — Get an expense
- "PUT /expenses/{expense_id}" — Update an expense
- "DELETE /expenses/{expense_id}" — Delete an expense

Database

The application uses SQLite. The database file is created automatically when the application starts.

Security

Passwords are hashed before storage. JWT tokens protect the expense endpoints, and each user can access only their own expenses.