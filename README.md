# Full-stack developer technical test

## Project structure

- Backend (Django app)
  - apps
    - departments
    - employees
    - appointments
- Frontend (Nextjs app)

# Installation

The project created with docker compose, that contains a python container for Django and
a PostgreSql container for database and a nodejs container for Nextjs.

Copy the .env.example file in the root directory and the backend and frontend directories too.
```bash
cp .env.example .env

cd backend
cp .env.example .env

cd ../frontend
cp .env.example .env

cd ..
```

Specify the environment variables if you want to.


Create docker containers:
```
docker compose up -d
```

## Backend

### Endpoints

- api/departments/
- api/employees/
- api/appointments/

Integration tests can be found in the tests.py files within the directories of the Django apps.