from django.urls import path
from rent import views

urlpatterns = [
    path('home/', views.home, name='home-page'),
    # crud :
    path('list/', views.pool_list, name='pool-list'),
    path('detail/<int:pool_pk>/', views.pool_detail, name='pool-detail'),
    path('poolcreation/', views.create_pool, name='pool-creation'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # logs :
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='login'),
    path('index', views.index, name='index'),
    path('special/', views.special, name='special'),
    path('logout/', views.user_logout, name='logout'),
]
