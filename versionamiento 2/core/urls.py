from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('becas/', views.becas, name="becas"),
    path('pagos/', views.pagos, name="pagos"),
    path('profesores/', views.profesores, name="profesores"),
    
]