from django.db import models
from grappelli_extras.models import base, base_entidad
from django.template.loader import render_to_string


# This is the way than you must to define your models
# the class base from grappelli_extras contain important functions for the models


class Foo(base_entidad):
    """
    A usual model than requiere to have a code, name and active condition.
    This the code left in blank under the creation of the object the code will be autogerenate.

    """
    date = models.DateTimeField()
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=600, null=True, blank=True)
    file = models.FileField(upload_to="documents", null=True)

    def render_as_table(self):
        return render_to_string("app/includes/foo.html", {'obj': self})


class Bar(base):
    """
    A usual related model for Foo
    """
    foo = models.ForeignKey(Foo, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)