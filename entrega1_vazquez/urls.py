"""entrega1_vazquez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
import entrega1_vazquez.settings as settings
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path("libreria/", include("AppLibreria.urls")),
=======
    path("", include("AppLibreria.urls"))
>>>>>>> 7390e03371be64353b6a7acff4acaa45f2c76a86
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)