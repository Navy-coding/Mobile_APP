from .models import Product, Order, User
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.core.paginator import Paginator


def user_login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'token': user.auth_token.key})
    else:
        return JsonResponse({'error': 'Invalid email or password'}, status=401)

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return JsonResponse({'products': [{'id': p.id, 'name': p.name, 'price': p.price, 'quantity': p.quantity}
                                      for p in products]})

def place_order(request):
    products = Product.objects.get(id=request.POST.get('product'))
    products_quantity = request.POST['quantity']
    products = Product.objects.get(id=products)
    if products.products_quantity < quantity:
        return JsonResponse({'error': 'Not enough product in stock'}, status=400)
    else:
        products.products_quantity -= products_quantity
        products.save()
        Order.objects.create(user=request.user, products=products, products_quantity=products_quantity)
        return JsonResponse({'message': 'Order placed successfully'})

def order_history(request):
    orders = Order.objects.filter(customer=request.user)
    return JsonResponse({'orders': [{'product': o.product.name, 'quantity': o.quantity, 'date': o.date} for o in orders]})