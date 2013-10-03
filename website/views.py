# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from models import Page

def index( request ):
    foo = "This is a test"
    return HttpResponse("index.html",{"foo":foo}, context_instance=RequestContext(request))

