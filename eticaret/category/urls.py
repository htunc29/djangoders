from django.urls import path
from . import views

urlpatterns = [
    path('',views.category_home,name="category"),
    path('delete/<int:id>/',views.category_delete,name="category_delete"),
    path('update/<int:id>/',views.category_update,name="category_update"),
    path('details/<int:id>/',views.category_details,name="category_details")
]

