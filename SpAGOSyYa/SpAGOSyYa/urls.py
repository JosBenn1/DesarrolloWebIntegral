"""SpAGOSyYa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from pagos import views as pagos_views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', pagos_views.home, name="home"),
    path('admin/', admin.site.urls),
    path('payments/', pagos_views.payments, name="payments"),
    path('becas/', views.becas, name="becas"),
    path('report/', pagos_views.report, name="report"),
    path('edit/<str:refpago>', pagos_views.edit, name="edit"),
    path('actualizar/<str:refpago>', pagos_views.actualizar, name="actualizar"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)