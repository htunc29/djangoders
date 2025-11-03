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


9. [Pratik Örnekler](#-pratik-yapalım)
   - Ürün Listesi
   - Blog Sistemi

10. [Komutlar & SSS](#-komutlar-cheat-sheet)

---

## 📚 Bu Derste Neler Öğreneceğiz?

✅ Django projesi başlatma (startproject)  
✅ Sanal ortam oluşturma ve yönetme  
✅ Yeni bir Django app oluşturma  
✅ HTML sayfaları (template) hazırlama  
✅ Sayfalara veri gönderme  
✅ Listelerle çalışma (for döngüsü)  
✅ Koşullu durumlar (if-else)  
✅ Sayfa linkleri oluşturma  

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
