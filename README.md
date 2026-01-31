# Library Device Fingerprinting

Django-based library management system with device fingerprinting authentication. This system allows users to login while tracking and limiting the number of devices they can use.

## Features

- **Device Fingerprinting**: Uses FingerprintJS to uniquely identify user devices
- **Device Limit**: Each user can register up to 2 devices maximum
- **Device Management**: Tracks device name and last login time
- **REST API**: Built with Django REST Framework
- **Frontend Interface**: Simple and clean login interface

## Technology Stack

- **Backend**: Django 6.0.1, Django REST Framework
- **Database**: SQLite3 (default)
- **Frontend**: HTML, JavaScript
- **Device Fingerprinting**: FingerprintJS v4
- **Additional**: python-dotenv for environment variables

## Project Structure

```
Library-dviceFingerpirnting/
├── accounts/           # User authentication and device management
│   ├── models.py      # UserDevice model
│   ├── views.py       # Login API endpoint
│   └── urls.py        # API routes
├── core/              # Django project settings
│   ├── settings.py    # Main configuration
│   └── urls.py        # Main URL routing
├── frontend/          # Frontend files
│   ├── index.html     # Login page
│   └── app.js         # Client-side logic
└── manage.py          # Django management script
```

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Asilbek2706/Library-dviceFingerpirnting.git
cd Library-dviceFingerpirnting
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django djangorestframework django-cors-headers python-dotenv
```

4. Create a `.env` file in the project root:
```
SECRET=your-secret-key-here
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Usage

### Starting the Application

1. Start the Django server:
```bash
python manage.py runserver
```

2. Open the frontend in your browser:
   - Open `frontend/index.html` in your web browser
   - Or serve it through a local web server

### API Endpoints

#### Login with Fingerprint
- **URL**: `/api/login/`
- **Method**: `POST`
- **Content-Type**: `application/json`

**Request Body**:
```json
{
    "username": "your-username",
    "password": "your-password",
    "fingerprint": "device-fingerprint-id",
    "device_name": "Chrome"
}
```

**Responses**:

- **Success (200)**: 
  ```json
  {
      "message": "Yangi qurilma qo'shildi va tizimga kirildi!"
  }
  ```
  or
  ```json
  {
      "message": "Xush kelibsiz! (Tanish qurilma)"
  }
  ```

- **Device Limit Reached (403)**:
  ```json
  {
      "error": "Limitga yetdingiz! Faqat 2 ta qurilmaga ruxsat berilgan. Iltimos, eski qurilmalarni o'chiring."
  }
  ```

- **Invalid Credentials (401)**:
  ```json
  {
      "error": "Login yoki parol noto'g'ri"
  }
  ```

## Models

### UserDevice

Stores device information for each user.

**Fields**:
- `user`: ForeignKey to User (CASCADE)
- `device_id`: CharField(255) - Fingerprint ID
- `device_name`: CharField(255) - Device/browser name (optional)
- `last_login`: DateTimeField - Auto-updated on save

**Constraints**:
- Unique together: (`user`, `device_id`)
- Maximum 2 devices per user

## Security Features

- Device fingerprinting prevents unauthorized access
- Device limit prevents account sharing
- CORS enabled for frontend-backend communication
- Password validation using Django's built-in validators

## Development

### Admin Interface

Access the Django admin at `http://127.0.0.1:8000/admin/` to:
- View registered users
- Manage user devices
- Monitor last login times

### Database

The project uses SQLite3 by default. To use a different database, update the `DATABASES` setting in `core/settings.py`.

## Configuration

### Environment Variables

Create a `.env` file with the following:
- `SECRET`: Django secret key (required)

### CORS Settings

CORS is enabled for all origins by default (`CORS_ALLOW_ALL_ORIGINS = True`). For production, restrict this to specific domains.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available for educational purposes.

---

# Kutubxona Qurilma Identifikatsiyasi

Django asosida qurilgan kutubxona boshqaruv tizimi qurilma identifikatsiyasi bilan. Bu tizim foydalanuvchilarga kirish imkonini beradi va ularning qancha qurilmalardan foydalanishini nazorat qiladi.

## Xususiyatlar

- **Qurilma Identifikatsiyasi**: FingerprintJS yordamida har bir qurilmani noyob identifikatsiya qiladi
- **Qurilma Limiti**: Har bir foydalanuvchi maksimal 2 ta qurilmani ro'yxatdan o'tkazishi mumkin
- **Qurilma Boshqaruvi**: Qurilma nomi va oxirgi kirish vaqtini kuzatib boradi
- **REST API**: Django REST Framework yordamida qurilgan
- **Frontend Interfeys**: Sodda va tushunarli kirish sahifasi

## Texnologiyalar

- **Backend**: Django 6.0.1, Django REST Framework
- **Ma'lumotlar bazasi**: SQLite3 (standart)
- **Frontend**: HTML, JavaScript
- **Qurilma Identifikatsiyasi**: FingerprintJS v4
- **Qo'shimcha**: python-dotenv muhit o'zgaruvchilari uchun

## O'rnatish

### Talablar

- Python 3.8+
- pip

### Sozlash

1. Repositoriyani klonlash:
```bash
git clone https://github.com/Asilbek2706/Library-dviceFingerpirnting.git
cd Library-dviceFingerpirnting
```

2. Virtual muhit yaratish:
```bash
python -m venv venv
source venv/bin/activate  # Windows'da: venv\Scripts\activate
```

3. Kutubxonalarni o'rnatish:
```bash
pip install django djangorestframework django-cors-headers python-dotenv
```

4. `.env` fayl yaratish:
```
SECRET=sizning-maxfiy-kalitingiz
```

5. Migratsiyalarni ishga tushirish:
```bash
python manage.py migrate
```

6. Superuser yaratish:
```bash
python manage.py createsuperuser
```

7. Serverni ishga tushirish:
```bash
python manage.py runserver
```

## Foydalanish

1. Django serverni ishga tushiring:
```bash
python manage.py runserver
```

2. Frontend'ni brauzerda oching:
   - `frontend/index.html` faylini brauzerda oching
   - Yoki lokal veb server orqali ishga tushiring

## Litsenziya

Ushbu loyiha ochiq kodli va ta'lim maqsadlari uchun mavjud.
