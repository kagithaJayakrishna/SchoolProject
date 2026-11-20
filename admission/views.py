from django.shortcuts import render
from django.http import HttpResponse
from admission.models import Admission
# Create your views here.
def Home(request):
   # return HttpResponse("<h1>Hello, World!</h1>")
    #return render(request, 'index.html',{})
    data = Admission.objects.all()
    res = render(request, 'index.html', {'data': data})
    return res

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