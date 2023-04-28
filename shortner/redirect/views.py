from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.
@csrf_exempt
def echo(request):
    get = request.GET
    post = request.POST
    # return HttpResponse(get)
    # return HttpResponse(post)
    return JsonResponse(post)

def my_links(request):
    context = {}
    if request.POST.get('delete_short_link', ''):
        ShortLink.objects.filter(pk=request.POST['link_id']).delete()
        short_links = ShortLink.objects.filter(user=request.user)
        context.update({"deleted_successfully": True, "short_links": short_links})
        return render(request, "index.html", context)
    short_links = ShortLink.objects.filter(user=request.user)
    context.update({"short_links": short_links})
    return render(request, "index.html", context)
