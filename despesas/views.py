#mysite/despesas/viewes.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, Israel!")
         
# Create your views here.
