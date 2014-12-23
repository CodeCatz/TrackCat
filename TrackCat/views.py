from django.template import RequestContext #za prikaz templatov
from django.shortcuts import render_to_response #za prikaz templatov

def index(request):
    return render_to_response("index.html")

def about(request):
    return render_to_response('about.html')

