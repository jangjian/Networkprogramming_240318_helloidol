from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello World!")

def say_hello_html(request):
    return render(request, 'playground/hello.html',{'name' : '지우야', 'greeting' : '안녀엉~'})

def say_bye_html(request):
    context = {
        'singer' : '포맨',
        'title' : '눈 떠보니 이별이더라',
    }
    return render(request, 'playground/bye.html', context=context)