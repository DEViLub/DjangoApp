from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt

def postmethod(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return HttpResponse(data.get("data")**2);