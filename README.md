# grappelli_extras

[![Latest PyPI version](https://pypip.in/v/django-grappelli-extras/badge.png)](https://crate.io/packages/django-grappelli-extras/)

[![Number of PyPI downloads](https://pypip.in/d/django-grappelli-extras/badge.png)](https://crate.io/packages/django-grappelli-extras/)


Available features:
* [Header navbar](#navbar)

Add a dynamic navbar that change according to user permissions

Add Traslation and addlink.

An Ajax api to omr using generics views.

Integration of adminactions and import_export modules.

Jquery Plugin to creade modals with objects forms.

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

 * Be sure 'django.core.context_processors.request' on your TEMPLATE_CONTEXT_PROCESSORS setting:


## To run tests

```
pip install -r requirements/tests.txt Django
export DJANGO_SETTINGS_MODULE=grappelli_dynamic_navbar.test_settings
`which django-admin.py` test grappelli_extras"
```

## Contributing

1. Fork it.
2. Create your feature branch. (`git checkout -b my-new-feature`)
3. Commit your changes. (`git commit -am 'Add some feature'`)
4. Push to the branch. (`git push origin my-new-feature`)
5. Create new Pull Request.