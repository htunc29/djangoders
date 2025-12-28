# Güncellemeler
> **Son Güncelleme:** README'ye ileri seviye konular eklendi (Model, Migration, Admin, Authentication, Permissions, Messages, Dosya Yükleme)

> Django giriş yap ve kayıt ol sayfaları oluşturuldu, kayıt olma ve kullanıcı girişi işlemleri tamamlandı

# 🐍 Django Kullanıcılar App Dersi

<div align="center">

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

**Django'da Template Kullanımı ve Temel Özellikler**

*Başlangıç Seviyesi | Türkçe | Uygulamalı Öğrenme*

</div>

---

---

## 📑 İçindekiler

### Temel Konular

1. [Proje Başlatma](#-sıfırdan-django-projesi-başlatma)
   - Sanal Ortam Oluşturma
   - Django Kurulumu
   - İlk Proje (startproject)

2. [App Oluşturma](#-başlangıç-yeni-app-oluşturma)
   - startapp Komutu
   - App Kaydetme

3. [Template Sistemi](#-template-html-sayfası-oluşturma)
   - Klasör Yapısı
   - HTML Sayfası Hazırlama
   - View Fonksiyonu

4. [Template Inheritance (base.html)](#-template-inheritance-kalıtım---basehtml)
   - Base Template Oluşturma
   - Extends Kullanımı
   - Block Yapısı

5. [URL Yönetimi](#-url-sayfa-adresi-tanımlama)
   - URL Pattern Tanımlama
   - name Parametresi
   - Dinamik URL (Parametreli)

6. [Context ve Veri Gönderme](#-sayfaya-veri-gönderme-context)
   - View'dan Template'e Veri
   - Template'de Veri Gösterme

7. [Template Tags](#-for-döngüsü---liste-gösterme)
   - For Döngüsü
   - If-Else Koşulları
   - Filtreler

8. [Pratik Örnekler](#-pratik-yapalım)
   - Ürün Listesi
   - Blog Sistemi

9. [Komutlar & SSS](#-komutlar-cheat-sheet)

### İleri Seviye Konular

10. [Model Oluşturma (Veritabanı)](#️-django-model-oluşturma-veritabanı)
    - Alan Türleri (CharField, TextField, vb.)
    - Alan Parametreleri
    - ForeignKey ve ManyToManyField
    - Custom Metodlar
    - save() Override Etme

11. [Migration İşlemleri](#-migration-işlemleri-veritabanı-güncelleme)
    - makemigrations
    - migrate
    - Migration Akışı

12. [Admin Paneli Özelleştirme](#-admin-paneli-özelleştirme)
    - Süper Kullanıcı Oluşturma
    - list_display, search_fields
    - Inline (TabularInline)

13. [Kullanıcı Kimlik Doğrulama](#-kullanıcı-kimlik-doğrulama-authentication)
    - Login, Logout, Register
    - authenticate() ve login()
    - User Modeli

14. [Şifre Sıfırlama](#-şifre-sıfırlama-password-reset)
    - PasswordResetView
    - E-posta Ayarları
    - Template Şablonları

15. [İzin Sistemi](#️-izin-sistemi-permissions)
    - @login_required
    - @permission_required
    - Template'de İzin Kontrolü

16. [Messages Framework](#-messages-framework-bildirim-mesajları)
    - Mesaj Türleri
    - Template'de Gösterme

17. [Dosya Yükleme](#-dosya-yükleme-file-upload)
    - ImageField, FileField
    - MEDIA Ayarları
    - enctype="multipart/form-data"

18. [Static Dosyalar](#-static-dosyalar-css-js-resimler)
    - {% load static %}
    - Klasör Yapısı

19. [Include Template Tag](#-include-template-tag)
    - with Parametresi

20. [Dil ve Zaman Dilimi](#-dil-ve-zaman-dilimi-ayarları)

21. [get_object_or_404](#️-get_object_or_404-kullanımı)

22. [QuerySet Metodları](#-queryset-metodları-veritabanı-sorguları)
    - filter(), get(), first()
    - Filtreleme Örnekleri (__contains, __gt, __lt)
    - CRUD İşlemleri
    - exists() Kullanımı

23. [redirect() Fonksiyonu](#-redirect-fonksiyonu-sayfa-yönlendirme)
    - URL Name ile Yönlendirme
    - PRG Pattern
    - redirect vs render

---

## 📚 Bu Derste Neler Öğreneceğiz?

### Temel Seviye
✅ Django projesi başlatma (startproject)
✅ Sanal ortam oluşturma ve yönetme
✅ Yeni bir Django app oluşturma
✅ HTML sayfaları (template) hazırlama
✅ Sayfalara veri gönderme
✅ Listelerle çalışma (for döngüsü)
✅ Koşullu durumlar (if-else)
✅ Sayfa linkleri oluşturma

### İleri Seviye
✅ Model oluşturma ve veritabanı tasarımı
✅ Migration işlemleri (makemigrations, migrate)
✅ Admin paneli özelleştirme
✅ Kullanıcı giriş/çıkış/kayıt (Authentication)
✅ Şifre sıfırlama sistemi
✅ İzin ve yetkilendirme sistemi (Permissions)
✅ Bildirim mesajları (Messages Framework)
✅ Dosya ve resim yükleme
✅ Static dosya yönetimi
✅ QuerySet metodları (filter, get, first, exists)
✅ redirect() ve PRG Pattern

---

## 🎬 Sıfırdan Django Projesi Başlatma

### 📦 Gereksinimler

Başlamadan önce bilgisayarınızda bunların olduğundan emin olun:

- ✅ Python 3.8 veya üzeri
- ✅ pip (Python paket yöneticisi)
- ✅ Bir kod editörü (VS Code önerilir)

### 1️⃣ Python Kontrolü

Terminal'i açın ve Python'un yüklü olup olmadığını kontrol edin:

```bash
python --version
# veya
python3 --version
```

**Çıktı şöyle olmalı:** `Python 3.11.0` (veya benzeri)

---

## 🌐 Sanal Ortam Oluşturma (Virtual Environment)

> 💡 **Sanal Ortam Nedir?** Her proje için ayrı bir Python ortamı oluşturur. Böylece projelerinizin paketleri birbirine karışmaz!

### Windows için:

```bash
# 1. Proje klasörünü oluştur
mkdir djangokurs
cd djangokurs

# 2. Sanal ortam oluştur
python -m venv sanalortam

# 3. Sanal ortamı aktifleştir
sanalortam\Scripts\activate
```

### Mac/Linux için:

```bash
# 1. Proje klasörünü oluştur
mkdir djangokurs
cd djangokurs

# 2. Sanal ortam oluştur
python3 -m venv sanalortam

# 3. Sanal ortamı aktifleştir
source sanalortam/bin/activate
```

**Başarılı olduysa** terminal başında `(sanalortam)` yazısını göreceksiniz:

```bash
(sanalortam) C:\Users\Kullanici\djangokurs>
```

---

## 📥 Django Kurulumu

Sanal ortam aktif iken Django'yu kurun:

```bash
# Django'nun en son versiyonunu kur
pip install django

# Kurulumu kontrol et
django-admin --version
```

**Çıktı:** `5.0` (veya benzer bir versiyon numarası)

> 💡 **İpucu:** Tüm paketleri görmek için `pip list` komutunu kullanabilirsiniz.

---

## 🚀 Django Projesi Oluşturma

### Projeyi Başlat

```bash
django-admin startproject eticaret
```

> 💡 **Ne yaptık?** `eticaret` adında yeni bir Django projesi oluşturduk!

### Oluşturulan Klasör Yapısı

```
djangokurs/
│
├── sanalortam/              # Sanal ortam klasörü
│
└── eticaret/                # 👈 Yeni projemiz
    ├── eticaret/            # Ana proje klasörü
    │   ├── __init__.py      # Python paketi işareti
    │   ├── settings.py      # ⚙️ Proje ayarları
    │   ├── urls.py          # 🔗 URL yönlendirmeleri
    │   ├── asgi.py          # ASGI yapılandırması
    │   └── wsgi.py          # WSGI yapılandırması
    │
    └── manage.py            # 🔧 Django yönetim komutları
```

### Proje Klasörüne Gir

```bash
cd eticaret
```

---

## ⚡ İlk Çalıştırma

### Geliştirme Sunucusunu Başlat

```bash
python manage.py runserver
```

**Başarılı olursa** şöyle bir çıktı göreceksiniz:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Tarayıcıda Test Et

Tarayıcınızı açın ve şu adrese gidin:

```
http://127.0.0.1:8000/
```

**Django roket sayfasını** görüyorsanız tebrikler! 🚀 Kurulum başarılı!

---







## 📊 Proje Başlatma Akış Şeması

```
┌─────────────────────────────────────────────────────────────┐
│                    DJANGO PROJESİ BAŞLATMA                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  Python Kurulu?  │
                    └──────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │  Sanal Ortam Oluştur │
                  │   python -m venv     │
                  └──────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │    Aktifleştir       │
                  │  activate / source   │
                  └──────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │   Django Kur         │
                  │  pip install django  │
                  └──────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │  Proje Oluştur       │
                  │  startproject        │
                  └──────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │  Sunucu Başlat       │
                  │    runserver         │
                  └──────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  🚀 HAZIR! 🎉   │
                    └──────────────────┘
```

---

## 🚀 Başlangıç: Yeni App Oluşturma

### 1️⃣ Adım: App Oluştur

Terminal'i açın ve şu komutu yazın:

```bash
python manage.py startapp kullanicilar
```

> 💡 **Ne yaptık?** Django'da her özellik için ayrı bir "app" (uygulama) oluşturuyoruz. Mesela kullanıcılar için bir app, ürünler için başka bir app.

### 2️⃣ Adım: App'i Kaydet

`settings.py` dosyasını açın ve `INSTALLED_APPS` listesine ekleyin:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... diğer uygulamalar
    'kullanicilar',  # 👈 Yeni app'imizi ekledik
]
```

> 💡 **Neden?** Django'nun bu app'i tanıması için kayıt etmemiz gerekiyor.

---

## 📁 Proje Yapısı Nasıl Olmalı?

İşte doğru klasör yapısı:

```
djangokurs/
│
├── eticaret/                    # Ana proje klasörü
│   ├── eticaret/
│   │   ├── settings.py          # Ayarlar burada
│   │   └── urls.py              # Ana URL'ler burada
│   │
│   └── kullanicilar/            # Yeni app'imiz
│       ├── templates/           # 👈 HTML sayfaları burada
│       │   └── kullanicilar/
│       │       └── liste.html
│       ├── views.py             # 👈 Sayfa fonksiyonları burada
│       └── urls.py              # 👈 Bu app'in URL'leri
│
└── sanalortam/                  # Sanal ortam (virtual environment)
```

---

## 🎨 Template (HTML Sayfası) Oluşturma

### 1️⃣ Klasör Yapısını Hazırla

1. `kullanicilar` klasörü içinde `templates` klasörü oluştur
2. `templates` içinde `kullanicilar` klasörü oluştur
3. İçine `liste.html` dosyası oluştur

### 2️⃣ HTML Sayfasını Yaz

`kullanicilar/templates/kullanicilar/liste.html`:

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kullanıcılar Listesi</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }
        h1 {
            color: #092E20;
        }
    </style>
</head>
<body>
    <h1>Kullanıcılar Sayfası</h1>
    <p>Hoş geldiniz!</p>
</body>
</html>
```

---

## 🔧 View (Sayfa Fonksiyonu) Oluşturma

`kullanicilar/views.py` dosyasını açın:

```python
from django.shortcuts import render

def kullanicilar_listesi(request):
    """
    Kullanıcılar listesi sayfasını gösterir
    """
    return render(request, 'kullanicilar/liste.html')
```

> 💡 **render() ne işe yarar?** HTML sayfasını kullanıcıya göstermek için kullanıyoruz.

---

## 🔗 URL (Sayfa Adresi) Tanımlama

### 1️⃣ App İçinde URL Tanımla

`kullanicilar/urls.py` dosyası oluşturun:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.kullanicilar_listesi, name='kullanicilar_listesi'),
]
```

### 2️⃣ Ana Projeye Bağla

`eticaret/urls.py` dosyasını açın:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kullanicilar/', include('kullanicilar.urls')),  # 👈 Ekle
]
```

> 💡 **Artık sayfamız hazır!** `http://127.0.0.1:8000/kullanicilar/` adresinden ulaşabilirsiniz.

---

## 📦 Sayfaya Veri Gönderme (Context)

### View'ı Güncelle

```python
def kullanicilar_listesi(request):
    # Gönderilecek verileri hazırla
    context = {
        'baslik': 'Kullanıcılar Listesi',
        'toplam_kullanici': 150,
        'site_adi': 'Django Kursu'
    }

    # Veriyi sayfaya gönder
    return render(request, 'kullanicilar/liste.html', context)
```

### HTML'de Veriyi Göster

```html
<h1>{{ baslik }}</h1>
<p>{{ site_adi }} - Toplam {{ toplam_kullanici }} kullanıcı</p>
```

> 💡 **{{ }}** içinde değişken adını yazarak veriyi gösteriyoruz!

---

## 🔄 For Döngüsü - Liste Gösterme

### Kullanıcı Listesi Gönder

```python
def kullanicilar_listesi(request):
    # Örnek kullanıcı listesi
    kullanicilar = [
        {'ad': 'Ahmet', 'soyad': 'Yılmaz', 'yas': 25},
        {'ad': 'Ayşe', 'soyad': 'Kaya', 'yas': 30},
        {'ad': 'Mehmet', 'soyad': 'Demir', 'yas': 28},
        {'ad': 'Zeynep', 'soyad': 'Şahin', 'yas': 22},
    ]

    context = {
        'kullanicilar': kullanicilar
    }

    return render(request, 'kullanicilar/liste.html', context)
```

### HTML'de Listeyi Göster

```html
<h2>Kullanıcılar</h2>

<table border="1">
    <tr>
        <th>Ad</th>
        <th>Soyad</th>
        <th>Yaş</th>
    </tr>

    {% for kullanici in kullanicilar %}
    <tr>
        <td>{{ kullanici.ad }}</td>
        <td>{{ kullanici.soyad }}</td>
        <td>{{ kullanici.yas }}</td>
    </tr>
    {% endfor %}
</table>
```

> 💡 **{% for %}** döngü başlatır, **{% endfor %}** döngüyü bitirir!

---

## ❓ If-Else - Koşullu Durumlar

### Örnek 1: Liste Boş mu Dolu mu?

```html
{% if kullanicilar %}
    <p>✅ Toplam {{ kullanicilar|length }} kullanıcı bulundu.</p>

    <ul>
    {% for kullanici in kullanicilar %}
        <li>{{ kullanici.ad }} {{ kullanici.soyad }}</li>
    {% endfor %}
    </ul>
{% else %}
    <p>❌ Henüz kullanıcı bulunmamaktadır.</p>
{% endif %}
```

### Örnek 2: Yaşa Göre Rozet Göster

```html
{% for kullanici in kullanicilar %}
    <div class="kullanici-kart">
        <h3>{{ kullanici.ad }} {{ kullanici.soyad }}</h3>

        {% if kullanici.yas >= 30 %}
            <span class="rozet kirmizi">🏆 Kıdemli</span>
        {% elif kullanici.yas >= 25 %}
            <span class="rozet mavi">⭐ Deneyimli</span>
        {% else %}
            <span class="rozet yesil">🌱 Genç</span>
        {% endif %}
    </div>
{% endfor %}
```

---

---

## 🎨 Template Inheritance (Kalıtım) - base.html

> 💡 **Neden Kullanırız?** Her sayfada header, footer, navbar gibi ortak bölümleri tekrar tekrar yazmamak için!

### Base Template Oluşturma

Tüm proje için ortak bir `templates` klasörü oluşturalım:

#### 1️⃣ Proje Seviyesinde Templates Klasörü

```
eticaret/
├── eticaret/
│   ├── settings.py
│   └── urls.py
├── templates/              # 👈 Yeni klasör (proje seviyesi)
│   └── base.html          # 👈 Ana template
└── kullanicilar/
    └── templates/
        └── kullanicilar/
            └── liste.html
```

#### 2️⃣ settings.py'de Ayarlama

`settings.py` dosyasını açın ve `TEMPLATES` bölümünü güncelleyin:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 👈 Bunu ekleyin
        'APP_DIRS': True,
        'OPTIONS': {
            # ...
        },
    },
]
```

#### 3️⃣ base.html Dosyası Oluşturma

`templates/base.html`:

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}E-Ticaret Sitesi{% endblock %}</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }

        /* Header / Navbar */
        .navbar {
            background: #092E20;
            color: white;
            padding: 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .navbar-brand {
            font-size: 1.5rem;
            font-weight: bold;
        }

        .navbar-menu {
            display: flex;
            gap: 2rem;
            list-style: none;
        }

        .navbar-menu a {
            color: white;
            text-decoration: none;
            transition: color 0.3s;
        }

        .navbar-menu a:hover {
            color: #4CAF50;
        }

        /* Ana İçerik */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        /* Footer */
        .footer {
            background: #092E20;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }

        /* Mesaj kutuları */
        .alert {
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 5px;
        }

        .alert-success {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }

        .alert-error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }

        /* Ek stil bloku */
        {% block extra_css %}{% endblock %}
    </style>
</head>
<body>
    <!-- NAVBAR / HEADER -->
    <nav class="navbar">
        <div class="navbar-brand">
            🛒 E-Ticaret
        </div>
        <ul class="navbar-menu">
            <li><a href="{% url 'anasayfa' %}">🏠 Ana Sayfa</a></li>
            <li><a href="{% url 'kullanicilar_listesi' %}">👥 Kullanıcılar</a></li>
            <li><a href="{% url 'urun_listesi' %}">📦 Ürünler</a></li>

            {% if user.is_authenticated %}
                <li><a href="#">👋 {{ user.username }}</a></li>
                <li><a href="{% url 'logout' %}">🚪 Çıkış</a></li>
            {% else %}
                <li><a href="{% url 'login' %}">🔑 Giriş</a></li>
            {% endif %}
        </ul>
    </nav>

    <!-- MESAJLAR (Django Messages Framework) -->
    {% if messages %}
        <div class="container">
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                </div>
            {% endfor %}
        </div>
    {% endif %}

    <!-- ANA İÇERİK ALANI -->
    <main class="container">
        {% block content %}
        <!-- Buraya alt sayfaların içeriği gelecek -->
        {% endblock %}
    </main>

    <!-- FOOTER -->
    <footer class="footer">
        <p>&copy; 2025 E-Ticaret Sitesi | Tüm Hakları Saklıdır</p>
        <p>Django ile ❤️ ile yapıldı</p>
        {% block extra_footer %}{% endblock %}
    </footer>

    <!-- Ek JavaScript bloku -->
    {% block extra_js %}{% endblock %}
</body>
</html>
```

#### 4️⃣ Alt Sayfada base.html Kullanma

`kullanicilar/templates/kullanicilar/liste.html`:

```html
{% extends 'base.html' %}

{% block title %}Kullanıcılar Listesi - E-Ticaret{% endblock %}

{% block content %}
<h1>👥 Kullanıcılar Listesi</h1>

<div class="kullanici-container">
    {% if kullanicilar %}
        <p>Toplam {{ kullanicilar|length }} kullanıcı bulundu.</p>

        <table border="1" style="width: 100%; margin-top: 20px;">
            <thead>
                <tr>
                    <th>Ad</th>
                    <th>Soyad</th>
                    <th>Yaş</th>
                    <th>Durum</th>
                    <th>İşlemler</th>
                </tr>
            </thead>
            <tbody>
                {% for kullanici in kullanicilar %}
                <tr>
                    <td>{{ kullanici.ad }}</td>
                    <td>{{ kullanici.soyad }}</td>
                    <td>{{ kullanici.yas }}</td>
                    <td>
                        {% if kullanici.yas >= 30 %}
                            <span style="color: orange;">🏆 Kıdemli</span>
                        {% else %}
                            <span style="color: green;">🌱 Genç</span>
                        {% endif %}
                    </td>
                    <td>
                        <a href="{% url 'kullanici_detay' kullanici.id %}">👁️ Detay</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <div class="alert alert-error">
            ❌ Henüz kullanıcı bulunmamaktadır.
        </div>
    {% endif %}
</div>
{% endblock %}

{% block extra_css %}
<style>
    table {
        border-collapse: collapse;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    th {
        background: #092E20;
        color: white;
        padding: 10px;
    }

    td {
        padding: 10px;
        text-align: center;
    }

    tr:nth-child(even) {
        background: #f2f2f2;
    }
</style>
{% endblock %}
```

### 📚 Template Block Türleri

| Block Adı | Kullanım Amacı | Örnek |
|-----------|----------------|-------|
| `{% block title %}` | Sayfa başlığı | `<title>` etiketi |
| `{% block content %}` | Ana içerik | Sayfanın gövdesi |
| `{% block extra_css %}` | Ek CSS | Sayfa özel stiller |
| `{% block extra_js %}` | Ek JavaScript | Sayfa özel scriptler |
| `{% block header %}` | Özel başlık | Özel navbar |
| `{% block footer %}` | Özel footer | Özel alt bilgi |

---

## 🔗 Dinamik URL Tanımlama (Parametreli URL)

> 💡 **Ne İşe Yarar?** URL'de değişken değerler kullanarak (id, slug, username) dinamik sayfalar oluşturuyoruz.

### Örnek Senaryolar

- `/kullanici/5/` → 5 numaralı kullanıcıyı göster
- `/urun/laptop-asus/` → "laptop-asus" slug'ına sahip ürünü göster
- `/kategori/elektronik/sayfa/2/` → Elektronik kategorisinin 2. sayfası

---

### 1️⃣ Integer (Sayı) Parametresi

#### URL Tanımlama

`kullanicilar/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.kullanicilar_listesi, name='kullanicilar_listesi'),
    path('<int:kullanici_id>/', views.kullanici_detay, name='kullanici_detay'),
    # <int:kullanici_id> → Sadece sayı kabul eder
]
```

#### View Fonksiyonu

`kullanicilar/views.py`:

```python
from django.shortcuts import render, get_object_or_404

def kullanici_detay(request, kullanici_id):
    """
    Tek bir kullanıcının detayını gösterir
    """
    # Örnek veri (gerçekte veritabanından gelir)
    kullanicilar = [
        {'id': 1, 'ad': 'Ahmet', 'soyad': 'Yılmaz', 'yas': 25, 'email': 'ahmet@example.com'},
        {'id': 2, 'ad': 'Ayşe', 'soyad': 'Kaya', 'yas': 30, 'email': 'ayse@example.com'},
        {'id': 3, 'ad': 'Mehmet', 'soyad': 'Demir', 'yas': 28, 'email': 'mehmet@example.com'},
    ]

    # ID'ye göre kullanıcıyı bul
    kullanici = None
    for k in kullanicilar:
        if k['id'] == kullanici_id:
            kullanici = k
            break

    context = {
        'kullanici': kullanici
    }

    return render(request, 'kullanicilar/detay.html', context)
```

#### Template

`kullanicilar/templates/kullanicilar/detay.html`:

```html
{% extends 'base.html' %}

{% block title %}{{ kullanici.ad }} {{ kullanici.soyad }} - Detay{% endblock %}

{% block content %}
<a href="{% url 'kullanicilar_listesi' %}" style="text-decoration: none;">
    ← Geri Dön
</a>

{% if kullanici %}
    <div style="background: #f9f9f9; padding: 20px; margin: 20px 0; border-radius: 8px;">
        <h1>👤 {{ kullanici.ad }} {{ kullanici.soyad }}</h1>
        <hr>
        <p><strong>ID:</strong> {{ kullanici.id }}</p>
        <p><strong>Yaş:</strong> {{ kullanici.yas }}</p>
        <p><strong>Email:</strong> {{ kullanici.email }}</p>

        {% if kullanici.yas >= 30 %}
            <span style="background: orange; color: white; padding: 5px 10px; border-radius: 5px;">
                🏆 Kıdemli Kullanıcı
            </span>
        {% endif %}
    </div>
{% else %}
    <div class="alert alert-error">
        ❌ Kullanıcı bulunamadı!
    </div>
{% endif %}
{% endblock %}
```

#### Template'de Kullanım (Link Oluşturma)

```html
<!-- Liste sayfasında -->
{% for kullanici in kullanicilar %}
    <a href="{% url 'kullanici_detay' kullanici.id %}">
        {{ kullanici.ad }} {{ kullanici.soyad }}
    </a>
{% endfor %}
```

---

### 2️⃣ String (Slug) Parametresi

#### URL Tanımlama

`urunler/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.urun_listesi, name='urun_listesi'),
    path('<slug:urun_slug>/', views.urun_detay, name='urun_detay'),
    # <slug:urun_slug> → Harf, rakam, tire (-) ve alt çizgi (_) kabul eder
]
```

#### View Fonksiyonu

```python
def urun_detay(request, urun_slug):
    """
    Ürün detay sayfası
    URL: /urunler/laptop-asus-rog/
    """
    urunler = [
        {'slug': 'laptop-asus-rog', 'ad': 'Asus ROG Laptop', 'fiyat': 25000},
        {'slug': 'iphone-15-pro', 'ad': 'iPhone 15 Pro', 'fiyat': 60000},
    ]

    urun = None
    for u in urunler:
        if u['slug'] == urun_slug:
            urun = u
            break

    context = {'urun': urun}
    return render(request, 'urunler/detay.html', context)
```

#### Template'de Kullanım

```html
<a href="{% url 'urun_detay' 'laptop-asus-rog' %}">Asus ROG Laptop</a>
<!-- Veya -->
<a href="{% url 'urun_detay' urun.slug %}">{{ urun.ad }}</a>
```

---

### 3️⃣ Birden Fazla Parametre

#### URL Tanımlama

```python
from django.urls import path
from . import views

urlpatterns = [
    path('kategori/<slug:kategori_slug>/sayfa/<int:sayfa>/',
         views.kategori_sayfalama,
         name='kategori_sayfalama'),
]
```

#### View Fonksiyonu

```python
def kategori_sayfalama(request, kategori_slug, sayfa):
    """
    URL: /kategori/elektronik/sayfa/2/
    """
    context = {
        'kategori': kategori_slug,
        'sayfa': sayfa,
        'toplam_sayfa': 10
    }
    return render(request, 'kategori.html', context)
```

#### Template'de Kullanım

```html
<!-- Önceki sayfa -->
{% if sayfa > 1 %}
    <a href="{% url 'kategori_sayfalama' kategori sayfa|add:"-1" %}">← Önceki</a>
{% endif %}

<!-- Sonraki sayfa -->
{% if sayfa < toplam_sayfa %}
    <a href="{% url 'kategori_sayfalama' kategori sayfa|add:"1" %}">Sonraki →</a>
{% endif %}
```

---

### 4️⃣ URL Path Converters (Dönüştürücüler)

| Converter | Açıklama | Örnek |
|-----------|----------|-------|
| `<int:name>` | Pozitif tam sayı | `/urun/42/` |
| `<str:name>` | Boş olmayan string (/ hariç) | `/sayfa/hakkimizda/` |
| `<slug:name>` | Slug formatı (harf, sayı, -, _) | `/blog/django-ogreniyorum/` |
| `<uuid:name>` | UUID formatı | `/siparis/550e8400-e29b...` |
| `<path:name>` | Her karakter (/ dahil) | `/dosya/klasor/alt/dosya.pdf` |

---

### 5️⃣ Pratik Örnek: Blog Sistemi

#### URL Yapısı

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Ana blog sayfası
    path('', views.blog_anasayfa, name='blog_anasayfa'),

    # Kategori filtreleme
    path('kategori/<slug:kategori_slug>/', views.kategori_yazilari, name='kategori_yazilari'),

    # Yazar sayfası
    path('yazar/<str:username>/', views.yazar_profil, name='yazar_profil'),

    # Tek yazı detayı
    path('yazi/<int:yazi_id>/<slug:yazi_slug>/', views.yazi_detay, name='yazi_detay'),

    # Arama
    path('ara/', views.arama, name='blog_arama'),
]
```

#### View Örnekleri

```python
# blog/views.py
from django.shortcuts import render

def yazi_detay(request, yazi_id, yazi_slug):
    """
    URL: /blog/yazi/42/django-template-sistemi/
    """
    context = {
        'yazi_id': yazi_id,
        'yazi_slug': yazi_slug,
    }
    return render(request, 'blog/detay.html', context)

def kategori_yazilari(request, kategori_slug):
    """
    URL: /blog/kategori/programlama/
    """
    context = {
        'kategori': kategori_slug,
    }
    return render(request, 'blog/kategori.html', context)
```

#### Template Kullanımı

```html
<!-- Blog yazı kartı -->
<div class="yazi-kart">
    <h3>
        <a href="{% url 'yazi_detay' yazi.id yazi.slug %}">
            {{ yazi.baslik }}
        </a>
    </h3>
    <p>Kategori:
        <a href="{% url 'kategori_yazilari' yazi.kategori_slug %}">
            {{ yazi.kategori }}
        </a>
    </p>
    <p>Yazar:
        <a href="{% url 'yazar_profil' yazi.yazar_username %}">
            {{ yazi.yazar }}
        </a>
    </p>
</div>
```

---

### 🎯 Dinamik URL Best Practices

#### ✅ Yapılması Gerekenler

```python
# ✅ İyi: Anlamlı parametre isimleri
path('urun/<int:urun_id>/', views.urun_detay)

# ✅ İyi: URL'de iki farklı bilgi (SEO için)
path('blog/<int:id>/<slug:slug>/', views.yazi_detay)

# ✅ İyi: Tutarlı isimlendirme
path('kullanici/<int:kullanici_id>/siparisler/', views.kullanici_siparisleri)
```

#### ❌ Yapılmaması Gerekenler

```python
# ❌ Kötü: Anlaşılmaz parametre
path('u/<int:x>/', views.detay)

# ❌ Kötü: Çok fazla parametre
path('a/<int:b>/<int:c>/<int:d>/<int:e>/', views.fonk)

# ❌ Kötü: Türkçe karakter
path('ürün/<int:id>/', views.detay)  # URL'de İngilizce kullan
```

---

## 🔗 Sayfa Linkleri (URL Tag)

### Neden `name=""` Kullanırız?

```python
# urls.py
urlpatterns = [
    path('', views.kullanicilar_listesi, name='kullanicilar_listesi'),
    path('detay/', views.kullanici_detay, name='kullanici_detay'),
]
```

### HTML'de Link Oluştur

```html
<!-- ❌ YANLIŞ: Direkt adres yazmayın -->
<a href="/kullanicilar/">Kullanıcılar</a>

<!-- ✅ DOĞRU: name kullanın -->
<a href="{% url 'kullanicilar_listesi' %}">Kullanıcılar</a>
<a href="{% url 'kullanici_detay' %}">Detay</a>
```

> 💡 **Neden?** Adres değişirse sadece `urls.py`'yi güncellemeniz yeterli!

---

## 🎯 Django Template Tagleri Özeti

### 📝 En Çok Kullanılanlar

| Tag | Açıklama | Örnek |
|-----|----------|-------|
| `{{ değişken }}` | Değişken yazdır | `{{ kullanici.ad }}` |
| `{% for %}` | Döngü | `{% for item in liste %}` |
| `{% if %}` | Koşul | `{% if yas > 18 %}` |
| `{% url %}` | Link oluştur | `{% url 'anasayfa' %}` |
| `{% load static %}` | CSS/JS yükle | `{% load static %}` |

### 🔧 Filtreler (Filters)

```html
{{ metin|upper }}                 <!-- BÜYÜK HARF -->
{{ metin|lower }}                 <!-- küçük harf -->
{{ metin|title }}                 <!-- Her Kelime Büyük -->
{{ liste|length }}                <!-- Uzunluk -->
{{ tarih|date:"d/m/Y" }}         <!-- 25/01/2024 -->
{{ metin|truncatewords:5 }}      <!-- İlk 5 kelime -->
```

### 🎨 Örnek Kullanım

```html
<h1>{{ baslik|upper }}</h1>
<p>Toplam: {{ kullanicilar|length }} kişi</p>
<p>{{ aciklama|truncatewords:10 }}</p>
```

---




## 🎓 Pratik Yapalım!

### Görev 1: Ürün Listesi

Bir `urunler` app'i oluşturun ve şu özellikleri ekleyin:

```python
# views.py
def urun_listesi(request):
    urunler = [
        {'ad': 'Laptop', 'fiyat': 15000, 'stok': 5},
        {'ad': 'Mouse', 'fiyat': 150, 'stok': 20},
        {'ad': 'Klavye', 'fiyat': 500, 'stok': 0},
    ]

    context = {'urunler': urunler}
    return render(request, 'urunler/liste.html', context)
```

```html
<!-- liste.html -->
{% for urun in urunler %}
    <div class="urun-kart">
        <h3>{{ urun.ad }}</h3>
        <p>Fiyat: {{ urun.fiyat }} ₺</p>

        {% if urun.stok > 0 %}
            <span class="yesil">✅ Stokta var ({{ urun.stok }} adet)</span>
        {% else %}
            <span class="kirmizi">❌ Stokta yok</span>
        {% endif %}
    </div>
{% endfor %}
```

---

## 📖 Komutlar Cheat Sheet

### 🎬 Proje Başlatma

```bash
# Sanal ortam oluştur
python -m venv sanalortam                    # Windows
python3 -m venv sanalortam                   # Mac/Linux

# Sanal ortamı aktifleştir
sanalortam\Scripts\activate                  # Windows
source sanalortam/bin/activate               # Mac/Linux

# Sanal ortamı deaktif et
deactivate

# Django kur
pip install django

# Django versiyonunu kontrol et
django-admin --version
```

### 🚀 Proje ve App Yönetimi

```bash
# Yeni proje oluştur
django-admin startproject proje_adi

# Yeni app oluştur
python manage.py startapp app_adi

# Sunucuyu başlat
python manage.py runserver

# Farklı portta başlat
python manage.py runserver 8080
```


### 🔧 Diğer Yararlı Komutlar

```bash
# Python shell aç
python manage.py shell

# Tüm paketleri listele
pip list

# requirements.txt oluştur
pip freeze > requirements.txt

# requirements.txt'ten kur
pip install -r requirements.txt

# Django admin komutlarını gör
python manage.py help
```

---

## ⚠️ Önemli Hatırlatmalar

### ✅ Yapılması Gerekenler

- **Template dosyaları** mutlaka `templates/app_adi/` içinde olmalı
- **URL'lerde** `name` parametresi kullan
- **Context dictionary** ile veri gönder
- **`{% csrf_token %}`** form'larda unutma
- **base.html** kullanarak kod tekrarını önle
- **Dinamik URL'lerde** anlamlı parametre isimleri kullan
- **`{% extends %}`** her zaman template'in ilk satırında olmalı
- **settings.py'de** `TEMPLATES['DIRS']` ayarını yap

### ❌ Yapılmaması Gerekenler

- Direkt HTML'de URL yazmayın (`/kullanicilar/` yerine `{% url %}` kullanın)
- Template klasörünü yanlış yere koymayın
- App'i `INSTALLED_APPS`'e eklemeyi unutmayın
- Her sayfada header/footer tekrar yazmayın (base.html kullanın)
- URL parametrelerinde Türkçe karakter kullanmayın
- `{% block %}` kapamayı unutmayın (`{% endblock %}`)
- Statik dosyalarda `{% load static %}` yazmayı unutmayın

---



### 📚 Önerilen Proje Fikirleri

1. **Blog Sistemi** - Yazı, kategori, yorum
2. **To-Do List** - Görev yönetimi
3. **E-Ticaret** - Ürün, sepet, sipariş
4. **Kütüphane Yönetimi** - Kitap ödünç alma
5. **Sosyal Medya** - Profil, gönderi, beğeni

---

## 📚 Faydalı Kaynaklar

- 📘 [Django Resmi Dökümantasyon](https://docs.djangoproject.com/)
- 🎥 [Django Template Dili](https://docs.djangoproject.com/en/stable/ref/templates/language/)
- 🔧 [Built-in Template Tags](https://docs.djangoproject.com/en/stable/ref/templates/builtins/)
- 💡 [Django Girls Tutorial (Türkçe)](https://tutorial.djangogirls.org/tr/)

---

## 🗄️ Django Model Oluşturma (Veritabanı)

> 💡 **Model Nedir?** Model, veritabanındaki tabloların Python sınıfları olarak temsil edilmesidir. Her model bir veritabanı tablosuna karşılık gelir.

### 📦 Temel Model Oluşturma

`urunler/models.py` dosyasını açın:

```python
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)           # Kısa metin
    description = models.TextField(max_length=500)     # Uzun metin
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Fiyat
    stock = models.PositiveIntegerField(default=0)     # Stok (pozitif sayı)
    is_active = models.BooleanField(default=True)      # Aktif mi?

    def __str__(self):
        return self.title  # Admin panelinde görünecek isim
```

> 💡 **`__str__` Metodu**: Admin panelinde ve Python shell'de nesneyi gösterirken kullanılır.

---

### 🔧 Alan Türleri (Field Types)

| Alan Türü | Açıklama | Örnek Kullanım |
|-----------|----------|----------------|
| `CharField` | Kısa metin (max_length zorunlu) | `title = models.CharField(max_length=200)` |
| `TextField` | Uzun metin | `description = models.TextField()` |
| `IntegerField` | Tam sayı | `quantity = models.IntegerField()` |
| `PositiveIntegerField` | Pozitif tam sayı | `stock = models.PositiveIntegerField()` |
| `DecimalField` | Ondalıklı sayı (fiyat için) | `price = models.DecimalField(max_digits=10, decimal_places=2)` |
| `FloatField` | Ondalıklı sayı | `rating = models.FloatField()` |
| `BooleanField` | True/False değeri | `is_active = models.BooleanField(default=True)` |
| `DateField` | Tarih | `birth_date = models.DateField()` |
| `DateTimeField` | Tarih ve saat | `created_at = models.DateTimeField()` |
| `EmailField` | E-posta adresi | `email = models.EmailField()` |
| `URLField` | URL adresi | `website = models.URLField()` |
| `SlugField` | URL-dostu metin | `slug = models.SlugField(unique=True)` |
| `ImageField` | Resim dosyası | `image = models.ImageField(upload_to="images/")` |
| `FileField` | Herhangi dosya | `document = models.FileField(upload_to="docs/")` |

---

### 📌 Alan Parametreleri

```python
class Product(models.Model):
    # Zorunlu alan
    title = models.CharField(max_length=200)

    # Boş bırakılabilir (veritabanında NULL)
    description = models.TextField(blank=True, null=True)

    # Varsayılan değer
    is_active = models.BooleanField(default=True)

    # Benzersiz (unique) değer
    slug = models.SlugField(unique=True)

    # Otomatik tarih ekleme (kayıt oluşturulduğunda)
    created_at = models.DateTimeField(auto_now_add=True)

    # Otomatik güncelleme tarihi (her kaydetmede)
    updated_at = models.DateTimeField(auto_now=True)
```

| Parametre | Açıklama |
|-----------|----------|
| `max_length` | Maksimum karakter sayısı (CharField için zorunlu) |
| `blank=True` | Form'da boş bırakılabilir |
| `null=True` | Veritabanında NULL olabilir |
| `default` | Varsayılan değer |
| `unique=True` | Benzersiz olmalı |
| `auto_now_add=True` | Kayıt oluşturulduğunda otomatik tarih |
| `auto_now=True` | Her güncellemede otomatik tarih |

---

### 🔗 İlişkiler (Relationships)

#### 1️⃣ ForeignKey (Bire-Çok İlişki)

Bir kategori birçok ürüne sahip olabilir:

```python
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_slug = models.SlugField(unique=True)
    category_image = models.ImageField(upload_to="kategori_resimleri")

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category_name = models.CharField(max_length=50)
    category_slug = models.SlugField(unique=True)
    # 👇 ForeignKey ile ana kategoriye bağlıyoruz
    parent_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,     # Kategori silinirse alt kategoriler de silinir
        related_name="altkategoriler" # Tersine erişim için
    )

    def __str__(self):
        return self.category_name
```

#### on_delete Seçenekleri:

| Seçenek | Açıklama |
|---------|----------|
| `CASCADE` | Ana kayıt silinirse bağlı kayıtlar da silinir |
| `PROTECT` | Ana kayıt silinmeye çalışılırsa hata verir |
| `SET_NULL` | Ana kayıt silinirse NULL yapar (null=True gerekir) |
| `SET_DEFAULT` | Ana kayıt silinirse varsayılan değer atar |

#### related_name Kullanımı:

```python
# Kategori üzerinden alt kategorilere erişim
kategori = Category.objects.get(id=1)
alt_kategoriler = kategori.altkategoriler.all()  # related_name sayesinde
```

#### 2️⃣ ManyToManyField (Çoka-Çok İlişki)

Bir ürün birden fazla etikete, bir etiket birden fazla ürüne sahip olabilir:

```python
class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)  # 👈 Çoka-çok ilişki

    def __str__(self):
        return self.title
```

#### ManyToManyField Kullanımı:

```python
# Ürüne etiket ekleme
urun = Product.objects.get(id=1)
etiket = Tag.objects.get(id=1)
urun.tags.add(etiket)

# Ürünün tüm etiketleri
urun.tags.all()

# Bir etiketin tüm ürünleri
etiket.product_set.all()
```

---

### 🎨 Custom Metodlar

Modellere özel metodlar ekleyebilirsiniz:

```python
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    # 👇 İndirim yüzdesini hesaplayan metod
    def discount_percent(self):
        return int((self.price - self.discount_price) * 100 / self.price)

    # 👇 Başlık ve slug birleştiren metod
    def fulltitle(self):
        return f"{self.title}-{self.slug}"
```

---

### 🔄 save() Metodunu Override Etme

Kaydetmeden önce otomatik işlemler yapabilirsiniz:

```python
from django.utils.text import slugify
import uuid

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Eğer slug boşsa otomatik oluştur
        if not self.slug:
            unique = uuid.uuid4().hex[:8]  # Benzersiz ID
            link = slugify(self.title)     # Türkçe karakterleri düzenle
            self.slug = f"{link}-{unique}"
        super().save(*args, **kwargs)  # Asıl kaydetme işlemi
```

> 💡 **slugify** fonksiyonu Türkçe karakterleri URL-dostu hale getirir:
> `"Laptop Çantası"` → `"laptop-cantasi"`

---

## 🔄 Migration İşlemleri (Veritabanı Güncelleme)

> 💡 **Migration Nedir?** Model değişikliklerini veritabanına uygulayan dosyalardır.

### Temel Komutlar

```bash
# 1. Migration dosyası oluştur (models.py değiştikten sonra)
python manage.py makemigrations

# 2. Migration'ları veritabanına uygula
python manage.py migrate

# 3. Belirli bir app için migration oluştur
python manage.py makemigrations urunler

# 4. Migration geçmişini görüntüle
python manage.py showmigrations

# 5. SQL sorgusunu göster (uygulamadan önce)
python manage.py sqlmigrate urunler 0001
```

### Migration Akışı

```
┌─────────────────────────────────────────────────────────────┐
│                    MODEL DEĞİŞİKLİĞİ                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │   models.py düzenle  │
                  └──────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │   makemigrations     │
                  │   (dosya oluştur)    │
                  └──────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │      migrate         │
                  │   (veritabanına      │
                  │    uygula)           │
                  └──────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  ✅ TAMAMLANDI!  │
                    └──────────────────┘
```

### ⚠️ Önemli Notlar

- Her model değişikliğinden sonra `makemigrations` çalıştırın
- `makemigrations` sadece dosya oluşturur, `migrate` uygular
- Migration dosyalarını silmeyin (versiyon kontrolü için önemli)
- Ekip çalışmasında migration çakışmalarına dikkat edin

---

## 👨‍💼 Admin Paneli Özelleştirme

> 💡 **Admin Paneli**: Django'nun yerleşik veritabanı yönetim arayüzü. `/admin/` adresinden erişilir.

### 1️⃣ Süper Kullanıcı Oluşturma

```bash
python manage.py createsuperuser
```

Kullanıcı adı, e-posta ve şifre girmeniz istenecek.

### 2️⃣ Modeli Admin'e Kaydetme

`urunler/admin.py`:

```python
from django.contrib import admin
from .models import Product, ProductImage, Tag

# Basit kayıt
admin.site.register(Product)
admin.site.register(Tag)
```

### 3️⃣ Admin Görünümünü Özelleştirme

```python
from django.contrib import admin
from .models import Product, ProductImage, Tag

class ProductView(admin.ModelAdmin):
    # Listede gösterilecek alanlar
    list_display = ["title", "slug", "price", "discount_price", "category", "is_active"]

    # Arama yapılabilecek alanlar
    search_fields = ["title", "description"]

    # Filtreleme seçenekleri (sağ tarafta)
    list_filter = ["category", "is_active", "created_at"]

    # Düzenleme formundaki alan sırası
    fields = ["title", "description", "price", "discount_price", "category", "is_active"]

    # Sayfa başına kayıt sayısı
    list_per_page = 20

# Özelleştirilmiş görünümle kaydet
admin.site.register(Product, ProductView)
```

### 4️⃣ Inline (İç İçe) Kayıtlar

Bir ürünün resimlerini ürün sayfasında düzenlemek için:

```python
from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInlineView(admin.TabularInline):
    model = ProductImage
    extra = 3  # Boş form sayısı

class ProductView(admin.ModelAdmin):
    list_display = ["title", "price", "category"]
    inlines = [ProductImageInlineView]  # 👈 Inline ekleme

admin.site.register(Product, ProductView)
```

### 5️⃣ Kategori Admin Örneği

```python
from django.contrib import admin
from .models import Category, SubCategory

class SubCategoryInlineView(admin.TabularInline):
    model = SubCategory
    extra = 5

class CategoryView(admin.ModelAdmin):
    list_display = ["category_name", "category_slug", "category_image"]
    fields = ["category_name", "category_slug", "category_image"]
    search_fields = ["category_name", "category_slug"]
    inlines = [SubCategoryInlineView]  # Alt kategoriler ana kategoride gösterilir

admin.site.register(Category, CategoryView)
admin.site.register(SubCategory)
```

---

## 🔐 Kullanıcı Kimlik Doğrulama (Authentication)

> 💡 **Authentication**: Kullanıcı giriş, çıkış ve kayıt işlemlerini yöneten sistem.

### 1️⃣ Gerekli Import'lar

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib import messages
```

### 2️⃣ Giriş (Login) View

`accounts/views.py`:

```python
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Kullanıcıyı doğrula
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Oturumu başlat
            return redirect('anasayfa')

        messages.error(request, "Kullanıcı bulunamadı")
        return render(request, 'login.html')

    return render(request, "login.html")
```

### 3️⃣ Kayıt (Register) View

```python
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Şifre kontrolü
        if password != confirm_password:
            messages.warning(request, "Şifreler uyuşmuyor!")
            return render(request, "register.html")

        # Kullanıcı adı kontrolü
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Bu kullanıcı adı zaten kullanılıyor!")
            return render(request, "register.html")

        # Yeni kullanıcı oluştur
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.save()

        # Kullanıcıyı bir gruba ekle (opsiyonel)
        role = Group.objects.filter(name="Satıcılar").first()
        if role:
            user.groups.add(role)

        messages.success(request, "Kayıt başarılı! Giriş yapabilirsiniz.")
        return redirect("login")

    return render(request, "register.html")
```

### 4️⃣ Çıkış (Logout) View

```python
def logout_view(request):
    logout(request)
    return redirect('login')
```

### 5️⃣ URL Tanımlamaları

`accounts/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
]
```

### 6️⃣ Template'de Kullanıcı Kontrolü

```html
{% if user.is_authenticated %}
    <p>Hoş geldin, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Çıkış Yap</a>
{% else %}
    <a href="{% url 'login' %}">Giriş Yap</a>
{% endif %}
```

### 7️⃣ Login Form Template

```html
<form method="post" action="{% url 'login' %}">
    {% csrf_token %}

    <label for="username">Kullanıcı Adı</label>
    <input type="text" name="username" id="username" required>

    <label for="password">Şifre</label>
    <input type="password" name="password" id="password" required>

    <button type="submit">GİRİŞ YAP</button>
</form>

<a href="{% url 'forgot_password' %}">Şifremi Unuttum</a>
```

---

## 🔑 Şifre Sıfırlama (Password Reset)

> 💡 Django'nun hazır şifre sıfırlama view'larını kullanarak güvenli bir şifre sıfırlama sistemi kurabilirsiniz.

### 1️⃣ URL Tanımlamaları

`accounts/urls.py`:

```python
from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    # Şifremi unuttum sayfası
    path('forgot-password/', auth_view.PasswordResetView.as_view(
        template_name="forgot_password.html",
        html_email_template_name="password_reset_email.html",
        subject_template_name="password_reset_subject.txt",
        success_url=reverse_lazy("password_reset_done")
    ), name="forgot_password"),

    # E-posta gönderildi sayfası
    path('reset-password/done/', auth_view.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"
    ), name="password_reset_done"),

    # Şifre sıfırlama linki (e-postadan gelen)
    path('reset-password/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name="reset_password.html"
    ), name="password_reset_confirm"),

    # Şifre başarıyla değiştirildi sayfası
    path('reset-password/complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"
    ), name="password_reset_complete"),
]
```

### 2️⃣ E-posta Ayarları

`settings.py`:

```python
# Development için (e-postalar terminalde görünür)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Production için Gmail SMTP:
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@gmail.com'
# EMAIL_HOST_PASSWORD = 'your-app-password'
# DEFAULT_FROM_EMAIL = 'Site Adı <your-email@gmail.com>'

# Şifre sıfırlama linki geçerlilik süresi (saniye)
PASSWORD_RESET_TIMEOUT = 86400  # 24 saat
```

### 3️⃣ Template Örnekleri

`forgot_password.html`:

```html
{% extends 'base.html' %}

{% block content %}
<h1>Şifremi Unuttum</h1>

<form method="post" action="{% url 'forgot_password' %}">
    {% csrf_token %}

    <label for="email">E-Posta Adresi</label>
    <input type="email" name="email" id="email" required>

    <button type="submit">Sıfırlama Bağlantısı Gönder</button>
</form>

<a href="{% url 'login' %}">Giriş sayfasına dön</a>
{% endblock %}
```

`password_reset_email.html` (E-posta şablonu):

```html
Merhaba,

Şifre sıfırlama talebinde bulundunuz.
Aşağıdaki linke tıklayarak yeni şifrenizi belirleyebilirsiniz:

{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}

Bu link 24 saat geçerlidir.

Eğer bu talebi siz yapmadıysanız, bu e-postayı görmezden gelebilirsiniz.
```

---

## 🛡️ İzin Sistemi (Permissions)

> 💡 Django'nun izin sistemi ile kullanıcıların ne yapabileceğini kontrol edebilirsiniz.

### 1️⃣ @login_required Dekoratörü

Sadece giriş yapmış kullanıcıların erişebileceği sayfalar için:

```python
from django.contrib.auth.decorators import login_required

@login_required
def category_home(request):
    # Sadece giriş yapmış kullanıcılar erişebilir
    # Giriş yapmamış kullanıcılar /accounts/login/ sayfasına yönlendirilir
    return render(request, "category_home.html")
```

Login URL'ini ayarlamak için `settings.py`:

```python
LOGIN_URL = '/accounts/login/'
```

### 2️⃣ @permission_required Dekoratörü

Belirli izinlere sahip kullanıcılar için:

```python
from django.contrib.auth.decorators import permission_required

@permission_required("category.add_category", login_url="/accounts/login/")
def category_add(request):
    # Sadece category.add_category iznine sahip kullanıcılar erişebilir
    return render(request, "category_add.html")
```

### 3️⃣ View İçinde İzin Kontrolü

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

@login_required
def category_home(request):
    # Manuel izin kontrolü
    if not request.user.has_perm("category.add_category"):
        messages.error(request, "Bu sayfaya erişim izniniz yok!")
        return redirect('login')

    category_list = Category.objects.all()
    return render(request, "category_home.html", {
        "category_list": category_list
    })
```

### 4️⃣ Template'de İzin Kontrolü

```html
{% if perms.category.add_category %}
    <form method="post">
        {% csrf_token %}
        <input type="text" name="category_name" placeholder="Kategori adı">
        <button type="submit">Ekle</button>
    </form>
{% endif %}

{% if perms.category.delete_category %}
    <a href="{% url 'category_delete' category.id %}">Sil</a>
{% endif %}

{% if perms.category.change_category %}
    <a href="{% url 'category_update' category.id %}">Güncelle</a>
{% endif %}

{% if perms.category.view_category %}
    <a href="{% url 'category_details' category.id %}">Görüntüle</a>
{% endif %}
```

### 5️⃣ Django İzin Türleri

Her model için otomatik oluşturulan izinler:

| İzin | Format | Açıklama |
|------|--------|----------|
| Ekleme | `app.add_model` | Yeni kayıt ekleme |
| Değiştirme | `app.change_model` | Kayıt düzenleme |
| Silme | `app.delete_model` | Kayıt silme |
| Görüntüleme | `app.view_model` | Kayıt görüntüleme |

Örnek: `category.add_category`, `category.delete_category`

---

## 💬 Messages Framework (Bildirim Mesajları)

> 💡 Kullanıcıya işlem sonuçlarını göstermek için kullanılır.

### 1️⃣ View'da Mesaj Ekleme

```python
from django.contrib import messages

def category_home(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')

        if category_name == "":
            messages.warning(request, "Lütfen kategori adını yazınız")
            return redirect('category')

        Category.objects.create(category_name=category_name)
        messages.success(request, "Kategori başarıyla eklendi!")
        return redirect('category')

    return render(request, "category_home.html")
```

### 2️⃣ Mesaj Türleri

```python
messages.debug(request, "Debug mesajı")     # Geliştirici için
messages.info(request, "Bilgi mesajı")      # Genel bilgi
messages.success(request, "Başarılı!")      # Başarılı işlem
messages.warning(request, "Dikkat!")        # Uyarı
messages.error(request, "Hata oluştu!")     # Hata
```

### 3️⃣ Template'de Mesajları Gösterme

```html
{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">
            {{ message }}
        </div>
    {% endfor %}
{% endif %}
```

### 4️⃣ Özel Alert Bileşeni (include ile)

`alert.html`:

```html
<div class="p-4 mb-4 rounded-lg
    {% if tag == 'success' %}bg-green-100 text-green-800{% endif %}
    {% if tag == 'warning' %}bg-yellow-100 text-yellow-800{% endif %}
    {% if tag == 'error' %}bg-red-100 text-red-800{% endif %}
    {% if tag == 'info' %}bg-blue-100 text-blue-800{% endif %}">
    {{ message }}
</div>
```

Kullanımı:

```html
{% for message in messages %}
    {% include 'alert.html' with message=message tag=message.tags %}
{% endfor %}
```

---

## 📤 Dosya Yükleme (File Upload)

> 💡 Kullanıcıların resim ve dosya yüklemesi için gerekli ayarlar.

### 1️⃣ settings.py Ayarları

```python
# Medya dosyaları için URL ve klasör
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 2️⃣ urls.py Ayarları

Ana `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... diğer URL'ler
]

# Geliştirme ortamında medya dosyalarını servis et
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 3️⃣ Model'de ImageField/FileField

```python
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to="kategori_resimleri")
    # Dosyalar media/kategori_resimleri/ klasörüne kaydedilir


class ProductImage(models.Model):
    image = models.ImageField(upload_to="product_images")
    alt_text = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    is_main = models.BooleanField(default=False)
```

> 💡 **ImageField** için `pillow` kütüphanesi gerekir: `pip install pillow`

### 4️⃣ Form'da Dosya Yükleme

```html
<!-- enctype="multipart/form-data" zorunlu! -->
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}

    <label for="file">Resim Seç</label>
    <input type="file" name="file" accept="image/*">

    <button type="submit">Yükle</button>
</form>
```

### 5️⃣ View'da Dosya Alma

```python
def category_home(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        file = request.FILES.get('file')  # 👈 Dosyayı al

        if file is None:
            messages.warning(request, "Lütfen dosya seçin")
            return redirect('category')

        Category.objects.create(
            category_name=category_name,
            category_image=file  # 👈 Dosyayı kaydet
        )
        return redirect('category')
```

### 6️⃣ Template'de Resim Gösterme

```html
<img src="{{ category.category_image.url }}" alt="{{ category.category_name }}">
```

---

## 🎨 Static Dosyalar (CSS, JS, Resimler)

> 💡 Sitenin tasarımı için kullanılan dosyalar (CSS, JavaScript, ikonlar vb.)

### 1️⃣ settings.py Ayarları

```python
STATIC_URL = 'static/'

# Proje seviyesinde static klasörler (opsiyonel)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

### 2️⃣ Klasör Yapısı

```
eticaret/
├── eticaret/
│   └── static/
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── main.js
│       └── img/
│           ├── banner.gif
│           └── icon/
│               ├── facebook.webp
│               └── instagram.webp
```

### 3️⃣ Template'de Static Kullanımı

```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <img src="{% static 'img/banner.gif' %}" alt="banner">

    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>
```

> ⚠️ **Önemli**: Her template'in başında `{% load static %}` yazmayı unutmayın!

---

## 🔗 Include Template Tag

> 💡 Tekrar eden HTML parçalarını ayrı dosyalara ayırıp dahil etme.

### Kullanım

```html
<!-- footer.html dosyasını dahil et -->
{% include 'footer.html' %}

<!-- Değişken göndererek dahil et -->
{% include 'alert.html' with message=message tag=message.tags %}

<!-- Birden fazla değişken göndererek -->
{% include 'card.html' with title=product.title price=product.price %}
```

### Örnek: Footer Include

`footer.html`:

```html
<footer>
    <p>&copy; 2025 E-Ticaret Sitesi</p>
    <div>
        <a href="#"><img src="{% static 'img/icon/facebook.webp' %}" alt="Facebook"></a>
        <a href="#"><img src="{% static 'img/icon/instagram.webp' %}" alt="Instagram"></a>
    </div>
</footer>
```

`base.html`:

```html
<body>
    <header>...</header>
    <main>{% block content %}{% endblock %}</main>
    {% include 'footer.html' %}
</body>
```

---

## 🌍 Dil ve Zaman Dilimi Ayarları

`settings.py`:

```python
# Türkçe dil ayarı
LANGUAGE_CODE = 'tr-TR'

# İstanbul zaman dilimi
TIME_ZONE = 'Europe/Istanbul'

# Uluslararasılaştırma aktif
USE_I18N = True

# Zaman dilimi aktif
USE_TZ = True
```

### Tarih Formatları

Template'de:

```html
{{ urun.created_at|date:"d/m/Y" }}       <!-- 25/01/2025 -->
{{ urun.created_at|date:"d F Y" }}       <!-- 25 Ocak 2025 -->
{{ urun.created_at|date:"d.m.Y H:i" }}   <!-- 25.01.2025 14:30 -->
```

---

## 🛠️ get_object_or_404 Kullanımı

> 💡 Kayıt bulunamazsa otomatik 404 hatası döndürür.

```python
from django.shortcuts import get_object_or_404

def category_update(request, id):
    # Eğer kategori bulunamazsa otomatik 404 sayfası gösterilir
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        category.category_name = request.POST.get('category_name')
        category.save()
        return redirect('category')

    return render(request, "update_category.html", {"category": category})
```

### Normal Yöntem vs get_object_or_404

```python
# ❌ Uzun yol
def category_details(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404("Kategori bulunamadı")
    return render(request, "category_detail.html", {"category": category})

# ✅ Kısa yol
def category_details(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, "category_detail.html", {"category": category})
```

---

## 🔍 QuerySet Metodları (Veritabanı Sorguları)

> 💡 **QuerySet Nedir?** Django ORM'in veritabanından veri çekmek için kullandığı sorgulardır. SQL yazmadan veritabanı işlemleri yapmanızı sağlar.

### 1️⃣ Temel Sorgulama Metodları

```python
from .models import Category

# Tüm kayıtları getir
Category.objects.all()

# Tek bir kayıt getir (bulunamazsa hata verir)
Category.objects.get(id=1)

# Filtreleme yap (birden fazla kayıt dönebilir)
Category.objects.filter(category_name="Elektronik")

# İlk kaydı getir (bulunamazsa None döner)
Category.objects.filter(id=5).first()

# Son kaydı getir
Category.objects.last()

# Kayıt sayısını öğren
Category.objects.count()
```

### 2️⃣ filter() vs get() vs first()

| Metod | Bulunamazsa | Birden fazla kayıt | Kullanım |
|-------|-------------|-------------------|----------|
| `get()` | **Hata verir** | **Hata verir** | Tek kayıt kesin varsa |
| `filter()` | Boş QuerySet | Hepsini döner | Birden fazla kayıt olabilirse |
| `first()` | **None döner** | İlkini döner | Hata istemiyorsan |

### 3️⃣ filter().first() Kullanımı

```python
def category_details(request, id):
    # ✅ Güvenli yol - kayıt bulunamazsa None döner
    category = Category.objects.filter(id=id).first()

    if category is None:
        # Kayıt bulunamadı, ne yapacağına karar ver
        messages.error(request, "Kategori bulunamadı")
        return redirect('category')

    return render(request, "category_detail.html", {
        "category": category
    })
```

### 4️⃣ get() Kullanımı

```python
def category_details(request, id):
    try:
        # ⚠️ Kayıt bulunamazsa DoesNotExist hatası verir
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        messages.error(request, "Kategori bulunamadı")
        return redirect('category')

    return render(request, "category_detail.html", {
        "category": category
    })
```

### 5️⃣ Filtreleme Örnekleri

```python
# Tam eşleşme
Category.objects.filter(category_name="Elektronik")

# İçinde geçen (case-sensitive)
Category.objects.filter(category_name__contains="elek")

# İçinde geçen (case-insensitive)
Category.objects.filter(category_name__icontains="elek")

# Başlayan
Category.objects.filter(category_name__startswith="Elekt")

# Biten
Category.objects.filter(category_name__endswith="ik")

# Büyük/küçük karşılaştırma
Product.objects.filter(price__gt=100)      # > 100
Product.objects.filter(price__gte=100)     # >= 100
Product.objects.filter(price__lt=100)      # < 100
Product.objects.filter(price__lte=100)     # <= 100

# Aralık
Product.objects.filter(price__range=(100, 500))

# Liste içinde mi
Product.objects.filter(id__in=[1, 2, 3, 4])

# NULL kontrolü
Product.objects.filter(description__isnull=True)
```

### 6️⃣ Birden Fazla Koşul

```python
# VE (AND) - virgülle ayır
Product.objects.filter(is_active=True, price__lt=1000)

# VEYA (OR) - Q objesi kullan
from django.db.models import Q
Product.objects.filter(Q(price__lt=100) | Q(is_active=False))

# DEĞİL (NOT) - exclude kullan
Product.objects.exclude(is_active=False)
```

### 7️⃣ Sıralama ve Limitleme

```python
# Artan sıralama
Category.objects.all().order_by('category_name')

# Azalan sıralama (başına - koy)
Category.objects.all().order_by('-id')

# Birden fazla sıralama kriteri
Product.objects.all().order_by('category', '-price')

# İlk 5 kayıt
Category.objects.all()[:5]

# 5. ile 10. arası kayıtlar
Category.objects.all()[5:10]
```

### 8️⃣ CRUD İşlemleri (Oluştur, Oku, Güncelle, Sil)

```python
# CREATE - Yeni kayıt oluşturma
category = Category.objects.create(
    category_name="Elektronik",
    category_slug="elektronik",
    category_image=file
)

# READ - Okuma
category = Category.objects.get(id=1)
categories = Category.objects.all()

# UPDATE - Güncelleme
category = Category.objects.get(id=1)
category.category_name = "Yeni İsim"
category.save()

# Toplu güncelleme
Category.objects.filter(is_active=False).update(is_active=True)

# DELETE - Silme
category = Category.objects.get(id=1)
category.delete()

# Toplu silme
Category.objects.filter(is_active=False).delete()
```

### 9️⃣ İlişkili Verilere Erişim

```python
# ForeignKey üzerinden erişim (alt kategoriye git)
subcategory = SubCategory.objects.get(id=1)
parent = subcategory.parent_category  # Ana kategoriye eriş

# Tersine erişim (related_name ile)
category = Category.objects.get(id=1)
subcategories = category.altkategoriler.all()  # Tüm alt kategoriler

# İlişkili kayıt var mı kontrolü
if category.products.exists():
    messages.warning(request, "Bu kategoriye bağlı ürünler var!")
```

### 🔟 exists() Kullanımı

```python
def category_delete(request, id):
    category = get_object_or_404(Category, id=id)

    # Bu kategoriye bağlı ürün var mı kontrol et
    if category.products.exists():
        messages.warning(request, "Lütfen önce bağlı ürünleri silin")
        return redirect('category')

    category.delete()
    messages.success(request, "Kategori silindi")
    return redirect('category')
```

---

## 🔄 redirect() Fonksiyonu (Sayfa Yönlendirme)

> 💡 **redirect Nedir?** Kullanıcıyı başka bir sayfaya yönlendirmek için kullanılır. Form gönderildikten sonra veya işlem tamamlandıktan sonra kullanılır.

### 1️⃣ Temel Kullanım

```python
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # 'login' URL name'ine yönlendir
```

### 2️⃣ redirect() Kullanım Yöntemleri

```python
# 1. URL Name ile (ÖNERİLEN)
return redirect('anasayfa')
return redirect('category')
return redirect('login')

# 2. URL Path ile
return redirect('/accounts/login/')
return redirect('/category/')

# 3. Parametre ile URL Name
return redirect('category_details', id=5)
return redirect('urun_detay', urun_id=10, slug='laptop')

# 4. Model objesi ile (get_absolute_url gerekir)
return redirect(category_obj)
```

### 3️⃣ Form İşlemlerinde redirect

```python
def category_home(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')

        # Validasyon hatası - aynı sayfaya yönlendir
        if category_name == "":
            messages.warning(request, "Lütfen kategori adını yazınız")
            return redirect('category')  # 👈 Aynı sayfaya dön

        # Başarılı - kaydet ve yönlendir
        Category.objects.create(category_name=category_name)
        messages.success(request, "Kategori eklendi!")
        return redirect('category')  # 👈 Listeye dön

    # GET isteği - sayfayı göster
    return render(request, "category_home.html")
```

### 4️⃣ İzin Kontrolünde redirect

```python
@login_required
def category_home(request):
    # İzin yoksa login sayfasına yönlendir
    if not request.user.has_perm("category.add_category"):
        messages.error(request, "Bu sayfaya erişim izniniz yok!")
        return redirect('login')

    return render(request, "category_home.html")
```

### 5️⃣ CRUD İşlemlerinde redirect

```python
# CREATE - Oluşturma sonrası
def category_create(request):
    if request.method == "POST":
        # ... kayıt oluştur
        messages.success(request, "Kategori oluşturuldu!")
        return redirect('category')  # Listeye dön
    return render(request, "category_create.html")


# UPDATE - Güncelleme sonrası
def category_update(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        category.category_name = request.POST.get('category_name')
        category.save()
        messages.success(request, "Kategori güncellendi!")
        return redirect('category')  # Listeye dön

    return render(request, "category_update.html", {"category": category})


# DELETE - Silme sonrası
def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, "Kategori silindi!")
    return redirect('category')  # Listeye dön
```

### 6️⃣ redirect vs render Karşılaştırması

| Özellik | `redirect()` | `render()` |
|---------|--------------|------------|
| **Ne yapar** | Yeni URL'e yönlendirir | Aynı URL'de template gösterir |
| **HTTP Kodu** | 302 (Found/Redirect) | 200 (OK) |
| **URL değişir mi** | Evet | Hayır |
| **Form tekrar gönderimi** | Engeller (PRG Pattern) | Engellenmez |
| **Kullanım** | Form işlemi sonrası | Sayfa ilk yüklemede |

### 7️⃣ PRG Pattern (Post-Redirect-Get)

> 💡 Form gönderildikten sonra `redirect` kullanmak, kullanıcı sayfayı yenilediğinde formun tekrar gönderilmesini engeller.

```python
def category_create(request):
    if request.method == "POST":
        # Form işle
        Category.objects.create(...)

        # ✅ DOĞRU: Redirect kullan - yenileme sorunu olmaz
        return redirect('category')

        # ❌ YANLIŞ: Render kullan - yenilemede form tekrar gönderilir
        # return render(request, "success.html")

    return render(request, "category_create.html")
```

```
POST İsteği (Form Gönder)
         │
         ▼
┌─────────────────────┐
│  Form işle, kaydet  │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  redirect('liste')  │  ← 302 Redirect
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  GET /liste/        │  ← Yeni istek
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Sayfa göster       │  ← Yenilemede form gönderilmez
└─────────────────────┘
```

---

## 📊 Proje Yapısı Özeti

```
eticaret/
│
├── manage.py                 # Django yönetim komutları
│
├── eticaret/                 # Ana proje klasörü
│   ├── __init__.py
│   ├── settings.py           # Proje ayarları
│   ├── urls.py               # Ana URL yönlendirmeleri
│   ├── views.py              # Ana view'lar
│   ├── wsgi.py
│   ├── asgi.py
│   ├── static/               # Static dosyalar (CSS, JS, IMG)
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   └── templates/            # Proje seviyesi template'ler
│       ├── base.html
│       ├── home.html
│       ├── footer.html
│       └── alert.html
│
├── accounts/                 # Kullanıcı yönetimi app'i
│   ├── models.py
│   ├── views.py              # login, register, logout
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       ├── login.html
│       ├── register.html
│       ├── forgot_password.html
│       └── reset_password.html
│
├── category/                 # Kategori yönetimi app'i
│   ├── models.py             # Category, SubCategory modelleri
│   ├── views.py              # CRUD işlemleri
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       ├── category_home.html
│       └── category_detail.html
│
├── urunler/                  # Ürün yönetimi app'i
│   ├── models.py             # Product, Tag, ProductImage
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│
├── media/                    # Yüklenen dosyalar
│   ├── kategori_resimleri/
│   └── product_images/
│
└── db.sqlite3                # SQLite veritabanı
```

---

## 🤔 Sık Sorulan Sorular

### S: Sanal ortam neden gerekli?
**C:** Her proje için ayrı paket versiyonları kullanabilirsiniz. Bir projede Django 4.0, diğerinde Django 5.0 kullanabilirsiniz.

### S: 'django-admin' komutu çalışmıyor?
**C:** Django kurulu olmayabilir. `pip install django` komutunu çalıştırın ve sanal ortamın aktif olduğundan emin olun.

### S: Sunucu başlatılamıyor, port kullanımda diyor?
**C:** 8000 portu başka bir program tarafından kullanılıyor. `python manage.py runserver 8080` ile farklı port deneyin.

### S: manage.py bulunamadı hatası?
**C:** Proje klasörünün içinde olduğunuzdan emin olun: `cd eticaret`

### S: base.html nerede olmalı?
**C:** İki seçenek var:
1. Proje seviyesi: `proje_adi/templates/base.html` (önerilen)
2. App seviyesi: `app_adi/templates/base.html`

Proje seviyesinde kullanmak için `settings.py`'de `TEMPLATES['DIRS']` ayarını yapın.

### S: {% extends %} nereye yazılır?
**C:** Her zaman template dosyasının **ilk satırına** yazılmalıdır. Üstünde hiçbir HTML kodu olmamalı.

### S: {% block %} kapatmayı unutursam ne olur?
**C:** `TemplateSyntaxError` hatası alırsınız. Her `{% block %}` mutlaka `{% endblock %}` ile kapatılmalı.

### S: Dinamik URL'de parametre geçmiyor?
**C:** URL pattern'deki parametre adı ile view fonksiyonundaki parametre adı **aynı** olmalı:
```python
# urls.py
path('<int:urun_id>/', views.detay)
# views.py
def detay(request, urun_id):  # Aynı isim!
```

### S: Template bulunamadı hatası alıyorum?
**C:** Klasör yapısını kontrol edin: `templates/app_adi/dosya.html`

### S: CSS/JS dosyalarım yüklenmiyor?
**C:** `{% load static %}` yazmayı unutmuş olabilirsiniz.

### S: URL'ler çalışmıyor?
**C:** `settings.py`'de `INSTALLED_APPS`'e app'inizi eklediniz mi?

### S: Context verisi görünmüyor?
**C:** Dictionary'deki anahtar (key) ile template'deki değişken adı aynı mı?

### S: Migration hatası alıyorum?
**C:** `python manage.py makemigrations` komutunu çalıştırdınız mı? Sonra `migrate` yapın.

### S: {% url %} tag'i hata veriyor?
**C:** `urls.py`'de tanımladığınız `name` parametresini doğru yazdığınızdan emin olun:
```python
# urls.py
path('', views.anasayfa, name='anasayfa')
# template'de
{% url 'anasayfa' %}  # Tırnak içinde!
```

### S: base.html'deki stil alt sayfalara gelmiyor?
**C:** Alt sayfada `{% extends 'base.html' %}` yazdınız mı? Ve bu satır dosyanın en üstünde mi?

---

<div align="center">

### 🌟 Başarılar Dilerim!

**Sorularınız için:** [huseyint428@gmail.com](mailto:huseyint428@gmail.com)

Made with ❤️ and ☕ by Hüseyin Tunç

![Django](https://img.shields.io/badge/Django-Template-092E20?style=flat-square&logo=django)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner-green?style=flat-square)
![Turkish](https://img.shields.io/badge/Language-Turkish-red?style=flat-square)

</div>
