from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def home(request):
    return render(request,  "core/home.html")
def becas(request):
    return render(request,"core/becas.html")
def pagos(request):
    return render(request,"core/pagos.html")
def profesores(request):
    return render(request,"core/profesores.html")

