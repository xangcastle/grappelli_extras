from django.http.response import HttpResponse
from django.forms.models import model_to_dict
from django.db.models import Q
import json
import operator
from django.core.mail import EmailMessage


def send_email(asunto="", texto="", correo=""):
    for e in correo.split(','):
        email = EmailMessage(asunto, texto,
                             to=[e],
                             )
        email.content_subtype = "html"
        email.send()


def find_entidad(sentence, filters=None):
    predicates = []
    if filters:
        predicates = filters
    for word in sentence.split(" "):
        predicates.append(('name__icontains', word))
    return [Q(x) for x in predicates]


def autocomplete_entidad(instance, request, filters=None):
    data = []
    if request.is_ajax:
        model = type(instance)
        result = []
        term = request.GET.get('term', None)
        if term:
            qs = model.objects.filter(reduce(operator.and_, find_entidad(term, filters)))
            for obj in qs:
                obj_json = {}
                obj_json['label'] = obj.name
                obj_json['value'] = obj.name
                obj_json['obj'] = obj.to_json()
                result.append(obj_json)
        data = json.dumps(result)
    return HttpResponse(data, content_type='application/json')


def entidad_to_json(instance, request):
    if request.is_ajax:
        model = type(instance)
        result = []
        id = request.POST.get('id', None)
        obj = model.objects.get(id=id)
        if obj:
            try:
                result = obj.to_json()
            except:
                result = model_to_dict(obj)
            data = json.dumps(result)
    else:
        data = 'fail'
    return HttpResponse(data, content_type='application/json')
