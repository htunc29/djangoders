from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from datetime import date,timedelta


def home(request):
    return render(request,"index.html")
def urun(request):
    return render(request,"telefon.html")
