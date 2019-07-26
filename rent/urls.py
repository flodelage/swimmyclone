from django.urls import path
from rent import views

urlpatterns = [
    path('list/', views.pool_list, name='pool_list'),
    #path('pools/detail/<int:pool_id>/', views.pool_detail, name='pool_detail'),
]
