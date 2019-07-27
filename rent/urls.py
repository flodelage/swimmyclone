from django.urls import path
from rent import views

urlpatterns = [
    path('home/', views.home, name='home-page'),
    path('list/', views.pool_list, name='pool-list'),
    path('detail/<int:pool_pk>/', views.pool_detail, name='pool-detail'),
    path('create/')
]
