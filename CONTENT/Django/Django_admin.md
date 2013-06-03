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
