from django.shortcuts import render
from django.http import HttpResponse

def panel(request):
    
    return HttpResponse("Moderator panel")