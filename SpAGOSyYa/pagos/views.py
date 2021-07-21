from django.shortcuts import render, redirect
from .models import PagosListado, PagoSolicitado
from .forms import RegForm, PayForm
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from django.http import HttpResponse
# Create your views here.

def home(request):
    pagos = PagoSolicitado.objects.all()
    return render(request, "pagos/home.html", {'pagos' : pagos})

def payments(request):
    form = PayForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        var1 = form_data.get("cuatrimestre")
        var2 = form_data.get("motivo")
        var3 = form_data.get("descripcion")
        var4 = form_data.get("beca")
        obj = PagoSolicitado.objects.create(cuatrimestre=var1, motivo=var2, descripcion=var3, beca=var4)
    context = {
        "la_form": form,
        "pagos" : PagosListado.objects.all(),

    }
    return render(request, "pagos/payments.html", context)


def edit(request, refpago):
    elemento = PagoSolicitado.objects.filter(refpago=refpago).first()
    form = RegForm(instance=elemento)
    return render(request,"pagos/registration.html",{"form":form, 'elemento':elemento})

def actualizar(request, refpago):
    elemento = PagoSolicitado.objects.get(pk=refpago)
    form = RegForm(request.POST, files=request.FILES, instance=elemento)
    if form.is_valid():
        form.save()
    pagos = PagoSolicitado.objects.all()
    return render(request, "pagos/home.html",{'pagos' : pagos})




def report(request):
    response = HttpResponse(content_type='application/pdf')
    response ['Content-Disposition'] = 'attachment; filename=OrdenPAGO.pdf'

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    #Header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30,750,'Orden de pago')
    c.setFont('Helvetica', 12)
    c.drawString(30,735,'Adan Palacios')


    c.setFont('Helvetica-Bold', 12)
    c.drawString(480,750,'09/04/2021')

    c.line(460,747,560,747)




    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def registration(request):
    pagos = PagosListado.objects.all()
    return render(request, "pagos/registration.html", {'pagos' : pagos})