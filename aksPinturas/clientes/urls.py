from django.urls import path
from . import views

urlpatterns = [
    #path('', views.client_list, name="client_list"),
    path('', views.ClienteList.as_view(), name="client_list"),
    #path('edit/', views.client_edit, name="client_edit"),
    path('edit/<int:pk>', views.ClienteEdit.as_view(), name="client_edit"),
    #path('create/', views.client_create, name="client_create"),
    path('create/', views.ClienteCreate.as_view(), name="client_create"),
    path('delete/<int:pk>', views.ClientestDelete.as_view(), name="client_delete"),
]