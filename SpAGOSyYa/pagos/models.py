from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
import uuid

# Create your models here.
class PagoSolicitado(models.Model):
    refpago = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, verbose_name="Rerencia de Pago")
    emision = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de emision")
    motivo = models.CharField(max_length=200, verbose_name="Motivo del Pago")
    cuatrimestre = models.CharField(max_length=200, verbose_name="Cuatrimestre al que corresponde el adeudo", blank=True)
    fpago = models.CharField(max_length=200, verbose_name="Forma de pago")
    descripcion = models.TextField(verbose_name="SDescripcion")
    beca = models.CharField(max_length=200, verbose_name="Beca aplicable")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    image = models.ImageField(upload_to="comprobantes", null=True, blank=True, verbose_name="Comprobante")
    cantidad = models.IntegerField(verbose_name="cantidad a pagar",default=100)
    
    class Meta:
        verbose_name = "Pagos solicitados"
        ordering = ["-emision"]

    
    def __unicode__(self):
        return self.motivo

    def __str__(self):
        return self.motivo



class PagosListado(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de emision")
    alias = models.CharField(max_length=200, verbose_name="Motivo del Pago o alias")
    cantidad = models.CharField(max_length=200, verbose_name="Monto que se paga")
    content = models.TextField(verbose_name="Descripcion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Pagos que puede realizar un usuario"
        ordering = ["-created"]

    def __str__(self):
        return self.alias


class State(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    class Meta:
        verbose_name = "estado"
        verbose_name_plural = "ESTATUS"
     

    def __str__(self):
        return self.name