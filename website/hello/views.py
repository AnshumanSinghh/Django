from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html") # returning html file
    
def anshuman(request):
    return HttpResponse("<h1>Hello, Anshuman Singh!!<h1>")

def python(request):
    return HttpResponse("<strong style='font-size:50px;'> I'm using Python!! </strong>") # returning HttpResponse only.

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize(),
    }) # render takes three arguments: request, "template name with route", context <dictionary of variables>
