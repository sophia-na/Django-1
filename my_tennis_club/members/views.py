from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from django.http import HttpResponse
from django.template import loader

# def members(request):
#     return HttpResponse("Hello world!")
def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())