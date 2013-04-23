Django, set up database
=======================


1. Edit `project_name/models.py` to contain
````
from django.db import models
 
class Poll(models.Model):                                                       
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
 
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
````

1. Add `project_name` to `mysite/settings.py`.

1. Initialize database:
        python manage.py sql project_name
        python manage.py syncdb
