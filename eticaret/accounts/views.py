from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse


def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('anasayfa')
        messages.error(request,"Kullanıcı bulunamadı")
        return render(request,'login.html')
    return render(request,"login.html")

def register_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")

        if password != confirm_password:
            messages.warning(request,"Girdiğin şifreler uyuşmuyor gözlerini bir baktır kanka 😂")
            messages.warning(request,"Bir daha dene")
            return render(request,"login.html")
        if User.objects.filter(username=username).exists():
            messages.warning(request,"Kanka seçtiğin kullanıcı adı baya popüler sanırım başkası almış bile 😄")
            return render(request,"login.html")
        user=User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.save()
        return redirect("login")
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

def forgot_password_view(request):
    if request.method=="POST":
        email=request.POST.get('email')

        if not User.objects.filter(email=email).exists():
            messages.error(request,"Bu e-posta adresi kayıtlı değil")
            return render(request,"forgot_password.html")

        messages.success(request,f"Şifre sıfırlama bağlantısı {email} adresine gönderildi. Lütfen e-postanızı kontrol edin.")
        return render(request,"forgot_password.html")

    return render(request,"forgot_password.html")

def reset_password_view(request):
    if request.method=="POST":
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request,"Girdiğiniz şifreler uyuşmuyor")
            return render(request,"reset_password.html")

        if len(password) < 8:
            messages.error(request,"Şifre en az 8 karakter olmalıdır")
            return render(request,"reset_password.html")

        messages.success(request,"Şifreniz başarıyla güncellendi. Yeni şifrenizle giriş yapabilirsiniz.")
        return redirect('login')

    return render(request,"reset_password.html")
