from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Category, Dish, Order
from .forms import CategoryForm, DishForm, OrderForm, OrderItemFormSet
from django.shortcuts import render, get_object_or_404
from .models import Order
def home(request):
    return render(request, 'menu/home.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'menu/category_list.html'
    context_object_name = 'categories'


class DishListView(ListView):
    model = Dish
    template_name = 'menu/dish_list.html'
    context_object_name = 'dishes'


class OrderListView(ListView):
    model = Order
    template_name = 'menu/order_list.html'
    context_object_name = 'orders'


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST, prefix='form')
        if form.is_valid() and formset.is_valid():
            order = form.save()
            items = formset.save(commit=False)
            for item in items:
                item.order = order
                item.save()
            return redirect('order_list')
    else:
        form = OrderForm()
        formset = OrderItemFormSet(prefix='form')
    return render(request, 'menu/create_order.html', {'form': form, 'formset': formset})



def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    items = order.orderitem_set.all()
    total = sum(item.dish.price * item.quantity for item in items)
    return render(request, 'menu/order_detail.html', {
        'order': order,
        'items': items,
        'total': total
    })

