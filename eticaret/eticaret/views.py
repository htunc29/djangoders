from django.shortcuts import render


def home(request):
    urunler=[
        {
            "urun_adi":"Monster Notebook",
            "aciklama":"Monster Notebook Abra A21.1 Oyuncu Bilgisayarı",
            "fiyat":51999.99,
            "resimler":[
                "https://cdn.cimri.io/image/1000x1000/monster-notebook-abra-a5-v17-2-i5-11400h-8gb-ram-500gb-ssd-rtx3050-ti-4gb-15-6-inc-dizustu-bilgisayar_896373398.jpg" ,

                "https://storage-monsternotebook-tr.mncdn.com/mnresize/2000/-/monsternotebook-tr/UPLOAD/SEMRUK/S7_V5/Semruk-S7-v5_01_1080sli.jpg"
            ]
        },
        {
            "urun_adi":"Asus Notebook",
            "aciklama":"Asus Notebook Abra A21.1 Oyuncu Bilgisayarı",
            "fiyat":51999.99,
            "resimler":[
                "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSRqXRdD1AIoQV6U7K026_zVynQmIqLweppMZVviLw_cwawxo6IPliA1b6sc9ScJ_qPEPpLkvAIXuu-yPejw3AInelB9_tE0pXDFkX1TeCpHc8-9q-gnr_C" ,
                "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcR1mqSXeNfRoH1rVbd63JZGS8OT-xPpI3zDLcTZKKHm9oNckeUua_jHeaRUJ-9565ptag09PBvxLzEso5A8gCiC8pK2Vt74rWcJQi1YSfJ2NgiJgHi92NC7eg"
            ]
        },
    ]
    return render(request,"home.html",{
        "urunler":urunler
    })

def category(request,kategori_adi):
    return render(request,"kategori.html",{
        "kategori":kategori_adi
    })
