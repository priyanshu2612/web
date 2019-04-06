from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from web.helper import get_signin_url

# Create your views here.

def index(request):
  redirect_uri = request.build_absolute_uri(reverse('web:gettoken'))
  sign_in_url = get_signin_url(redirect_uri)
  context={'signin_url':sign_in_url}
  return render(request,'index.html',context)

def gettoken(request):
  return HttpResponse('<h1 style="text-align:center;font-family:Calibri;font-size: 48px ; color:#232323">Welcome to CSEA Event Management</h1>')
