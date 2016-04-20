## Django basics

### Set-up

 1. Initialize and run server

    ```bash
    django-admin.py startproject mysite
    python manage.py runserver
    ```

 1. Specify port as

    ```bash
    python manage.py runserver 0.0.0.0:8000
    python manage.py runserver 8080
    ```

    etc.

 1. Edit `mysite/settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'site01.db',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': '',
            'PASSWORD': '',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }
    ```

 1. From within directory, run

    ```bash
    python manage.py runserver
    ```

    and set browser to `http://127.0.0.1:8000/`

[end[