from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "core/index.html")

def becas(request):
    return render(request, "core/becas.html")

