from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    # path('create/', views.product_create, name='product_create'),
    # path('edit/<int:product_id>/', views.product_create, name='product_edit'),
    # path('delete/<int:product_id>/', views.product_delete, name='product_delete'),
]
