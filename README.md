# Vendor Management System – Backend API

A production-ready **Vendor Management REST API** built with **Django 5** and **Django REST Framework**.

This project demonstrates modern backend engineering practices including **JWT authentication**, **role-based access control**, **object-level permissions**, **multi-tenant architecture**, **PostgreSQL**, **automated testing**, and **cloud deployment**. It is designed to serve as the backend for a complete Vendor Management System and will later be extended with a React frontend and AI-powered features.

---

# 🚀 Live Demo

**Live API**

https://vendor-app-backend-q553.onrender.com

**Swagger API Documentation**

https://vendor-app-backend-q553.onrender.com/api/docs/

---

# ✨ Features

## Authentication

* JWT Authentication
* Refresh Token Support
* Protected REST APIs
* Custom User Model
* Role-based Users (Admin, Vendor, Customer)

## Vendor Management

* Vendor Profile Management
* One-to-One User ↔ Vendor Relationship
* Secure Vendor Ownership
* Multi-Tenant Data Isolation

## Product Management

* Create Products
* Update Products
* Delete Products
* Product Detail
* Product Listing
* Product Image Upload

## API Features

* RESTful API Design
* Search
* Ordering
* Pagination
* Interactive Swagger Documentation
* OpenAPI Schema

## Security

* JWT Authentication
* Object-Level Permissions
* Vendor Ownership Validation
* Multi-Tenant Resource Isolation
* Resource Hiding (404 for unauthorized resources)
* Environment-Based Configuration
* Production Settings Separation

## Testing

The project includes automated tests covering:

* Authentication
* JWT Tokens
* Product CRUD Operations
* Vendor Permissions
* Search
* Ordering
* Pagination
* Image Upload

Current automated test suite:

* 12+ passing tests

---

# 🏗 Architecture

```text
                   Client
                      │
                      ▼
          Django REST Framework API
                      │
      JWT Authentication & Permissions
                      │
        Products | Vendors | Orders
                      │
                      ▼
                 PostgreSQL
                      │
                      ▼
           Render Cloud Deployment
```

---

# 🛠 Tech Stack

### Backend

* Python 3
* Django 5
* Django REST Framework

### Authentication

* Simple JWT

### Database

* PostgreSQL

### API Documentation

* drf-spectacular (Swagger/OpenAPI)

### Image Processing

* Pillow

### Deployment

* Render
* Gunicorn
* WhiteNoise
* HTTPS

### Configuration

* python-decouple
* Environment Variables

---

# 📁 Project Structure

```text
vendor_app/
│
├── accounts/
├── vendors/
├── products/
├── orders/
├── config/
│   └── settings/
│       ├── base.py
│       ├── development.py
│       └── production.py
│
├── templates/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🔒 Production Features

* Cloud PostgreSQL Database
* Environment Variable Configuration
* Gunicorn WSGI Server
* WhiteNoise Static File Serving
* HTTPS Deployment
* Production Settings Module
* Secure Secret Management

---

# 📚 API Documentation

Swagger UI

```text
/api/docs/
```

OpenAPI Schema

```text
/api/schema/
```

---

# 🧪 Running the Project Locally

## Clone Repository

```bash
git clone https://github.com/jenita-mary/vendor-app-backend.git
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file and configure:

* SECRET_KEY
* DEBUG
* ALLOWED_HOSTS
* DB_NAME
* DB_USER
* DB_PASSWORD
* DB_HOST
* DB_PORT

## Apply Migrations

```bash
python manage.py migrate
```

## Run Development Server

```bash
python manage.py runserver
```

---

# ✅ Running Tests

Execute the complete automated test suite:

```bash
python manage.py test
```

---

# 🚀 Roadmap

## Completed

* Django 5
* Django REST Framework
* PostgreSQL
* JWT Authentication
* Vendor Management
* Product CRUD
* Image Upload
* Search
* Ordering
* Pagination
* Swagger Documentation
* Automated Testing
* Render Deployment
* WhiteNoise
* Gunicorn
* HTTPS

## Planned

* React Frontend
* AI Product Description Generator
* AI Category Suggestion
* Natural Language Product Search
* AI Insights Dashboard
* Docker
* CI/CD Pipeline
* Performance Monitoring
* Caching

---

# 👨‍💻 Author

**Jenita Mary**

GitHub:
https://github.com/jenita-mary
