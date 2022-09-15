from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.
@login_required(redirect_field_name='next', login_url='login')
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            #clear cart
            cart.clear()
            return render(request, 'orders/created.html', {'order': order})
    else:
      form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})