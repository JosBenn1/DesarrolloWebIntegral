from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('perfil/', views.profile, name="profile"),
    path('pago/', views.pago, name="pago"),
    path('regpagos/', views.regpagos, name="regpagos"),
    path('ordenpag/', views.ordenpag, name="ordenpag"),
    path('becas/', views.becas, name="becas"),
]