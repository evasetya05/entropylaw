from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_perkara, name='daftar_perkara'),
    path('baru/', views.kalkulasi_baru, name='kalkulasi_baru'),
    path('<int:pk>/', views.detail_perkara, name='detail_perkara'),
]