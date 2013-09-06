# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext


def index( request ):
   return HttpResponse("Hello World!")
