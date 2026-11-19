from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def transport(request):
    #return HttpResponse("<h1>Transport</h1>")
     return render(request, 'transport.html',{})