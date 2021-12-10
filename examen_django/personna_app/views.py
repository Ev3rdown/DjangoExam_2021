from django.http import HttpResponse
from django.shortcuts import redirect, render

from personna_app.models import Persona

# Create your views here.
def persona_list(request):
    persona_list = Persona.objects.all().order_by("-id")
    context = {
        'persona_list':persona_list
    }
    return render(request, 'persona_app/persona_list.html', context)

def persona_detail(request,id):
    persona = Persona.objects.get(id=id)
    context = {
        'persona':persona
    }
    return render(request, 'persona_app/persona_detail.html', context)

def persona_generate(request):
    return HttpResponse(f'Génération de persona')