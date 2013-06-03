## Django admin

### Activate admin site

 1. Uncomment `django.contrib.admin` in the `INSTALLED_APPS` dictionary in `<sitename>/settings.py`.
 1. Update the tables with `python <sitename>/manage.py syncdb`.
 1. Uncomment three lines in ``<sitename>/urls.py`:
 
~~~
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ...
    url(r'^admin/', include(admin.site.urls)),
)
~~~

### Customize admin site

 Create a model admin object and pass it as second argument to `admin.site.register()`; do this in `<sitename>/admin.py` by changingg:

~~~
from django.contrib import admin
from polls.models import Poll

admin.site.register(Poll)
~~~

 to
~~~
from django.contrib import admin
from polls.models import Poll

class PollAdmin(admin.ModelAdmin):
    fields = ['<field1>', '<field2>']

admin.site.register(Poll, PollAdmin)
~~~

### Fieldsets

 A fieldset is a list of tuples in `<sitename>/admin.py`:

~~~
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['field1']}),
        ('<title_of_fieldset>', {'fields': ['field2']}),
    ]

admin.site.register(Poll, PollAdmin)
~~~

 A fieldset can be displayed initially collapsed:

~~~
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['field1']}),
        ('<title_of_fieldset>', {'fields': ['field2'], 'classes': ['collapse']}),
    ]

admin.site.register(Poll, PollAdmin)
~~~
