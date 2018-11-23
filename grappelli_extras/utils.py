import json
from django.db.models import Q
import operator
import datetime
import decimal
from functools import reduce
from django.db.models.fields.files import ImageFieldFile, FileField, FieldFile
from django.contrib.contenttypes.models import ContentType


def smart_text(tuples, key):
    for t in tuples:
        if t[0] == key:
            return t[1]
    else:
        return None


class Codec(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(obj, datetime.time):
            return obj.strftime('H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, FieldFile):
            try:
                return obj.url
            except:
                return 'null'
        elif isinstance(obj, FileField):
            try:
                return obj.url
            except:
                return 'null'
        elif isinstance(obj, ImageFieldFile):
            try:
                return obj.url
            except:
                return 'null'
        elif obj == None:
            return 'null'
        else:
            return json.JSONEncoder.default(self, obj)


class Filter(object):
    app_label = None
    model_name = None
    model = None

    def __init__(self, app_label, model_name):
        self.app_label = app_label
        self.model_name = model_name
        self.model = ContentType.objects.get(app_label=app_label, model=model_name).model_class()

    def get_instance(self, pk):
        return self.model.objects.get(pk=pk)

    @staticmethod
    def _like(sentence, field_name, separator=" ", filters=[]):
        for word in sentence.split(separator):
            filters.append(('{}__icontains'.format(field_name.replace('__like', '')), word))
        return filters

    def format(self, filters):
        final_filter = []
        for f in filters:
            if f[0].find('__like') > -1:
                final_filter = self._like(f[1], f[0], filters=final_filter)
            else:
                final_filter.append(f)
        return [Q(x) for x in final_filter]

    def filter_by_json(self, filters=None, op=operator.and_):
        if filters:
            final_filter = []
            for k, v in json.loads(str(filters).replace("'", "\"")).items():
                final_filter.append((str(k), str(v)))
            return self.model.objects.filter(reduce(op, self.format(final_filter)))
        else:
            return self.model.objects.all()

    def filter_by_list(self, filters=[], op=operator.and_, extra=None):
        if len(filters) > 0:
            qs = self.model.objects.filter(reduce(op, self.format(filters)))
            if extra:
                qs = qs.filter(reduce(operator.and_, self.format(extra)))
            return qs
        else:
            return self.model.objects.all()
