from django.shortcuts import render_to_response, render
from django.template import RequestContext

def index(request):
    return render_to_response('pages/index.html')

def projects(request):
	return render(request, 'pages/projects.html',{})
