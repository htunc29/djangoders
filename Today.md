# Django Ders 2
## Bugün Yapacaklarımız
1. Kullanıcılar App Oluştur
1. Kullanıcılar Sayfası (.html)  oluştur ve render et
1. Sayfaya link verme ve yönlendirmeler path(name="") olayı
1. Sayfaya context ile veri gönderme
1. Sayfada context ile gönderilen veriyi görüntüleme
1. Dinamik url tanımlama ve sayfalarda kullanma
1. Sayfada {{if}} kullanımı (olup olmama durumları)
1. Fake user control
1. Sayfada {{for}} kullanımı (Dummy ürün listesi)
1. Django tagleri
1. Kendi django tagimizi oluşturma


## Kullanıcı App'i Oluşturma
> Kullanıcı Uygulaması oluşturma:
```
django-admin startapp kullanicilar`
```

## Kullanıcılar Sayfası (.html)  oluştur ve render et
```python
from django.shortcuts import render
def kullanicilar(request):
    return render(request,"user.html")
```
## Sayfaya link verme ve yönlendirmeler
```django
<a href={% url 'home'%}>Anasayfa</a>
```
```django
<a href={% url 'home'%}>Anasayfa</a>
```
