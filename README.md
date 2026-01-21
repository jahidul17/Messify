# Messify – Smart Mess Management System

Messify is a **web-based mess management system** designed to efficiently manage **meals, seats, members, and monthly charges** for hostels or mess facilities.  
It provides a secure, scalable backend with a modern frontend, making daily operations simple for both **admins** and **members**.

---

## 📌 Project Description

Messify solves common mess management problems such as:
- Daily meal tracking (breakfast, lunch, dinner)
- Monthly meal count calculation
- Seat-wise rent and utility charge management
- Centralized billing system
- Role-based access for Admin and Members

The system is built using **Django REST Framework** for the backend and **React** for the frontend, ensuring high performance and clean separation of concerns.

---

## 🔗 Important Links

- 📮 **Postman Public API Collection**  
  👉 https://documenter.getpostman.com/view/37745715/2sBXVkA8rC

- 📄 **Project Documentation**  
  👉 https://docs.google.com/document/d/1jLksZEh5u0UNy_7pW9wdLrPHzUvw-UfT-nDvWUUp9AQ/edit?usp=sharing

---

## ✨ Core Features

### 👤 Authentication & Authorization
- JWT-based authentication
- Role-based access (Admin / Member)

### 🍛 Meal Management
- Daily meal logging (Breakfast, Lunch, Dinner)
- Member-wise meal tracking
- Monthly meal count (month-wise summary)

### 🛏️ Seat Management
- Seat assignment per member
- Seat-wise monthly rent

### 💰 Rate & Charge Configuration (Admin)
- Meal rate (per meal)
- Seat rent (monthly)
- Electricity bill (monthly)
- Water bill (monthly)
- Utility charge (monthly)
- Effective month-based configuration

### 🧾 Billing System
- Automatic monthly bill calculation
- Meal-based cost calculation
- Charge breakdown per member

### 📊 Admin Dashboard
- View members, meals, and charges
- Update monthly rates
- Monitor overall mess expenses

---

## 🛠️ Tech Stack

### Backend
- **Python**
- **Django**
- **Django REST Framework**
- **JWT Authentication**
- **PostgreSQL / SQLite**

### Tools
- **Postman** (API Testing)
- **Git & GitHub**
- **VS Code**

---

## Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/jahidul17/Messify.git
    cd Messify
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```


4. **Create a superuser (As admin login -Optional)**
    ```bash
    python manage.py createsuperuser
    ```


5. **Apply migrations**
    ```bash
    python manage.py migrate
    ```

6. **Run the server**
    ```bash
    python manage.py runserver
    ```

7. **Access the project:**
    Open your browser and go to `http://127.0.0.1:8000/`<br>
