# grappelli_extras

[![Latest PyPI version](https://img.shields.io/pypi/v/django-grappelli-extras.svg)](https://crate.io/packages/django-grappelli-extras/)

[![Number of PyPI downloads](https://img.shields.io/pypi/l/django-grappelli-extras.svg)](https://crate.io/packages/django-grappelli-extras/)

# Requirements
* Python = 3
* Django >= 2.1
* django-grappelli >= 2.11.1

# Installation

* ```pip install django-grappelli-extras```

## settings.py

 * Put 'grappelli_extras' **before** 'grappelli' on INSTALLED_APPS

```python
# Your setting will look like:
INSTALLED_APPS = [
    'grappelli_extras',
    'grappelli',
    'import_export',
    'adminactions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # continue with your apps
]
```

* Put 'applist' in your active context_processors.
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'grappelli_extras.context_processors.applist',
                
                # if you need to add customs menu
                'grappelli_extras.context_processors.extra_menus',
            ],
        },
    },
]
```


To configure the extra menus than you need please add the following config
your settings:

```python
EXTRA_MENUS = [
    {'menu': 'Reports', 'link': '#',

     'options': [
        {'link': '/reports/report1', 'label': 'Report # 1',
        'perm': 'app.can_report_1'},
        {'link': '/reports/report2', 'label': 'Report # 2',
        'perm': 'app.can_report_2'},
        ]

     },
]
```



## urls.py

 * Put grappelli extras urls in 'urlpatterns':

```python
# Your urls will look like:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('admin/ajax/', include('grappelli_extras.ajax_urls')),
    path('admin/extras/', include('grappelli_extras.extras_urls')),
]
```


Available features:

* [Header navbar](#navbar)
Add a dynamic navbar that change according to user permissions

* [Add Links](#add-links)
Add addlink for each model in the nabvar according to user permissions.

* [Traslation](#translation)
Traslation Suport by Locales.

* [Ajax](#ajax)
An Ajax api to make queries to django OMR using generics views.
The ajax url list are:

    * "{% url 'ajax_getCollection' %}"
    * "{% url 'ajax_getObject' %}"
    * "{% url 'ajax_autocomplete' %}"
    
But if you need to use in a javascript file out of a django template, you can use as:

    * $ajax_getColletion
    * $ajax_getObject
    * $ajax_autocomplete

This is the way than you must to define your models
the class base from grappelli_extras contain important functions for the models

```python
from django.db import models
from grappelli_extras.models import base, BaseEntity
from django.template.loader import render_to_string


class Foo(BaseEntity):
    """
    A usual model than requiere to have a code, name and active condition.
    This the code left in blank under the creation of the object the code will be autogerenate.

    """
    date = models.DateTimeField()
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=600, null=True, blank=True)

    def render_as_table(self):
        return render_to_string("app/foo.html", {'obj': self})


