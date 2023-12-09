from distutils.util import strtobool

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from bd.models import Products, Companies, Orders, Users, Stock, Managers, Statuses


def home(request):
    product = Products.objects.all()
    p_count = len(product)
    company = Companies.objects.all()
    order = Orders.objects.all().order_by('id')
    user = Users.objects.all()
    stock = Stock.objects.all()
    manager = Managers.objects.all()
    status = Statuses.objects.all()
    data = {
        'product': product,
        'company': company,
        'order': order,
        'user': user,
        'stock': stock,
        'manager': manager,
        'status': status,
        'pcount': p_count,
    }
    return render(request, 'СС.html', data)
def create_product(request):
    company = Companies.objects.all()
    model = Stock.objects.all()
    data = {
        'company': company,
        'model': model
    }
    return render(request, 'Product-formcreate.html', data)

def add_new_product(request):
    p = Products.objects.all()
    id = len(p) + 1
    if request.method == 'POST':
        model = Products()
        model.id = id
        model.price = request.POST.get('price')
        model.productname = request.POST.get('productname')
        model.abouproduct = request.POST.get('aboutproduct')

        instock_str = request.POST.get('instock')
        quantityid = request.POST.get('quantityid')
        companyid = request.POST.get('companyid')

        quantity = get_object_or_404(Stock, id=quantityid)
        company = get_object_or_404(Companies, id=companyid)
        instock = strtobool(instock_str)

        model.quantityid = quantity
        model.instock = instock
        model.companyid = company

        model.save()

        return redirect(home)
def add_product(request):
    product = Products.objects.all()
    company = Companies.objects.all()
    model = Stock.objects.all()
    data = {
        'product': product,
        'company': company,
        'model': model
    }
    return render(request, 'Product-form.html', data)

def get_product_data(request):
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Products, id=product_id)
    models = Stock.objects.values_list('model')
    companies = Companies.objects.values_list('company')
    companies_list = list(Companies.objects.values_list('id'))
    models_list = list(Stock.objects.values_list('id'))
    data = {
        'productname': product.productname,
        'companyid': companies_list,
        'aboutproduct': product.abouproduct,
        'price': product.price,
        'instock': product.instock,
        'quantityid': models_list,
        'all_companies': list(companies),
        'all_quantities': list(models)
    }

    return JsonResponse(data)

def save_product(request):
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Products, id = product_id)
    if request.method == 'POST':
        productname = request.POST.get('productname')
        aboutproduct = request.POST.get('aboutproduct')
        price = request.POST.get('price')
        instock_str = request.POST.get('instock')
        quantityid = request.POST.get('quantityid')
        companyid = request.POST.get('companyid')

        quantity = get_object_or_404(Stock, id=quantityid)
        company = get_object_or_404(Companies, id = companyid)
        instock = strtobool(instock_str)

        product.productname = productname
        product.abouproduct = aboutproduct
        product.price = price
        product.instock = instock
        product.quantityid = quantity
        product.companyid = company

        product.save()
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

def on_delete(request):
    product = Products.objects.all()
    return render(request, 'Product-formdeletes.html', {'product': product})

def delete(request):
    product = get_object_or_404(Products, id = request.POST.get('productname'))
    product.delete()
    return redirect(home)

