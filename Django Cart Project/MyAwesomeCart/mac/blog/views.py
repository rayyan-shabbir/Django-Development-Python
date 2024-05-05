from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return HttpResponse("We are at About")


def contact(request):
    return HttpResponse("We are at Contact")


def tracker(request):
    return HttpResponse("We are at Tracker")


def search(request):
    return HttpResponse("We are at Search")


def productView(request):
    return HttpResponse("We are at ProductView")


def checkout(request):
    return HttpResponse("We are at Checkout")