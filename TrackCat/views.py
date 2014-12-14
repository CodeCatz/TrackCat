from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext #za prikaz templatov
from django.shortcuts import render_to_response #za prikaz templatov

def index(request):
    return HttpResponse("TrackCat")

def about(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('TrackCat/about.html', context)
