# Code-Wise

Code-Wise is an ongoing project built with Django REST Framework to manage questions through REST API endpoints.

## Project Status

🚧 **In Development**

The project is being developed incrementally while practising Django REST Framework and REST API development. Features and improvements may be added over time.

## Current Features

- Retrieve all questions.
- Create a new question.
- Retrieve an individual question by ID.
- Update an existing question.
- Delete a question.

## Technologies Used

- Python
- Django
- Django REST Framework
- Django models and serializers
- Database configured in Django

## Concepts Practised

- REST API development
- Class-based API views using `APIView`
- Serializing and validating request data
- Database operations using Django ORM
- HTTP methods: GET, POST, PUT, and DELETE

## Project Structure

The project includes Django configuration files and a `myApp` application containing the question model, serializer, and API views.

## Running the Project

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies from `requirements.txt`, if available.
4. Configure the database and required settings.
5. Run database migrations.

```bash
python manage.py migrate
python manage.py runserver
```

## Future Improvements

Planned improvements may include better error handling, input validation, API response consistency, and additional features as development continues.
