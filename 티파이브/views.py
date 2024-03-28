from django.shortcuts import render

# Create your views here.

def show_jihoon(request):
    return render(request, 'T5/jihoon.html')

def show_junkyu(request):
    return render(request, 'T5/junkyu.html')