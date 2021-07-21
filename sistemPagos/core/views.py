from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "core/index.html")

def profile(request):
    return render(request, "core/profile.html")

def pago(request):
    return render(request, "core/pago.html")

def regpagos(request):
    return render(request, "core/regpagos.html")

def ordenpag(request):
    return render(request, "core/ordenpag.html")

def becas(request):
    return render(request, "core/becas.html")