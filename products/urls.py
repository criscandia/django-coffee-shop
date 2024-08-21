# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Ruta para la vista index
    path(
        "agregar-producto/", views.ProductFormView.as_view(), name="add_product"
    ),  # Ruta para la vista ProductFormView
    path("products/", views.Products, name="products"),  # Ruta para la vista Products
]
