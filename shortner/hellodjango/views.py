from django.shortcuts import render
from django.http import HttpResponse
import redis

def hello(request):
    r = redis.Redis(host='localhost', port=6379, db=0)
    name = r.get('name').decode()
    return HttpResponse(f"hello {name}!\n")
