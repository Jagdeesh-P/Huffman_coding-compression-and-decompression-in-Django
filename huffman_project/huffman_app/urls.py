from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('download/compressed/', views.download_compressed, name='download_compressed'),
    path('download/decompressed/', views.download_decompressed, name='download_decompressed'),
]
