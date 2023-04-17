from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/', views.registerpage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('forgetpassword/',views.forgetpassword,name="forgetpassword"),
    # path('resetpassword/',views.resetpassword,name="resetpassword"),
]
