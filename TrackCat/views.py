#from django.http import HttpResponse
from django.template import RequestContext #za prikaz templatov
from django.shortcuts import render_to_response #za prikaz templatov

#def index(request):
    #return HttpResponse("TrackCat")

def about(request):
    return render_to_response('about.html')
