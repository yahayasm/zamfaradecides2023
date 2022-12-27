from django.urls import path
from . import views


urlpatterns = [
    path('', views.Userlogin, name="login"),
    path('index', views.dashboard),
    path('logout/', views.logout, name="logout"),
]