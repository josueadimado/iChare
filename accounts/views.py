from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def index(request):
    template_name = "accounts/index.html"
    args = {}
    return render(request,template_name,args)