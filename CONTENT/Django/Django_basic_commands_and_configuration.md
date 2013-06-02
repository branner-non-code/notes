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

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': '<sitename>',
    }
}
```

### Create app

 * create and populate directory

```
python <sitename>/manage.py startapp <appname>
```
    
 * add `<appname>` to the `INSTALLED_APPS` dictionary in <sitename>/settings.py

### Display SQL statements and use them create database model tables

```
python <sitename>/manage.py sql <appname>
python <sitename>/manage.py syncdb # only creates tables that don't already exist
```
    
* commands to manage SQL:

```
python <sitename>/manage.py validate <appname> # checks for errors in SQL statements
python <sitename>/manage.py sqlall <appname> # displays all relevant SQL statements
```

### Format for data models

 * Each model is a class in `<appname>/modelspy`
 * Import `django.db` and use the following template:

```
class Name(django.db.models.Model):
    field_instance = django.db.models.<FieldName>(args)
```
 * Fields:
  * `CharField`: requires `max_length` argument
  * `DateTimeField`
  * `IntegerField`: optional `default` argument
 * first positional argument is optionally a human-readable name
