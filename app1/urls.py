from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.Homepage),
    path('SignupPage',views.SignupPage),
    path('LoginPage', views.LoginPage),
    path('LogoutPage', views.LogoutPage),
    
]

