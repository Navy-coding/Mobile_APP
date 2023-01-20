from django.urls import path
from Mobile_App import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('products/', views.product_list, name='product_list'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_history/', views.order_history, name='order_history'),
]