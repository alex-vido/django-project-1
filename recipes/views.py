from django.http import HttpResponse
from django.shortcuts import render


# HTTP REQUEST
def home(request):
    return render(request, 'recipes/home.html')
    # HTTP RESPONSE


def contact(request):
    return render(request, 'recipes/contact.html')


def about(request):
    return HttpResponse('About')
