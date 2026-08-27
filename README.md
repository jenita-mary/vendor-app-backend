# Vendor Management System

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-5.2-darkgreen)
![DRF](https://img.shields.io/badge/DRF-REST-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![Cloudinary](https://img.shields.io/badge/Images-Cloudinary-blue)
![Gemini](https://img.shields.io/badge/AI-Gemini-purple)
![Render](https://img.shields.io/badge/Backend-Render-purple)
![Vercel](https://img.shields.io/badge/Frontend-Vercel-black)

A production-ready **full-stack Vendor Management System** built using **Django REST Framework, React, PostgreSQL, Cloudinary, and Google Gemini AI**.

The application allows authenticated vendors to securely manage their products through a REST API and React frontend. It demonstrates JWT authentication, multi-tenant authorization, object-level permissions, image uploads, search, sorting, pagination, AI-assisted product descriptions, automated testing, and cloud deployment.

---

## 📑 Table of Contents

- [🚀 Live Demo](#-live-demo)
- [✨ Features](#-features)
- [🏗 Architecture](#-architecture)
- [🛠 Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🔐 Authentication Flow](#-authentication-flow)
- [📚 API Documentation](#-api-documentation)
- [🔌 Core API Endpoints](#-core-api-endpoints)
- [🔎 API Query Parameters](#-api-query-parameters)
- [🖼 Image Upload Architecture](#-image-upload-architecture)
- [🤖 AI Integration](#-ai-integration)
- [🔒 Multi-Tenant Security](#-multi-tenant-security)
- [🧪 Testing](#-testing)
- [⚙️ Running the Backend Locally](#️-running-the-backend-locally)
- [⚛️ Running the Frontend Locally](#️-running-the-frontend-locally)
- [🔑 Environment Variables](#-environment-variables)
- [🚀 Production Deployment](#-production-deployment)
- [📸 Screenshots](#-screenshots)
- [💡 Engineering Highlights](#-engineering-highlights)
- [🗺 Roadmap](#-roadmap)
- [👨‍💻 Author](#-author)

---

## 🚀 Live Demo

### Frontend

https://vendor-app-frontend.vercel.app/

### Backend API

https://vendor-app-backend-q553.onrender.com/

### Swagger API Documentation

https://vendor-app-backend-q553.onrender.com/api/docs/

---

## ✨ Features

### Authentication

- JWT Authentication
- Access Token and Refresh Token
- Protected REST APIs
- Automatic access-token refresh
- Custom Django User Model
- Role-based users: Admin, Vendor, Customer

### Vendor Management

- Vendor profiles
- One-to-One User ↔ Vendor relationship
- Vendor ownership validation
- Multi-tenant data isolation
- Object-level authorization

### Product Management

- Create products
- View products
- Update products
- Delete products
- Product detail
- Product image upload
- Product image replacement
- Cloudinary image storage

### Search, Sorting & Pagination

- Product search
- Sort by newest, oldest, name, price, and stock
- Page-based pagination

### AI Product Descriptions

- Google Gemini AI integration
- Generate descriptions from product names
- AI loading state
- AI error handling
- Generated description inserted into the product form

### Frontend

- React and Vite
- Responsive dashboard
- Product search and sorting
- Pagination controls
- Image preview
- Loading indicators
- Error handling
- JWT authentication flow

### Security

- JWT authentication
- Object-level permissions
- Vendor ownership validation
- Multi-tenant resource isolation
- Unauthorized resource hiding
- Environment-based configuration
- Secret management through environment variables

---

## 🏗 Architecture

```text
                         User
                          │
                          ▼
                  React Frontend
                     (Vercel)
                          │
                     HTTPS / REST
                          │
                          ▼
              Django REST Framework
                     (Render)
                          │
             ┌────────────┼────────────┐
             │            │            │
             ▼            ▼            ▼
        PostgreSQL    Cloudinary    Gemini AI
         Database       Images      Descriptions
```

### Application Flow

```text
React Frontend
      │
      │ JWT + REST API
      ▼
Django REST Framework
      │
      ├── Authentication
      ├── Permissions
      ├── Validation
      ├── Product Management
      │
      ├──────────────► PostgreSQL
      ├──────────────► Cloudinary
      └──────────────► Gemini AI
```

---

## 🛠 Tech Stack

### Backend

- Python 3.13
- Django 5.2
- Django REST Framework

### Authentication

- Django REST Framework Simple JWT

### Database

- PostgreSQL

### Frontend

- React
- Vite
- JavaScript

### AI

- Google Gemini API

### Image Storage

- Cloudinary

### API Documentation

- drf-spectacular
- OpenAPI
- Swagger UI

### Deployment

- Render — Backend
- Vercel — Frontend
- PostgreSQL — Database
- Cloudinary — Image Storage

### Configuration

- python-decouple
- Environment Variables

---

## 📁 Project Structure

### Backend

```text
vendor_app/
│
├── accounts/
├── vendors/
├── products/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── ...
│
├── orders/
├── ai/
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
```

### Frontend

```text
vendor_frontend/
│
├── src/
│   ├── api/
│   │   ├── api.js
│   │   ├── productApi.js
│   │   └── aiApi.js
│   │
│   ├── components/
│   │   ├── AddProductForm.jsx
│   │   ├── Dashboard.jsx
│   │   ├── Login.jsx
│   │   ├── Navbar.jsx
│   │   └── ProductList.jsx
│   │
│   ├── hooks/
│   │   └── useProducts.js
│   │
│   ├── App.jsx
│   └── App.css
│
├── package.json
└── README.md
```

---

## 🔐 Authentication Flow

The application uses JWT authentication with access and refresh tokens.

### 1. Login

```http
POST /api/token/
```

The client provides valid credentials and receives an Access Token and Refresh Token.

### 2. Protected APIs

```http
Authorization: Bearer <access_token>
```

Example:

```http
GET /api/products/
Authorization: Bearer <access_token>
```

### 3. Refresh Token

```http
POST /api/token/refresh/
```

The refresh token is used to obtain a new access token.

---

## 📚 API Documentation

The backend provides interactive API documentation using drf-spectacular and OpenAPI.

### Swagger UI

https://vendor-app-backend-q553.onrender.com/api/docs/

### OpenAPI Schema

```text
/api/schema/
```

---

## 🔌 Core API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/token/` | Obtain JWT access and refresh tokens |
| POST | `/api/token/refresh/` | Refresh access token |
| GET | `/api/products/` | List products |
| POST | `/api/products/` | Create product |
| GET | `/api/products/{id}/` | Retrieve product |
| PATCH | `/api/products/{id}/` | Update product |
| DELETE | `/api/products/{id}/` | Delete product |
| POST | `/api/ai/generate-description/` | Generate AI product description |

---

## 🔎 API Query Parameters

The product API supports search, ordering, and pagination.

### Search

```text
/api/products/?search=mouse
```

### Ordering

```text
/api/products/?ordering=-price
```

### Pagination

```text
/api/products/?page=2
```

### Combined Query

```text
/api/products/?search=mouse&ordering=-price&page=2
```

---

## 🖼 Image Upload Architecture

Product images are stored in Cloudinary rather than relying on the Render server filesystem.

```text
React
  │
  │ multipart/form-data
  ▼
Django REST API
  │
  ▼
Cloudinary
  │
  ▼
Secure Cloudinary URL
  │
  ▼
React Image Display
```

The application supports:

- Image upload
- Image preview
- Image replacement
- Cloudinary storage
- Secure Cloudinary URLs

---

## 🤖 AI Integration

The application integrates Google Gemini AI to generate product descriptions.

### AI Workflow

```text
Vendor enters product name
          │
          ▼
React Frontend
          │
          ▼
Django AI Endpoint
          │
          ▼
Google Gemini API
          │
          ▼
Generated Description
          │
          ▼
React Product Form
```

### AI Endpoint

```http
POST /api/ai/generate-description/
```

Example request:

```json
{
    "name": "Wireless Headphones"
}
```

The frontend provides:

- AI generation button
- Loading indicator
- Generated description insertion
- Error handling

---

## 🔒 Multi-Tenant Security

Each product belongs to a specific vendor.

The backend validates vendor ownership before allowing operations on a product.

```text
Vendor A
   │
   └── Product A

Vendor B
   │
   └── Product B
```

Vendor A cannot access or modify Vendor B's products.

The application uses:

- JWT authentication
- Object-level authorization
- Vendor ownership validation
- Multi-tenant resource isolation
- Resource hiding for unauthorized resources

Unauthorized resources can return `404 Not Found` rather than exposing whether another vendor's resource exists.

---

## 🧪 Testing

### Automated Tests

```bash
python manage.py test
```

The automated tests cover areas including:

- Authentication
- JWT tokens
- Product CRUD
- Vendor permissions
- Search
- Ordering
- Pagination
- Image upload

### Production Smoke Testing

The deployed application has been manually tested for:

- Login
- Logout
- Dashboard loading
- Product listing
- Search
- Sorting
- Pagination
- Add product
- Edit product
- Delete product
- Image upload
- Image replacement
- Cloudinary storage
- AI description generation
- Loading states
- Error handling
- Protected API access

---

## ⚙️ Running the Backend Locally

### Clone Repository

```bash
git clone https://github.com/jenita-mary/vendor-app-backend.git
cd vendor-app-backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

Backend:

```text
http://127.0.0.1:8000/
```

Swagger:

```text
http://127.0.0.1:8000/api/docs/
```

---

## ⚛️ Running the Frontend Locally

### Clone Repository

```bash
git clone https://github.com/jenita-mary/vendor-app-frontend.git
cd vendor-app-frontend
```

### Install Dependencies

```bash
npm install
```

### Configure Development Environment

Create `.env.development`:

```env
VITE_API_URL=http://127.0.0.1:8000
```

### Start Development Server

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173/
```

---

## 🔑 Environment Variables

### Backend

Create a `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=your_database
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

GEMINI_API_KEY=your_gemini_api_key

CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
```

### Frontend Development

```env
VITE_API_URL=http://127.0.0.1:8000
```

### Frontend Production

```env
VITE_API_URL=https://vendor-app-backend-q553.onrender.com
```

> **Important:** Never commit API keys, passwords, or `.env` files to GitHub.

---

## 🚀 Production Deployment

### Backend — Render

The Django REST API is deployed on Render.

Production components include:

- Django REST Framework
- Gunicorn
- PostgreSQL
- Cloudinary
- Gemini API
- Environment-based configuration
- HTTPS

### Frontend — Vercel

The React frontend is deployed on Vercel.

The frontend connects to the Render backend through `VITE_API_URL`.

```text
Vercel
  │
  ▼
React Application
  │
  ▼
Render
  │
  ▼
Django REST API
  │
  ├── PostgreSQL
  ├── Cloudinary
  └── Gemini AI
```

---

## 💡 Engineering Highlights

This project demonstrates practical full-stack engineering concepts:

- REST API design
- Django REST Framework
- JWT authentication
- Access and refresh tokens
- Custom User model
- Role-based access
- Multi-tenant authorization
- Object-level permissions
- Serializer validation
- Multipart file uploads
- Cloud image storage
- Search and ordering
- Pagination
- React state management
- API abstraction
- Loading and error states
- AI API integration
- PostgreSQL
- Environment-based configuration
- Git/GitHub workflow
- Production deployment
- Production debugging

---

## 📸 Screenshots

### Swagger API Documentation

Interactive API documentation generated using **drf-spectacular** and OpenAPI.

![Swagger UI](screenshots/swagger-ui.png)

### Django Administration Dashboard

The Django admin interface provides centralized management of application data.

![Admin Dashboard](screenshots/admin-dashboard.png)

### Custom User Model

The application uses a custom Django User model with role-based access.

![Custom User Model](screenshots/custom-user-model.png)

---

## 🗺 Roadmap

### Completed

- Django REST Framework backend
- PostgreSQL database
- JWT authentication
- Vendor management
- Product CRUD
- Vendor ownership and permissions
- Search
- Sorting
- Pagination
- Swagger/OpenAPI documentation
- Automated backend testing
- React frontend
- Responsive UI
- Cloudinary image storage
- Gemini AI product descriptions
- Render backend deployment
- Vercel frontend deployment

### Future Improvements

- CI/CD pipeline
- Docker containerization
- Redis caching
- Background task processing
- Monitoring and observability
- Expanded AI capabilities
- Automated frontend testing

---

## 👨‍💻 Author

**Jenita Mary**

GitHub:

https://github.com/jenita-mary
