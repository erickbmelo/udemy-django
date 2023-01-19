from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', {
        'name': 'Erick Brito',
    })

def pag_temp(request):
    return render(request, 'me-apague/temp.html')