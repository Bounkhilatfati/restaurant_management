from django import forms
from .models import Category, Dish, Order, OrderItem
from django.forms.models import inlineformset_factory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price', 'description', 'image', 'category']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['dish', 'quantity']


OrderItemFormSet = inlineformset_factory(
    Order, OrderItem, form=OrderItemForm,
    extra=1, can_delete=True
)
