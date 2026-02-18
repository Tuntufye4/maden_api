from pathlib import Path
from datetime import timedelta

# ---------------- BASE ----------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-0l(095vq#zin1_s$_ser9l5k7()s)_ye_*^5ez$ly77x=3z-pz'
DEBUG = True
ALLOWED_HOSTS = ['maden-api.onrender.com','127.0.0.1']                                                            
        
# ---------------- CORS ----------------   
INSTALLED_APPS = [                      
    'django.contrib.admin',  
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',   
    'rest_framework',
    'corsheaders',   # ⚠️ make sure corsheaders is installed   
    'document',
    'favourite',  
    'message',
    'property',  
    'reservation',
    'users',
    'viewingRequest',
]
  #        
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # ⚠️ must be before CommonMiddleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Allow your React app to call API
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]
CORS_ALLOW_ALL_ORIGINS = True  # dev only
CORS_ALLOW_CREDENTIALS = True

# ---------------- AUTH ----------------
AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),   # short-lived access token
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),      # refresh token valid 7 days
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}

# ---------------- URLS & TEMPLATES ----------------
ROOT_URLCONF = 'maden.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'maden.wsgi.application'

# ---------------- DATABASE ----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ---------------- PASSWORD VALIDATION ----------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------- INTERNATIONALIZATION ----------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ---------------- STATIC FILES ----------------
STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    
# ---------------- MEDIA FILES ----------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
    