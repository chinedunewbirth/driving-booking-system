
# Driving School AI (Flask + PostgreSQL + Docker)

## Run Project

docker-compose up --build

## Run Database Migrations

docker-compose exec web flask db init
docker-compose exec web flask db migrate -m "initial"
docker-compose exec web flask db upgrade

## Test API

POST /students
{
 "name": "John Doe",
 "email": "john@example.com"
}

GET /students
