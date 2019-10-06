# mysite/core/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, Israe!")

# Create your views here.
