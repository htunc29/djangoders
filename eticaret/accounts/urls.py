from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('login/',views.login_view,name="login"),
    path('register/',views.register_view,name="register"),
    path('logout/',views.logout_view,name="logout"),
    path('forgot-password/',views.forgot_password_view,name="forgot_password")
]
