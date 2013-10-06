# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,render,get_object_or_404,get_list_or_404
from django.template.loader import render_to_string
from django.template import RequestContext
from models import Page

def index(request):
    foo = "This is a test"
    
    return render(request,'index.html',{"test":foo},context_instance=RequestContext(request))


def list_pages(request):
    pages = Page.objects.all()
    
    return render(request,"pages.html",{"pages":pages},context_instance=RequestContext(request))

def page_detail(request,Page):
    page = Page.object.get(name=Page)
    
    return render(request,"page_detail.html",{"page":page},context_instance=RequestContext(request))

def search_page(request):
    return render(request,"search.html",context_instance=RequestContext(request))