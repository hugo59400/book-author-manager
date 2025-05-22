from pathlib import Path

# Chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète pour Django (OK en local pour un test)
SECRET_KEY = 'django-insecure-change-me'

# Mode de développement
DEBUG = True

# Autoriser toutes les connexions en local
ALLOWED_HOSTS = []

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books',  # Ton app personnalisée
]

# Middleware requis par Django (admin, sessions, sécurité…)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Fichier principal d’URL du projet
ROOT_URLCONF = 'bookstore.urls'

# Configuration des templates (HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Tu peux y mettre un dossier 'templates' si besoin
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

# Application WSGI
WSGI_APPLICATION = 'bookstore.wsgi.application'

# Base de données par défaut (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validators désactivés pour simplifier les mots de passe en dev
AUTH_PASSWORD_VALIDATORS = []

# Localisation
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Fichiers statiques (CSS, JS)
STATIC_URL = '/static/'

# Fichiers médias (ex : couverture de livres)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Clé primaire auto par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
