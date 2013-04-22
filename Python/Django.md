Django basics
=============

Set-up
------
~~~
django-admin.py startproject mysite
python manage.py runserver
~~~
Specify port as
~~~
python manage.py runserver 0.0.0.0:8000
python manage.py runserver 8080
~~~
etc.
Edit `mysite/settings.py`:
~~~
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
~~~
From within directory, run 
~~~
python manage.py runserver
~~~
and set browser to `http://127.0.0.1:8000/`
