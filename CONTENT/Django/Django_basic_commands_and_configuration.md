## Basic commdands and configuration

### Start project

    django-admin.py startproject <sitename>

### Start server

    python <sitename>/manage.py runserver
    # port or IP can be specified after runserver
    python <sitename>/manage.py runserver 8080 
    python <sitename>/manage.py runserver 0.0.0.0:8080

### Edit settings at

    <sitename>/settings.py

* for SQLite3 use

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', 
             'NAME': '<sitename>',
        }

### Create app

 * create and populate directory

    python <sitename>/manage.py startapp <appname>
    
 * add `<appname>` to the `INSTALLED_APPS` dictionary in <sitename>/settings.py

### Display SQL statements and use them create database model tables

    python <sitename>/manage.py sql <appname>
    python <sitename>/manage.py syncdb # only creates tables that don't already exist
    
* commands to manage SQL:
  
    python <sitename>/manage.py validate <appname> # checks for errors in SQL statements
    python <sitename>/manage.py sqlall <appname> # displays all relevant SQL statements

###
