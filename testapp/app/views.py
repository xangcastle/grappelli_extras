from django.shortcuts import render

def demo(request):
    return render(request, "app/demo.html")


def datatables(request):
    return render(request, "app/datatables.html")
