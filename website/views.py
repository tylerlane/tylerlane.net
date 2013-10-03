# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,render,get_object_or_404,get_list_or_404
from django.template.loader import render_to_string
from django.template import RequestContext
from models import Page

def index(request):
    foo = "This is a test"
    
    pages = Page.objects.all()
    return render(request,'index.html',{"test":foo,"pages":pages},context_instance=RequestContext(request))

