# coding: utf8
from __future__ import unicode_literals

from django.db import models
from django.db.models import Max
from django.forms.models import model_to_dict


def get_code(entity, length=4):
        model = type(entity)
        code = ''
        sets = model.objects.filter(code__isnull=False)
        if sets:
            maxi = str(sets.aggregate(Max('code'))['code__max'])
            if maxi:
                consecutive = list(range(1, int(maxi)))
                busy = list(sets.values_list('code', flat=True))
                n = 0
                for l in busy:
                    busy[n] = int(str(l))
                    n += 1
                available = list(set(consecutive) - set(busy))
                if len(available) > 0:
                    code = min(available)
                else:
                    code = max(busy) + 1
        else:
            code = 1
        return str(code).zfill(length)


class base(models.Model):

    def __iter__(self):
        for field_name in self._meta.fields():
            try:
                value = getattr(self, field_name)
            except:
                value = None
            yield (field_name, value)

    def __getitem__(self, fieldname):
        try:
            return getattr(self, fieldname)
        except:
            return None

    def __setitem__(self, fieldname, value):
        try:
            return setattr(self, fieldname, value)
        except:
            return None

    def to_json(self):
        o = model_to_dict(self)
        o['app_label'] = self._meta.app_label
        o['model'] = self._meta.object_name.lower()
        return o

    class Meta:
        abstract = True


class BaseEntity(base):
    code = models.CharField(max_length=25, null=True, blank=True,
        verbose_name="code")
    name = models.CharField(max_length=100, verbose_name="name")
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.code is None or self.code == '':
            self.code = get_code(self)
        super().save()

    def __str__(self):
        if self.code and self.name:
            return "%s %s" % (str(self.code), str(self.name))
        elif self.name:
            return self.name
        elif self.code:
            return str(self.code)
        else:
            return ''

    class Meta:
        abstract = True
        ordering = ['name']


class Entity(BaseEntity):

    @staticmethod
    def autocomplete_search_fields():
        return ("code__iexact", "name__icontains",)

    class Meta:
        abstract = True
        ordering = ['name']


class Document(base):
    firts_status = "Draft"
    date = models.DateField(null=True, blank=True)
    number = models.PositiveIntegerField(null=True, blank=True)
    blog = models.TextField(max_length=5000, verbose_name="Correos e Información Relacionada", null=True, blank=True)
    printed = models.BooleanField(default=False)

    def printed_number(self, zeros=4):
        return str(self.number).zfill(zeros)

    def doc_name(self):
        if not self.number and not self.date:
            return self.firts_status
        else:
            return "%s # %s" % (self._meta.verbose_name, self.printed_number())

    doc_name.short_description = "Document"

    def __unicode__(self):
        return self.doc_name()

    class Meta:
        abstract = True
