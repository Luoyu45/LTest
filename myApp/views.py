from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#def hello(request):
#    return HttpResponse('Hello,world')

def getMovieOrder(request):
    return render(request, "../templates/superIndex/index.html")

def calendar(request):
    return render(request,"../templates/superIndex/calendar.html")