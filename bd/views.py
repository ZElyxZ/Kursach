from django.shortcuts import render

from bd.models import Products, Companies, Orders, Users, Stock, Managers, Statuses


def home(request):
    product = Products.objects.all()
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
        'status': status
    }
    return render(request, 'СС.html', data)
