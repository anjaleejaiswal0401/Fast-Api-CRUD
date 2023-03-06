# FastAPI CRUD with Tortoise ORM and PostgreSQL
This is a FastAPI project that provides basic CRUD functionality for managing users. It uses Tortoise ORM to interact with a PostgreSQL database and is built with Python 3.9.

# Features
Supports creating, reading, updating, and deleting user records
Validates user input to ensure it meets requirements
Uses JSON Web Tokens (JWT) for authentication
Includes API documentation using Swagger

# methods
GET /users - retrieves a list of all users

GET /users/{id} - retrieves a specific user by ID

POST /users - creates a new user

PUT /users/{id} - updates an existing user by ID

DELETE /users/{id} - deletes an existing user by ID
