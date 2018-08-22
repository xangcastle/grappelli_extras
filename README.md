# grappelli_extras

[![Latest PyPI version](https://pypip.in/v/django-grappelli-extras/badge.png)](https://crate.io/packages/django-grappelli-extras/)

[![Number of PyPI downloads](https://pypip.in/d/django-grappelli-extras/badge.png)](https://crate.io/packages/django-grappelli-extras/)


Available features:

* [Header navbar](#navbar)
Add a dynamic navbar that change according to user permissions

* [Add Links](#add-links)
Add addlink for each model in the nabvar according to user permissions.

* [Traslation](#translation)
Traslation Suport by Locales.

* [Ajax](#ajax)
An Ajax api make queries to django OMR using generics views.

# Using Autocomplete generic view
```javascript


<script src="{% static 'ajax/grp-token.js' %}"></script>

<input type="text" id="complete-input">

<script>
    (function ($) {
        var completeEvent = function () {
            $(this).autocomplete({
                minLength: 2,
                source: "{% url 'ajax_autocomplete' %}?app_label=app&model=foo&column_name=name&column_value=code",
                select: function (i, o) {
                    console.log(o);
                }
            });
        };
        $('#complete-input').on('keyup', completeEvent);
    })(grp.jQuery)
</script>


```

# Using GetCollection generic view
```javascript


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
```javascript


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

* [Integration](#integration)*
Integration of adminactions, filebrowser, import_export modules.

* [Integration](#jquery)
Include a Jquery Plugin to creade modals with objects json getting data from django OMR.

# Requirements

* Python > 2.6
* django-grappelli >= 2.4.5
* Django >= 1.4

# Installation

* ```pip install django-grappelli-extras```

## settings.py

 * Put 'grappelli_extras' **before** 'grappelli' on INSTALLED_APPS
 * Put 'apptemplates.Loader' on your TEMPLATE_LOADERS setting:

```python
# Your setting will look like:
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'apptemplates.Loader',
)
```

## urls.py

 * Put grappelli extras urls in 'urlpatterns':

```python
# Your urls will look like:
urlpatterns = [
    url('admin/', admin.site.urls),
    url('grappelli/', include('grappelli.urls')),
    url('admin/ajax/', include('grappelli_extras.ajax_urls')),
    url('admin/extras/', include('grappelli_extras.extras_urls')),

]
```

 * Be sure 'django.core.context_processors.request' on your TEMPLATE_CONTEXT_PROCESSORS setting:


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