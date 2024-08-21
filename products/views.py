from django.shortcuts import render
from .models import Product
from django.views import generic
from .forms import ProductForm
from django.urls import reverse_lazy
from django.contrib import messages


class ProductFormView(generic.FormView):
    template_name = "add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("products")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Producto agregado exitosamente.")
        return super().form_valid(form)


# Create your views here.


def index(request):
    return render(request, "index.html")


class ProductFormView(
    generic.FormView
):  # FormView es una vista que se encarga de mostrar un formulario
    template_name = "add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy(
        "products"
    )  # Reverse_lazy es una funcion que me permite redirigir a una url

    def form_valid(self, form):  # Metodo que se ejecuta cuando el formulario es valido
        form.save()
        messages.success(self.request, "Product succesfully added")
        return super().form_valid(form)


def Products(request):
    products = Product.objects.all()
    data = {"products": products}
    return render(request, "products.html", data)
