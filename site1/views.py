from django.http import HttpResponse
from django.shortcuts import render,redirect
def index(request):
    return render(request,"crud/home.html")
    #return HttpResponse("this is homepage")