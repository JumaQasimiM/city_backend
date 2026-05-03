import os
from pathlib import Path
from datetime import timedelta
import dj_database_url
from dotenv import load_dotenv

# ================= BASE =================
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# ================= SECURITY =================
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

if not SECRET_KEY and os.getenv("ENV") == "production":
    raise ValueError("SECRET_KEY is required in production!")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "city-backend-django.onrender.com",
    ".onrender.com",
    "localhost",
    "127.0.0.1",
]

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# ================= APPS =================
AUTH_USER_MODEL = "accounts.User"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party
    'rest_framework',
    'corsheaders',
    'django_filters',

    # local
    'place',
    'city',
    'category',
    'country',
    'accounts',
    'blog',
]

# ================= MIDDLEWARE =================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',   # 🔥 must be first
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ================= URL =================
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# ================= TEMPLATES =================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ================= CORS =================
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    "https://cityexplor26.netlify.app",
    "http://localhost:5173",
]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "https://cityexplor26.netlify.app",
]

# ================= DATABASE =================
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600
    )
}

# ================= AUTH =================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ================= INTERNATIONAL =================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ================= DRF + JWT =================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

# ================= STATIC =================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ================= MEDIA =================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'