from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('dishes/', views.DishListView.as_view(), name='dish_list'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/new/', views.create_order, name='create_order'),
]
