from django.urls import path
from . import views

urlpatterns = [
    #path('', views.product_list, name="product_list"),
    path('', views.ProductList.as_view(), name="product_list"),
    path('create/', views.ProductCreate.as_view(), name="product_create"),
    path('edit/<int:pk>', views.ProductEdit.as_view(), name="product_edit"),  
    path('delete/<int:pk>', views.ProductDelete.as_view(), name="product_delete"),
]