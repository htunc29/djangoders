# 20-26 Ekim
1. Kullanıcılar App Oluştur
2. Kullanıcılar Sayfası (.html)  oluştur ve render et
3. Sayfaya link verme ve yönlendirmeler path(name="") olayı
4. Sayfaya context ile veri gönderme
5. Sayfada context ile gönderilen veriyi görüntüleme
6. Sayfada {{for}} kullanımı (Dummy ürün listesi)
7. Sayfada {{if}} kullanımı (olup olmama durumları)
8. Django tagleri
9. Fake user control

'''
{{ urun.fiyat|floatformat:2 }}   {# 2 ondalıklı gösterir #}
{{ urun.aciklama|truncatechars:50 }}   {# 50 karaktere kısaltır #}
{{ urun.tarih|date:"d.m.Y" }}
{% url 'urun_detay' urun.slug %}

'''
# 27 Ekim - 2 Kasım
0. Dinamik url tanımlama
1. Base.html mantığı
1. Static dosyadan statik dosyaları çağırma (css,js,image)
4. Partial view
#  10 Kasım - 16 Kasım
1. Migrate nedir ?
2. Model sınıflarını oluşturma models.py
2. Veritabanı veri türleri textfield() imagefield() filefield()
3. Admin.py ile model'i kayıt etme
4. Makemigrations işlemleri




