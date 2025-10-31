# Django Ders 2

## 🎯 Bugün Yapacaklarımız
1. Kullanıcılar App Oluştur  
2. Kullanıcılar Sayfası (.html) oluştur ve render et  
3. Sayfaya link verme ve yönlendirmeler (`path(name="")` olayı)  
4. Sayfaya context ile veri gönderme  
5. Sayfada context ile gönderilen veriyi görüntüleme  
6. Dinamik URL tanımlama ve sayfalarda kullanma  
7. Sayfada `{% if %}` kullanımı (olup olmama durumları)  
8. Fake user control  
9. Sayfada `{% for %}` kullanımı (Dummy ürün listesi)  
10. Django tagleri  
11. Kendi Django tagimizi oluşturma  

---

## 🧱 Kullanıcı App'i Oluşturma
> Kullanıcı uygulaması oluşturma komutu:
```bash
django-admin startapp kullanicilar
```

> Ardından `settings.py` dosyasında uygulamayı aktif et:
```python
INSTALLED_APPS = [
    ...,
    'kullanicilar',
]
```

---

## 🧩 Kullanıcılar Sayfası (.html) oluştur ve render et
**views.py**
```python
from django.shortcuts import render

def kullanicilar(request):
    return render(request, "user.html")
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path("kullanicilar/", views.kullanicilar, name="kullanicilar"),
]
```

**user.html**
```html
<h1>Kullanıcılar Sayfası</h1>
<p>Hoş geldiniz!</p>
```

---

## 🔗 Sayfaya Link Verme ve Yönlendirmeler

`home` isimli bir path tanımladığını varsayalım:

```django
<a href="{% url 'home' %}">Anasayfa</a>
```

veya `kullanicilar` sayfasına geçmek için:

```django
<a href="{% url 'kullanicilar' %}">Kullanıcılar</a>
```

**urls.py örneği**
```python
urlpatterns = [
    path('', views.home, name='home'),
    path('kullanicilar/', views.kullanicilar, name='kullanicilar'),
]
```

---

## 📦 Context ile Veri Gönderme

**views.py**
```python
def kullanicilar(request):
    context = {
        "isim": "Hüseyin",
        "yas": 22
    }
    return render(request, "user.html", context)
```

**user.html**
```django
<p>İsim: {{ isim }}</p>
<p>Yaş: {{ yas }}</p>
```

---

## 🧠 `if` Kullanımı (Şartlı Gösterim)
```django
{% if yas > 18 %}
  <p>Reşitsiniz.</p>
{% else %}
  <p>Henüz reşit değilsiniz.</p>
{% endif %}
```

---

## 🔁 `for` Kullanımı (Listeyi Döngüyle Gösterme)

**views.py**
```python
def kullanicilar(request):
    kisiler = [
        {"isim": "Ali", "yas": 20},
        {"isim": "Veli", "yas": 17},
        {"isim": "Ayşe", "yas": 25},
    ]
    return render(request, "user.html", {"kisiler": kisiler})
```

**user.html**
```django
<h2>Kişi Listesi</h2>
<ul>
{% for k in kisiler %}
  <li>{{ k.isim }} - {{ k.yas }}</li>
{% endfor %}
</ul>
```

---

## 🏷 Django Tagleri Örnekleri
```django
{{ veri|length }}                {# listenin uzunluğu #}
{{ fiyat|floatformat:2 }}        {# ondalıklı fiyat #}
{{ tarih|date:"d.m.Y" }}         {# tarih formatı #}
{{ metin|truncatechars:50 }}     {# metni kısaltır #}
```

---

## 🧩 Kendi Django Tag’imizi Oluşturma
1. Uygulama içinde `templatetags` klasörü oluştur:
```
kullanicilar/
 ├── templatetags/
 │    ├── __init__.py
 │    └── custom_tags.py
```

2. `custom_tags.py` içine yaz:
```python
from django import template
register = template.Library()

@register.simple_tag
def kdv_ekle(fiyat, oran=20):
    return fiyat + (fiyat * oran / 100)
```

3. Template içinde kullan:
```django
{% load custom_tags %}
<p>KDV dahil fiyat: {% kdv_ekle 100 18 %}</p>
```

---

✅ **Sonuç:**  
Bu derste bir Django app oluşturmayı, sayfayı render etmeyi, URL yönlendirmelerini, context göndermeyi, `if` ve `for` yapılarını, Django tag’lerini ve kendi tag’imizi nasıl yazacağımızı öğrendik.
