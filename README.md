# Vendor App Backend

A production-ready Vendor Management REST API built using **Django** and **Django REST Framework**.

The application allows vendors to securely manage their products with JWT authentication, object-level permissions, image uploads, search, ordering, pagination, automated testing, and interactive API documentation.

---

## Features

### Authentication

- JWT Authentication
- Refresh Token Support
- Protected APIs
- Role-based Users

### Vendor Management

- Vendor Registration
- Vendor Profile
- Secure Product Ownership

### Product Management

- Create Product
- Update Product
- Delete Product
- Product Detail
- Product List

### Product Features

- Image Upload
- Search
- Ordering
- Pagination

### Security

- Object-Level Permissions
- Multi-Tenant Resource Isolation
- Vendor Ownership Validation

### API Documentation

- Swagger UI (drf-spectacular)
- OpenAPI Schema

### Testing

- Automated API Tests
- JWT Tests
- Permission Tests
- Search Tests
- Ordering Tests
- Pagination Tests
- Image Upload Tests

---

## Tech Stack

- Python 3.x
- Django 5
- Django REST Framework
- Simple JWT
- drf-spectacular
- Pillow
- SQLite (Development)

---

## Project Structure

```
vendor_app/
│
├── accounts/
├── vendors/
├── products/
├── orders/
├── config/
├── templates/
├── media/
├── manage.py
└── requirements.txt
```

---

## API Features

- JWT Authentication
- CRUD APIs
- Search
- Ordering
- Pagination
- Image Upload
- Swagger Documentation

---

## Running the Project

### Clone Repository

```bash
git clone https://github.com/jenita-mary/vendor-app-backend.git
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Development Server

```bash
python manage.py runserver
```

---

## API Documentation

Swagger UI

```
/api/docs/
```

OpenAPI Schema

```
/api/schema/
```

---

## Testing

Run all automated tests

```bash
python manage.py test
```

---

## Future Enhancements

- PostgreSQL
- Docker
- CI/CD
- React Frontend
- AI Product Description Generator
- AI Product Categorization
- AI Product Search

---

## Author

Jenita Mary

GitHub

https://github.com/jenita-mary
