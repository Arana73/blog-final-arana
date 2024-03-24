# En el archivo views.py de la aplicación principal
from django.shortcuts import render

def about_view(request):
    # Aquí puedes incluir el contenido de la vista de "Acerca de mí"
    return render(request, 'about/about.html')

def home_view(request):
    context = {
        'welcome_message': 'Bienvenido a Rincones Remotos',
        'description': 'Este es el mejor lugar para descubrir destinos remotos y planificar tus próximas aventuras.'
    }
    return render(request, 'inicio/home.html', context)