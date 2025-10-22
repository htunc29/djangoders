from django.shortcuts import render

# Create your views here.
def users(request):
    kullanicilar=[
        {
            "ad":"Steve",
            "soyad":"Jobs"
        },
        {
            "ad":"Bill",
            "soyad":"Gates"
        },
        {
            "ad":"Elon",
            "soyad":"Musk"
        }

    ]
    return render(request,"users/index.html",{"yas":16,"kullanicilar":kullanicilar})
