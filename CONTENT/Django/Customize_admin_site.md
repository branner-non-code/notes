## Customize admin site

 Create a model admin object and pass it as second argument to `admin.site.register()`; do this in `<sitename>/admin.py` by changingg:

~~~
from django.contrib import admin
from <sitename>.models import <ClassName>

admin.site.register(<ClassName>)
~~~

 to
~~~
from django.contrib import admin
from <sitename>.models import <ClassName>

class <ClassNameAdmin>(admin.ModelAdmin):
    fields = ['<field1>', '<field2>']

admin.site.register(<ClassName>, <ClassNameAdmin>)
~~~

### Fieldsets

 A fieldset is a list of tuples in `<sitename>/admin.py`:

~~~
class <ClassNameAdmin>(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['field1']}),
        ('<title_of_fieldset>', {'fields': ['field2']}),
    ]

admin.site.register(<ClassName>, <ClassNameAdmin>)
~~~

 A fieldset can be displayed initially collapsed:

~~~
class <ClassNameAdmin>(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['field1']}),
        ('<title_of_fieldset>', {'fields': ['field2'], 'classes': ['collapse']}),
    ]

admin.site.register(<ClassName>, <ClassNameAdmin>)
~~~

### Multiple choices



~~~
from django.contrib import admin
from <sitename>.models import Choice, <ClassName>

class ChoiceInline(admin.StackedInline):  # or admin.TabularInline
    model = Choice
    extra = 3

class <ClassNameAdmin>(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['field1']}),
        ('<title_of_fieldset>', {'fields': ['field2'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(<ClassName>, <ClassNameAdmin>)
~~~

[end]
