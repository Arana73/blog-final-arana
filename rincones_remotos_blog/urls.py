"""
URL configuration for rincones_remotos_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from accounts.views import logout_view
from rincones_remotos_blog.views import home_view  # Importa la vista home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # URL de la vista home_view
    path('blogs/', include('blogs.urls')),  # URLs de la aplicación de Publicaciones de Blog
    path('accounts/', include('accounts.urls')),  # URLs de la aplicación de Usuarios
    path('messages/', include('user_messages.urls')),  # URLs de la aplicación de Mensajes
    path('about/', views.about_view, name='about'),
    path('logout/', logout_view, name='logout'),
    # Otros patrones de URL aquí...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
