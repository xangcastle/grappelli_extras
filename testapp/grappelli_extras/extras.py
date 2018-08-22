from django.shortcuts import render
from .utils import Filter

def to_print(request):
    app_label = request.GET.get('app_label')
    model = request.GET.get('model')
    instance = Filter(app_label=app_label, model_name=model
                      ).get_instance(int(request.GET.get('id')))
    instance.impreso = True
    instance.save()
    data = {'obj': instance}
    return render(request, "print/%s/%s.html" % (app_label, model), data)