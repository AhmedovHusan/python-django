from django.http import HttpResponse
from django.shortcuts import render
from .models import Products


def index(request):
    products = Products.objects.all()
    return render(request, 'index.html')


def new(request):
    return HttpResponse("This is next new page")


def three_line(request):
    return HttpResponse("This is third page")