class Bar(base):
    """
    A usual related model for Foo
    """
    foo = models.ForeignKey(Foo, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
    

```


# Using Autocomplete generic view
```html
<script src="{% static 'ajax/grp-token.js' %}"></script>

<input type="text" id="complete-input">

<script>
    (function ($) {
        var completeEvent = function () {
            $(this).autocomplete({
                minLength: 2,
                source: "{% url 'ajax_autocomplete' %}?app_label=app&model=foo&column_name=name&column_value=code",
                select: function (i, o) {
                    // you can user obj to populate another inputs
                    console.log(o.item.obj);
                }
            });
        };
        $('#complete-input').on('keyup', completeEvent);
    })(grp.jQuery)
</script>
```

# Using GetCollection generic view
```html
<script src="{% static 'ajax/grp-token.js' %}"></script>

<script>
    (function ($) {
        $.ajax("{% url 'ajax_getCollection' %}", {
                method: "POST",
                data: {app_label: "app", model: "foo"},
                success: function (collection) {
                    console.log(collection);
                }
            })
    })(grp.jQuery)
</script>
```

# Using GetObject generic view
```html
<script src="{% static 'ajax/grp-token.js' %}"></script>

<script>
    (function ($) {
        $.ajax("{% url 'ajax_getObject' %}", {
                method: "POST",
                data: {app_label: "app", model: "foo", id: '1'},
                success: function (obj) {
                    console.log(obj);
                }
            })
    })(grp.jQuery)
</script>
```

# Using ObjectView generic view
First define the method returning a html string
```python
from grappelli_extras.models import BaseEntity
from django.template.loader import render_to_string

class Foo(BaseEntity):
    ...
    def render_as_table(self):
        return render_to_string("app/foo.html", {'obj': self})

```

In the html template render using django tags and filters as usual
```djangotemplate
<table class="grp-table">
    <thead>
    <tr>
        <th colspan="2">Foo Object</th>
    </tr>
    <tr>
        <th>Key</th>
        <th>Value</th>
    </tr>
    </thead>

    <tbody>
    <tr>
        <td>ID</td>
        <td>{{obj.id}}</td>
    </tr>
    <tr>
        <td>CODE</td>
        <td>{{obj.code}}</td>
    </tr>
    <tr>
        <td>NAME</td>
        <td>{{obj.name}}</td>
    </tr>
    </tbody>
</table>

```
After when you need to render this conten by Ajax
```html
<script src="{% static 'ajax/grp-token.js' %}"></script>

<div id="result"></div>

<script>
    (function ($) {
        $.ajax("{% url 'ajax_ObjectView' %}", {
                method: "POST",
                data: {app_label: "app", model: "foo", id: '1', view: 'render_as_table'},
                success: function (response) {
                    $('#result').html(response);
                }
            })
    })(grp.jQuery)
</script>
```

# Working with jQuery pluggins.
Let start with datatables.

In your template include the js script ajax token.js after jQuery to keep secure the request.
And include all css and js as you need.

```djangotemplate
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% load static %}

<table></table>


<script src="https://code.jquery.com/jquery-3.3.1.js"></script>
<script src="{% static 'ajax/token.js' %}"></script>
<script src="https://cdn.datatables.net/1.10.18/js/jquery.dataTables.min.js"></script>
<link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">

<script>

    $(document).ready(function () {
        $("table").DataTable({
            ajax: '{% url "ajax_getDataTables" %}?app_label=app&model=foo&filters={"activo": 1}',
            columns: [{'data': 'id'}, {'data': 'code'}, {'data': 'name'}]
        });
    });

</script>
</body>
</html>
```


Now lets try with fullcalendar
```djangotemplate
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% load static %}
<div id="calendar"></div>


<script src="https://code.jquery.com/jquery-3.3.1.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.2/moment.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.9.0/fullcalendar.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.9.0/fullcalendar.css">

<script>

    $(document).ready(function () {
        $('#calendar').fullCalendar({
            events: "{% url 'ajax_getCollection' %}?app_label=app&model=foo&filters={'activo': 1}"
        });
    });

</script>
</body>
</html>

```

Now we can try by POST with more advanced filters. But don't forget to include ajax/token.js, is
diferent form grp-token.js, grp-token must to by used inside grappelli pages.

```djangotemplate
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% load static %}
<div id="calendar"></div>
<script src="https://code.jquery.com/jquery-3.3.1.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.2/moment.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.9.0/fullcalendar.js"></script>
<script src="{% static 'ajax/token.js' %}"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.9.0/fullcalendar.css">

<script>
    $(document).ready(function () {
        $('#calendar').fullCalendar({
            events: function (start, end, timezone, callback) {
                    $.ajax("{% url 'ajax_getCollection' %}", {
                        type: "POST",
                        data: {app_label: 'app', model: 'foo',
                            filters: "{'date__gte': '" + start.format('Y-MM-DD') + "', 'date__lte': '" + end.format('Y-MM-DD') + "'}"
                        },
                        success: function (response) {
                            callback(response);
                        },
                        error: function (error) {
                            console.log(error);
                        }
                    })
                }
        });
    });
</script>
</body>
</html>
```


You can add filters like a json see doc.
Full documentation is pending, in need time. Working so hard for now...:(

* [Integration](#integration)*
Integration of adminactions, filebrowser, import_export modules.

* [Integration](#jquery)
Include a Jquery Plugin to creade modals with objects json getting data from django OMR.

## To run test project

```
cd ~/grappelli_extras/testapp
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Contributing

1. Fork it.
2. Create your feature branch. (`git checkout -b my-new-feature`)
3. Commit your changes. (`git commit -am 'Add some feature'`)
4. Push to the branch. (`git push origin my-new-feature`)
5. Create new Pull Request.

Thank You