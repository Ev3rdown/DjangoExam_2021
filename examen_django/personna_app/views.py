import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests

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
    r = requests.get('https://randomuser.me/api?nat=fr')
    json_data = r.json()
    generatedPersona = Persona(first_name=json_data['results'][0]['name']['first'],
        last_name       = json_data['results'][0]['name']['last'],
        address_street  = json_data['results'][0]['location']['street']['name'],
        address_number  = json_data['results'][0]['location']['street']['number'],
        city            = json_data['results'][0]['location']['city'],
        postcode        = json_data['results'][0]['location']['postcode'],
        country         = json_data['results'][0]['location']['country'],
        email           = json_data['results'][0]['email'],
        username        = json_data['results'][0]['login']['username'],
        password        = json_data['results'][0]['login']['password'],
        age             = json_data['results'][0]['dob']['age'],
        picture         = json_data['results'][0]['picture']['large'])
    print(json.dumps(json_data, indent=4))
    generatedPersona.save()
    return redirect('url_persona_detail',id=generatedPersona.id)