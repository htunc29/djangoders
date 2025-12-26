from django.shortcuts import render,redirect,get_object_or_404
from .models import Category
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from django.utils.text import slugify
from django.contrib.auth.decorators import permission_required,login_required
import google.generativeai as genai



@login_required
# @permission_required("category.add_category","/accounts/login",False)
def category_home(request):
    if not request.user.has_perm("category.add_category"):
        messages.error(request,"Sen kendini akıllı mı zannettin 😂")
        return redirect('login')

    if request.method=="POST":
        category_name=request.POST.get('category_name')
        file=request.FILES.get('file')
        if category_name=="":
            messages.warning(request,"Lütfen kategori adını yazınız")
            return redirect('category')

        if file is None:
            messages.warning(request,"Lütfen dosya seç")
            return redirect('category')

        Category.objects.create(
            category_name=category_name,
            category_slug=slugify(category_name),
            category_image=file
        )
        return redirect('category')
    category_list=Category.objects.all()
    return render(request,"category_home.html",{
        "category_list":category_list
    })

def category_delete(request,id):
    category=get_object_or_404(Category,id=id)

    if category.products.exists():
        messages.warning(request,"Lütfen bağlı ürünleri sil")
        return redirect('category')
    category.delete()
    return redirect('category')


def category_update(request,id):
    category=get_object_or_404(Category,id=id)
    if request.method=="POST":
        gelen_category_name=request.POST.get('category_name')
        gelen_file=request.FILES.get('file')

        if gelen_category_name:
            category.category_name=gelen_category_name
        if gelen_file:
            category.category_image=gelen_file
        category.save()
        return redirect('category')
    return render(request,"update_category.html",{
        "category":category
    })

def category_details(request,id):
    category=Category.objects.filter(id=id).first()
    #category=get_object_or_404(Category,id=id)
    return render(request,"category_detail.html",{
        "category":category
    })

def ask_gemini(request):
    genai.configure(api_key="buraya_api_key_gelecek")
    models=genai.GenerativeModel("gemini-2.5-flash")
    category_list=Category.objects.all()
    response=models.generate_content(f"Gemini benim kategorilerim:{category_list} bunları incele ve olmayan kategorileri aralarına virgül koyarak bana sadece istediğimi ver gereksiz fazlalık oluşturma")
    answer=response.text
    return JsonResponse({"answer":answer})
