from django.shortcuts import render
from .models import Customer, Tag, Product, Order


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'cloth/customer_list.html', {'customers': customers})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'cloth/tag_list.html', {'tags': tags})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'cloth/product_list.html', {'products': products})


def create_order(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        product_id = request.POST.get('product')
        status = request.POST.get('status')

        customer = Customer.objects.get(id=customer_id)
        product = Product.objects.get(id=product_id)

        Order.objects.create(customer=customer, product=product, status=status)

        return render(request, 'cloth/order_success.html')

    customers = Customer.objects.all()
    products = Product.objects.all()
    return render(request, 'cloth/create_order.html', {'customers': customers, 'products': products})
