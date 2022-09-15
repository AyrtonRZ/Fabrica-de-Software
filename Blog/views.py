from django.views.generic import TemplateView

from django.shortcuts import render
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = "Fab2022.html"

def chiclete(request):
    html = "<html><body><h1>Tome chiclete</h1></body></html>"
    return HttpResponse(html)

def jujuba(request):
     html = "<html><body><h1>Tome jujuba</h1></body></html>"
     return HttpResponse(html)