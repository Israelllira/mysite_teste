# mysite/apartamento/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, Israel Lira!")

# Create your views here.
