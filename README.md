# 🌍 City Explorer Backend

A Django-based backend project for managing cities, places (like hotels, hospitals), user roles, and related services. This project is designed as a scalable API-ready system for location-based platforms.

---

## 🚀 Features

- Custom User Model with roles:
  - Admin
  - Business Owner
  - User
  - Viewer

- City & Country management

- Place management (e.g., hotels, hospitals)

- Multiple images for places and cities

- Services system (e.g., hotel, hospital, etc.)

- Role-based structure for future permissions

- Ready for API integration (Django REST Framework)

---

## 🏗️ Project Structure

- `accounts` → Custom user model and roles
- `city` → City and city images
- `country` → Country model
- `place` → Places, services, and images
  ...

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/JumaQasimiM/city_backend.git
cd city_backend
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Create superuser

```bash
python manage.py createsuperuser
```

---

### 6. Run server

```bash
python manage.py runserver
```

---

## 🔐 Custom User Roles

| Role     | Description                                 |
| -------- | ------------------------------------------- |
| Admin    | Full access                                 |
| Business | Can manage places (hotels, hospitals, etc.) |
| User     | Can write comments and content              |
| Viewer   | Read-only access                            |

---

## 🖼️ Media Handling

- Images are stored in:

```
/media/
```

- Make sure these settings exist in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 🧠 Key Concepts

- **One-to-Many** → Place → Images
- **Many-to-Many** → Place ↔ Services
- **Custom User Model** using `AbstractUser`

---

## 📌 Notes

- Always define `AUTH_USER_MODEL = "accounts.User"` before first migration
- Install Pillow for image handling:

```bash
pip install Pillow
```

---

## 🔮 Future Improvements

- API with Django REST Framework
- JWT Authentication
- Role-based permissions
- Comment & Review system
- Search & filtering

---

## 👨‍💻 Author

Mohammad Juma Qasimi

---

## 📄 License

This project is for educational and development purposes.
