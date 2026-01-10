from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # CRUD
    path('book/', views.book, name='book'),                 # CREATE
    path('list/', views.booking_list, name='booking_list'), # READ
    path('update/<int:pk>/', views.booking_update, name='booking_update'),  # UPDATE
    path('delete/<int:pk>/', views.booking_delete, name='booking_delete'),  # DELETE

    path('success/', views.success, name='success'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
]
