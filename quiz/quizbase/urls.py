from . import views
from django.urls import path

urlpatterns=[
    path('',views.homePage,name="home"),
    path('game/',views.start_game,name='game'),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('result/',views.start_game,name='result'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutPage,name='logout'),
    path('register/', views.registerPage,name='register'),


]