from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_to_base64, name='base64'),
    path('get_base64/<str:pk>/', views.get_base64_link, name='get-base64'),
    path('delete/<str:pk>/', views.delete_table, name='delete-table'),
]
