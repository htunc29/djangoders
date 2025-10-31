# Django E-Ticaret Projesi - Öğrenci Rehberi

Bu proje, Django framework'ünü sıfırdan öğrenmek için hazırlanmış bir örnek e-ticaret uygulamasıdır.

## İçindekiler
- [Gereksinimler](#gereksinimler)
- [Kurulum Adımları](#kurulum-adımları)
- [Proje Yapısı](#proje-yapısı)
- [Adım Adım Proje Oluşturma](#adım-adım-proje-oluşturma)
- [URL Yapılandırması](#url-yapılandırması)
- [Views ve Templates](#views-ve-templates)
- [Çalıştırma](#çalıştırma)

---

## Gereksinimler

- Python 3.10 veya üzeri
- pip (Python paket yöneticisi)

---

## Kurulum Adımları

### 1. Sanal Ortam (Virtual Environment) Oluşturma

Sanal ortam, projenin bağımlılıklarını sistem genelindeki Python paketlerinden izole etmek için kullanılır.

```bash
# Windows için
python -m venv sanalortam

# Sanal ortamı aktif etme (Windows)
sanalortam\Scripts\activate

# Sanal ortamı aktif etme (Linux/Mac)
source sanalortam/bin/activate
```

**Not:** Sanal ortam aktif olduğunda terminal başında `(sanalortam)` yazısını görmelisiniz.

### 2. Django Kurulumu

```bash
pip install django
```

Django versiyonunu kontrol etmek için:
```bash
python -m django --version
```

---

## Adım Adım Proje Oluşturma

### 1. Django Projesi Oluşturma

```bash
django-admin startproject eticaret
cd eticaret
```

Bu komut şu yapıyı oluşturur:
```
eticaret/
    manage.py
    eticaret/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

**Dosyaların Açıklaması:**
- `manage.py`: Projeyi yönetmek için kullanılan komut satırı aracı
- `settings.py`: Proje ayarlarının bulunduğu dosya
- `urls.py`: URL yönlendirmelerinin tanımlandığı dosya
- `wsgi.py` / `asgi.py`: Web sunucusu için giriş noktaları

### 2. Django Uygulaması (App) Oluşturma

Django'da projeler birden fazla uygulamadan oluşur. Her uygulama belirli bir işlevi yerine getirir.

```bash
python manage.py startapp urunler
```

Bu komut şu yapıyı oluşturur:
```
urunler/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
    migrations/
```

**Dosyaların Açıklaması:**
- `models.py`: Veritabanı modellerinin tanımlandığı yer
- `views.py`: İş mantığının ve görünümlerin bulunduğu dosya
- `admin.py`: Django yönetici paneli yapılandırması
- `migrations/`: Veritabanı değişikliklerinin takip edildiği klasör

### 3. Uygulamayı Projeye Kaydetme

`eticaret/settings.py` dosyasını açın ve `INSTALLED_APPS` listesine uygulamanızı ekleyin:

```python
INSTALLED_APPS = [
    'urunler.apps.UrunlerConfig',  # Yeni eklenen satır
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### 4. Templates Klasörü Oluşturma

HTML şablonlarını saklamak için `urunler` uygulaması içinde `templates` klasörü oluşturun:

```bash
# urunler klasörü içindeyken
mkdir templates
```

Yapı şöyle olmalı:
```
urunler/
    templates/
        index.html
        telefon.html
```

---

## Views ve Templates

### Views Oluşturma

`urunler/views.py` dosyasını açın ve görünümlerinizi tanımlayın:

```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Ana sayfa görünümü - HTML template döndürür"""
    return render(request, "index.html")

def telefon(request):
    """Telefon sayfası görünümü - Basit metin döndürür"""
    return HttpResponse("Telefon sayfası")
```

**View Türleri:**
1. **render()**: HTML şablonu döndürür
2. **HttpResponse()**: Basit metin/HTML döndürür

### Template Oluşturma

`urunler/templates/index.html`:

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ana Sayfa</title>
</head>
<body>
    <h1>Anasayfa</h1>
    <p>E-ticaret sitemize hoş geldiniz!</p>
</body>
</html>
```

---

## URL Yapılandırması

### 1. Uygulama URL'lerini Tanımlama

`urunler/urls.py` dosyası oluşturun:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),              # /urunler/
    path('telefon/', views.telefon, name="telefon") # /urunler/telefon/
]
```

**URL Parametreleri:**
- İlk parametre: URL yolu (route)
- İkinci parametre: Çağrılacak view fonksiyonu
- `name`: URL'ye verilen isim (template'lerde kullanılır)

### 2. Ana Proje URL'lerine Dahil Etme

`eticaret/urls.py` dosyasını düzenleyin:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('urunler/', include('urunler.urls')),  # urunler uygulamasını dahil et
    path('admin/', admin.site.urls),
]
```

**URL Yapısı:**
- `http://127.0.0.1:8000/urunler/` → Ana sayfa
- `http://127.0.0.1:8000/urunler/telefon/` → Telefon sayfası
- `http://127.0.0.1:8000/admin/` → Yönetici paneli

---

## Veritabanı İşlemleri

### Migration (Göç) İşlemleri

Django, veritabanı şemasını yönetmek için migration sistemi kullanır.

```bash
# Migration dosyalarını oluşturma
python manage.py makemigrations

# Migration'ları veritabanına uygulama
python manage.py migrate
```

**İlk migrate komutu şunları oluşturur:**
- Kullanıcı tabloları
- Oturum tabloları
- Yönetici paneli tabloları
- İzinler ve gruplar tabloları

---

## Çalıştırma

### Geliştirme Sunucusunu Başlatma

```bash
python manage.py runserver
```

Tarayıcınızda şu adresleri ziyaret edin:
- Ana sayfa: http://127.0.0.1:8000/urunler/
- Telefon sayfası: http://127.0.0.1:8000/urunler/telefon/

### Sunucuyu Durdurma

Terminal'de `Ctrl + C` tuşlarına basın.

---

## Proje Yapısı

```
djangodersi/
│
├── sanalortam/              # Sanal ortam klasörü
│
└── eticaret/                # Ana proje klasörü
    ├── manage.py            # Django yönetim komutu
    ├── db.sqlite3           # SQLite veritabanı
    │
    ├── eticaret/            # Proje ayarları klasörü
    │   ├── __init__.py
    │   ├── settings.py      # Proje ayarları
    │   ├── urls.py          # Ana URL yapılandırması
    │   ├── wsgi.py
    │   └── asgi.py
    │
    └── urunler/             # Urunler uygulaması
        ├── __init__.py
        ├── admin.py         # Admin panel ayarları
        ├── apps.py          # Uygulama yapılandırması
        ├── models.py        # Veritabanı modelleri
        ├── tests.py         # Test dosyaları
        ├── views.py         # Görünüm fonksiyonları
        ├── urls.py          # Uygulama URL'leri
        │
        ├── migrations/      # Veritabanı migration'ları
        │   └── __init__.py
        │
        └── templates/       # HTML şablonları
            ├── index.html
            └── telefon.html
```

---

## Önemli Django Komutları

```bash
# Yeni proje oluşturma
django-admin startproject proje_adi

# Yeni uygulama oluşturma
python manage.py startapp uygulama_adi

# Geliştirme sunucusunu başlatma
python manage.py runserver

# Migration oluşturma
python manage.py makemigrations

# Migration'ları uygulama
python manage.py migrate

# Süper kullanıcı oluşturma (admin paneli için)
python manage.py createsuperuser

# Django shell'i açma (Python yorumlayıcısı)
python manage.py shell
```

---

## Settings.py Önemli Ayarları

```python
# Dil ayarı
LANGUAGE_CODE = 'tr-TR'  # Türkçe

# Zaman dilimi
TIME_ZONE = 'UTC'

# Debug modu (Geliştirme: True, Production: False)
DEBUG = True

# İzin verilen host'lar (Production'da doldurulmalı)
ALLOWED_HOSTS = []

# Veritabanı ayarı (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

---

## Django MTV Mimarisi

Django, **MTV (Model-Template-View)** mimarisini kullanır:

1. **Model (models.py)**: Veritabanı yapısını tanımlar
2. **Template (HTML dosyaları)**: Kullanıcının gördüğü arayüz
3. **View (views.py)**: İş mantığı ve veri işleme

**İstek Akışı:**
```
Kullanıcı → URL → View → Model (varsa) → Template → Yanıt
```

---

## Sık Karşılaşılan Hatalar ve Çözümleri

### 1. "ModuleNotFoundError: No module named 'django'"
**Çözüm:** Django kurulu değil veya sanal ortam aktif değil
```bash
pip install django
```

### 2. "TemplateDoesNotExist"
**Çözüm:** Template dosyası yanlış yerde veya INSTALLED_APPS'e uygulama eklenmemiş


---

## Sonraki Adımlar

1. **Model Oluşturma**: Ürünler için veritabanı modeli tanımlama
2. **Admin Panel**: Django admin panelinde ürünleri yönetme
3. **Form İşlemleri**: Kullanıcı girişlerini işleme
4. **Statik Dosyalar**: CSS, JavaScript ve görseller ekleme
5. **Veritabanı İlişkileri**: Kategoriler, yorumlar gibi ilişkili tablolar
6. **Kullanıcı Yetkilendirme**: Login/Logout işlemleri
7. **Template Inheritance**: Ana şablon oluşturma

---

## Faydalı Kaynaklar

- **Resmi Django Dokümantasyonu**: https://docs.djangoproject.com/
- **Django Tutorial (Türkçe)**: https://docs.djangoproject.com/tr/
- **Django Girls Tutorial**: https://tutorial.djangogirls.org/tr/

---

## Lisans

Bu proje eğitim amaçlıdır ve özgürce kullanılabilir.

---

**Hazırlayan:** Django Dersi
**Tarih:** 2025
**Amaç:** Öğrencilere Django framework'ünü adım adım öğretmek
