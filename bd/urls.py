
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('addproduct/', views.add_product),
    path('get_product_data/', views.get_product_data, name='get_product_data'),
    path('save_product/', views.save_product, name = 'save_product'),
    path('createproduct/', views.create_product, name ='create_product'),
    path('create-product/', views.add_new_product, name ='create-product'),
    path('productdelete', views.on_delete),
    path('delete/', views.delete, name ='product-delete')
]