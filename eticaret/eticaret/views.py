from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request,"home.html")

def category(request,kategori_adi):
    return render(request,"kategori.html",{
        "kategori":kategori_adi
    })
