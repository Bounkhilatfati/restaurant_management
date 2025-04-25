from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Category, Dish, Order
from .forms import CategoryForm, DishForm, OrderForm, OrderItemFormSet

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

def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        formset = OrderItemFormSet(request.POST, instance=order, prefix='form')
        if form.is_valid() and formset.is_valid():
            items = formset.save(commit=False)
            for item in items:
                if not item.order_id:
                    item.order = order
                item.save()
            formset.save()  # Save deletions and other changes
            form.save()
            return redirect('order_list')
        else:
            # Debugging: print form and formset errors
            print("Form errors:", form.errors)
            print("Formset errors:", formset.errors)
            return render(request, 'menu/create_order.html', {'form': form, 'formset': formset, 'edit': True})
    else:
        form = OrderForm(instance=order)
        formset = OrderItemFormSet(instance=order, prefix='form')
    return render(request, 'menu/create_order.html', {'form': form, 'formset': formset, 'edit': True})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'menu/order_confirm_delete.html', {'order': order})

def dish_create(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'menu/dish_form.html', {'form': form})

def dish_edit(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm(instance=dish)
    return render(request, 'menu/dish_form.html', {'form': form, 'dish': dish})

def dish_delete(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        dish.delete()
        return redirect('dish_list')
    return render(request, 'menu/dish_confirm_delete.html', {'dish': dish})
