from django.urls import path
from rent import views

urlpatterns = [
    path('list/', views.pool_list, name='pool_list'),
    path('detail/<int:pool_pk>/', views.pool_detail, name='pool_detail'),
]
