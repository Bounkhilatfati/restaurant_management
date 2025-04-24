from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('dishes/', views.DishListView.as_view(), name='dish_list'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/new/', views.create_order, name='create_order'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/<int:pk>/edit/', views.order_edit, name='order_edit'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
]
