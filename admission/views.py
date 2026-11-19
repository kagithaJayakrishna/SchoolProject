from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
   # return HttpResponse("<h1>Hello, World!</h1>")
    return render(request, 'index.html',{})

def products(request):
    #return HttpResponse("<h1>Products</h1>")
    return render(request, 'products.html', {})
def services(request):
    #return HttpResponse("<h1>Services</h1>")
    return render(request, 'services.html', {})
def login(request):
    return render(request, 'login.html',{})
def transport(request):
    #return HttpResponse("<h1>Transport</h1>")
    return render(request, 'transport.html', {})