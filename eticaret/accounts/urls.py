from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_view,name="login"),
    path('register/',views.register_view,name="register"),
    path('forgot-password/',views.forgot_password_view,name="forgot_password"),
    path('reset-password/',views.reset_password_view,name="reset_password"),
    path('logout/',views.logout_view,name="logout")
]
