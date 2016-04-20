## Django, set up database

1. Edit `project_name/models.py` to contain

   ```python
        from django.db import models
        
        class Poll(models.Model):                                                       
            question = models.CharField(max_length=200)
            pub_date = models.DateTimeField('date published')

            def __str__(self):
                return self.question
         
        class Choice(models.Model):
            poll = models.ForeignKey(Poll)
            choice_text = models.CharField(max_length=200)
            votes = models.IntegerField(default=0)
            
            def __str__(self):
                  return self.choice_text
   ```


1. Add `project_name` to `INSTALLED_APPS` in `mysite/settings.py`.

1. Initialize database:

   ```bash
   python manage.py sql project_name
   ```

to generate SQL for tables and then 

   ```bash
   python manage.py syncdb
   ```

to create them.

[emd]