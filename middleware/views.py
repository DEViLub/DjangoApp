import json
from django.http import HttpResponse
from django.shortcuts import render
from urllib import request, parse

from suds.client import Client
from suds.cache import NoCache
from concurrent.futures import ThreadPoolExecutor as executor
# Create your views here.
def middwarefun(req1):
    future = executor().submit(excuteRequest)
    future1 = executor().submit(excuteRequest)
    future2 = executor().submit(excuteRequest)
    future3 = executor().submit(excuteRequest)
    future4 = executor().submit(excuteRequest)

    return_value = future.result()
    return_value2 = future2.result()
    return_value3 = future3.result()
    return_value1 = future1.result()
    return_value4 = future4.result()
    list = [return_value,return_value1,return_value2,return_value3,return_value4]

 
    return HttpResponse(list)

def middlewarewithoutthreads(req2):
    list=[excuteRequest(),
    excuteRequest(),
    excuteRequest(),
    excuteRequest(),
    excuteRequest()] 
    return HttpResponse(list)


def excuteRequest():
    my_client = Client('http://127.0.0.1:8000/soap_server?wsdl')

    a = my_client.service.sum(3, 2)

    data = {
        "data": a
    }
    data = json.dumps(data)
    data = data.encode()
    req =  request.Request("http://127.0.0.1:8000/rest_server", data=data,method="POST") # this will make the method 
    x = request.urlopen(req)
    return json.loads(x.read())